import torch
import argparse
import cv2
import os
import json
from google_drive_downloader import GoogleDriveDownloader as gdd

def attemp_download_weight():
    if not os.path.exists('./weight'):
        os.makedirs('./weight')
    
    # with open('./weight/config.json') as json_file:
    #     json_data = json.load(json_file)
        
    
    yolov5l6_id = '1sYHRy8uvBFJbNOPzOlzjEh3VUorHTy8S'
    yolov5m6_id = '1F6e6fztaSjzY_XZMFqqrLJv-QDo5eQ_a'
    yolov5s6_id = '1eAxFouSUlFlnMiooidbV3uI37hq5xXLo'
    
    for Id, file_name in ((yolov5s6_id, 'yolov5s6.pt'), (yolov5m6_id, 'yolov5m6.pt'), (yolov5l6_id, 'yolov5l6.pt')):
        gdd.download_file_from_google_drive(file_id=Id, dest_path=f'weight/{file_name}', showsize=True)

def mosaic()

def detect(input_image_path, output_image_path, weight_path):
# Model
    model = torch.hub.load('ultralytics/yolov5', 'custom', path=weight_path)
    
    # Inference
    results = model(input_image_path)
    
    ratio = 0.05
    img = cv2.imread(input_image_path)
    for xmin, ymin, xmax, ymax, conf, class_num in results.xyxy[0]:
        src = img[int(ymin): int(ymax), int(xmin): int(xmax)]   # 관심영역 지정
        
        small = cv2.resize(src, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
        src = cv2.resize(small, src.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)
        
        img[int(ymin): int(ymax), int(xmin): int(xmax)] = src   # 원본 이미지에 적용
    cv2.imwrite(output_image_path, img)
    

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--input_image_path', '-i')
parser.add_argument('--output_image_path', '-o')
parser.add_argument('--weight_path', '-w')

args = parser.parse_args()

attemp_download_weight()
detect(args.input_image_path, argparse.output_image_path, args.weight_path)