# YOLOv5 🚀 by Ultralytics, GPL-3.0 license
"""
Run inference on images, videos, directories, streams, etc.

Usage:
    $ python path/to/detect.py --source path/to/img.jpg --weights yolov5s.pt --img 640
"""

import argparse
import sys
from pathlib import Path

import cv2
import torch


from models.experimental import attempt_load
from utils.datasets import LoadImages
from utils.general import check_img_size, non_max_suppression, save_one_box, scale_coords
from utils.torch_utils import time_sync


@torch.no_grad()
def run(weights='weight/yolov5s6.pt ',  # model.pt path(s)
        source='image/soldier2.jpg',  # file/dir/URL/glob, 0 for webcam
        dest='image/out.jpg',
        imgsz=640,  # inference size (pixels)
        conf_thres=0.25,  # confidence threshold
        iou_thres=0.45,  # NMS IOU threshold
        ):

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


    model = attempt_load(weights, map_location=device)  # load FP32 model
    stride = int(model.stride.max())  # model stride
    names = model.module.names if hasattr(model, 'module') else model.names  # get class names
    
    imgsz = check_img_size(imgsz, s=stride)  # check image size

    # Dataloader
   
    dataset = LoadImages(source, img_size=imgsz, stride=stride)
    bs = 1  # batch_size

    # Run inference
    if device.type != 'cpu':
        model(torch.zeros(1, 3, *imgsz).to(device).type_as(next(model.parameters())))  # run once
    dt = [0.0, 0.0, 0.0]
    for path, img, im0, vid_cap in dataset:
        img = torch.from_numpy(img).to(device)
        img = img.float()  # uint8 to fp16/32
        img = img / 255.0  # 0 - 255 to 0.0 - 1.0
        if len(img.shape) == 3:
            img = img[None]  # expand for batch dim

        # Inference
        pred = model(img)[0]
        # NMS
        pred = non_max_suppression(pred, conf_thres, iou_thres)

        # Process predictions
        for i, det in enumerate(pred):  # per image

            if len(det):
                # Rescale boxes from img_size to im0 size
                det[:, :4] = scale_coords(img.shape[2:], det[:, :4], im0.shape).round()
                    
                ratio = 0.1
                # Write results
                for xmin, ymin, xmax, ymax, conf, class_num in reversed(det):
                    src = im0[int(ymin): int(ymax), int(xmin): int(xmax)]   # 관심영역 지정
                    small = cv2.resize(src, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
                    src = cv2.resize(small, src.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)
                    im0[int(ymin): int(ymax), int(xmin): int(xmax)] = src 
                    

            # Save results (image with detections)
            cv2.imwrite(dest, im0)
                

   
    print(f"Results saved to {dest}")


def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--weights', nargs='+', type=str, default='weight/yolov5s6.pt ', help='model path(s)')
    parser.add_argument('--source', type=str, default='image/out.jpg', help='file/dir/URL/glob, 0 for webcam')
    parser.add_argument('--dest', type=str, default='image/soldier2.jpg ', help='file/dir/URL/glob, 0 for webcam')
    parser.add_argument('--imgsz', '--img', '--img-size', nargs='+', type=int, default=[640], help='inference size h,w')
   
    opt = parser.parse_args()
    opt.imgsz *= 2 if len(opt.imgsz) == 1 else 1  # expand
    return opt


def main(opt):
    run(**vars(opt))


opt = parse_opt()
main(opt)
