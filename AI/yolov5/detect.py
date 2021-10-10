import torch
import argparse
import cv2
import os
import json
import requests
from google_drive_downloader import GoogleDriveDownloader as gdd

MOSAIC_RATIO = 0.05

def attemp_download_weight():
    if not os.path.exists('./weight'):
        os.makedirs('./weight')
    
    with open('./config.json') as json_file:
        json_data = json.load(json_file)
    
    if os.path.exists('./weight/yolov5m6.pt'): return
    
    try:
        data = requests.get("http://52.14.108.141:8080/deeplearning/models").json()
        version = data['version']
        model_url = data['file']
        
        print(data)
        
        if json_data['version'] < version:
            r = requests.get(model_url)
            with open('./weight/yolov5m6.pt', 'wb') as f: f.write(r.content)
            json_data['version'] = version
            with open('./weight/config.json', 'w') as json_file: json.dump(json_data, json_file)
            
    except:
        if os.path.exists('./weight/yolov5m6.pt'):
            os.remove('./weight/yolov5m6.pt')
        
        yolov5m6_id = '1F6e6fztaSjzY_XZMFqqrLJv-QDo5eQ_a'
        gdd.download_file_from_google_drive(file_id=yolov5m6_id, dest_path=f'weight/yolov5m6.pt', showsize=True)
    
    

# def mosaic()

def detect(args):
# Model
    input_image_path = args.input_image_path
    output_image_path = args.output_image_path
    weight_path = args.weight_path
    activeBlur = args.blur

    model = torch.hub.load('ultralytics/yolov5', 'custom', path=weight_path)
    
    # Inference
    results = model(input_image_path)
    img = cv2.imread(input_image_path)

    if activeBlur == True:
        # TODO : Blur
        print("Not yet!")
    else:
        for xmin, ymin, xmax, ymax, conf, class_num in results.xyxy[0]:
            if class_num == 1 or 6:
                print("Military uniform or bulletproof vest detected. Pass mosaic")
                continue

            xmin = int(xmin); xmax = int(xmax); ymin = int(ymin); ymax = int(ymax)
            src = img[ymin: ymax, xmin: xmax]   # 관심영역 지정


            small = cv2.resize(src, None, fx=MOSAIC_RATIO, fy=MOSAIC_RATIO, interpolation=cv2.INTER_NEAREST)
            src = cv2.resize(small, src.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)
            
            img[ymin: ymax, xmin: xmax] = src   # 원본 이미지에 적용
        cv2.imwrite(output_image_path, img)

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--input_image_path', '-i')
parser.add_argument('--output_image_path', '-o')
parser.add_argument('--weight_path', '-w')
parser.add_argument('--blur', '-b', action="store_true")
# parser.add_argument('--strength', '-s', type='int', default=100, choices=[50, 75, 100])

# TODO: arg로 mosaic 강도를 입력받고, 그 만큼 면적을 줄여서 return
# TODO: output_warning_path를 입력받아 군복, 방탄조끼 class가 포함되어 있을 시 경고문 전달?


args = parser.parse_args()

attemp_download_weight()
detect(args)