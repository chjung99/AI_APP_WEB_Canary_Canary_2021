import torch
import argparse
import cv2
import os
import json
import requests
import urllib.request
from google_drive_downloader import GoogleDriveDownloader as gdd

MOSAIC_RATIO = 0.05

def check_config(path='./config.json'):
    if os.path.exists(path):
        with open(path) as json_file:
            json_data = json.load(json_file)
    else:
        json_data = {"version": 0}
        with open(path, 'w') as outfile:
            json.dump(json_data, outfile)

def attemp_download_weight():
    if not os.path.exists('./weight'): os.makedirs('./weight')
    
    config_path = './config.json'
    check_config(config_path)
    
    try:
        with open(config_path) as json_file:
            json_data = json.load(json_file)
    
        data = requests.get("http://52.14.108.141:8080/deeplearning/models").json()
        print(data)
        version = data['version']
        model_url = data['file']
        
        if json_data['version'] < version or not os.path.exists('weight/yolov5m6.pt'):
            json_data['version'] = version
            with open('./weight/config.json', 'w') as json_file: json.dump(json_data, json_file)
            
            
            urllib.request.urlretrieve(model_url, 'weight/yolov5m6.pt') 
            
    except:       
        yolov5m6_id = '1QUaufxw06NVPyn_tIm0qBdOy5ewQ5ffi'
        gdd.download_file_from_google_drive(file_id=yolov5m6_id, dest_path=f'weight/yolov5m6.pt', showsize=True)

    

# def mosaic()

def detect(args):
# Model
    input_image_path = args.input_image_path
    output_image_path = args.output_image_path
    
    weight_path = args.weight_path
    activeBlur = args.blur
    # strength = args.strength
    output_warning_path = args.output_warning_path
    output_log_path=args.output_log_path
    model = torch.hub.load('ultralytics/yolov5', 'custom', path=weight_path)

    # Inference
    results = model(input_image_path)
    img = cv2.imread(input_image_path)
    CLASS_LIST = ['항공모함', '방탄조끼', '포', '모니터', '군용 차량', '노트북', '군복', '미사일', '모니터', '서류', '부대마크', '리볼버', '소총', '탱크', '군 항공기', '군 표지판']
    
    if activeBlur == True:
        # TODO : Blur
        print("Not yet!")
    else:
        flag=0
        warn_list = []
        if args.strength == 0:
          keep_data=[]
          for xmin, ymin, xmax, ymax, conf, class_num in results.xyxy[0]:
              class_num = int(class_num)
              if(class_num!=6):
                if class_num==3 or class_num==5 or class_num==8 or class_num==9:
                  flag=1
                  break
                continue
              xmin = int(xmin); xmax = int(xmax); ymin = int(ymin); ymax = int(ymax)
              src = img[ymin: ymax, xmin: xmax].copy()   # 관심영역 지정
              tmp_img=src
                  # import pdb;pdb.set_trace()
              keep_data.append((xmin, ymin, xmax, ymax,tmp_img))
        for xmin, ymin, xmax, ymax, conf, class_num in results.xyxy[0]:
            xmin = int(xmin); xmax = int(xmax); ymin = int(ymin); ymax = int(ymax)
            src = img[ymin: ymax, xmin: xmax]   # 관심영역 지정
            class_num = int(class_num)
            if class_num >= 16: continue
            warn_list.append(CLASS_LIST[class_num])
            if class_num == 6:
                
                print("Military uniform is detected. Pass mosaic")
                continue

            small = cv2.resize(src, None, fx=MOSAIC_RATIO, fy=MOSAIC_RATIO, interpolation=cv2.INTER_NEAREST)
            src = cv2.resize(small, src.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)
            
            img[ymin: ymax, xmin: xmax] = src   # 원본 이미지에 적용

        if args.strength == 0 and flag==0 :
          for data in keep_data:
            
            img[data[1]:data[3],data[0]:data[2]]=data[4]
          
        cv2.imwrite(output_image_path, img)
        warn_list = ','.join(list(set(warn_list)))

        if warn_list:
            warn_text = f'{warn_list} (이/가) 감지되었습니다.'
            if ("모니터" in warn_list or "서류" in warn_list or "노트북" in warn_list):
              warn_text +='혹시 지금 군사 기밀을 노출하진 않으셨나요?'
              risk_level=5
            elif ("소총" in warn_list or "리볼버" in warn_list or "포" in warn_list or "탱크" in warn_list or "군항공기" in warn_list or "미사일" in warn_list or "방탄조끼" in warn_list):
              warn_text +='지금 훈련 중이신가요? 훈련모습 촬영은 규정에 어긋납니다!'
              risk_level=3
            elif ('군용 차량' in warn_list):
              warn_text +='군용 차량을 촬영하셨네요.차종 및 번호판 식별 위험이있습니다.'
              risk_level=2
            elif ('부대마크' in warn_list):
              warn_text +='부대마크 및 명칭 노출은 군사보안에 위배되는 사항입니다.'
              risk_level=2
            elif ('항공모함' in warn_list):
              warn_text +='설마 한미연합훈련 중 카메라를 사용하시는 건 아니겠죠?'
              risk_level=2
            elif ('군 표지판' in warn_list):
              warn_text +='군 표지판 촬영은 부대 위치가 식별될 위험이 있습니다.'
              risk_level=3
            else:
              warn_text +='군복을 입고 찍는 기념 사진인가요? 훈련 중이 아니길 빌어요!'
              risk_level=1
        else:
            warn_text = '아무런 객체가 검출되지 않았습니다.'
            risk_level=0
        with open(output_warning_path, 'w') as f:
            f.write(warn_text)
        with open(output_log_path, 'w') as f:
            log_text='user_id:'+f'{args.user_id}/object:'+f'{warn_list}/risk level:'+f'{risk_level}'
            f.write(log_text)



parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--input_image_path', '-i', help='Input image path')
parser.add_argument('--output_image_path', '-o', help='Output image path')
parser.add_argument('--weight_path', '-w', help='Weight path')
parser.add_argument('--blur', '-b', action="store_true")

parser.add_argument('--output_warning_path', '-o2', help='Warning text path')


parser.add_argument('--strength', '-s', type=int, default=1, choices=[0,1]) # test 후 결과에 따라 강도 조정 예정 --> 찬호님이 자동 적응 mosaic 진행중
parser.add_argument('--user_id', '-d', help='user_id') # user_id from front
parser.add_argument('--output_log_path', '-o3', help='output_log_path') # user_id from front
# TODO: arg로 mosaic 강도를 입력받고, 그 만큼 면적을 줄여서 return
# TODO: output_warning_path를 입력받아 군복, 방탄조끼 class가 포함되어 있을 시 경고문 전달? 해결


args = parser.parse_args()
attemp_download_weight()
detect(args)