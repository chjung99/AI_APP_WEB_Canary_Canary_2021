import torch
import argparse
import cv2
import os
import json
import requests
import urllib.request
from google_drive_downloader import GoogleDriveDownloader as gdd

MOSAIC_RATIO = 0.05

def check_config(path="./config.json"):
    if os.path.exists(path):
        with open(path) as json_file:
            json_data = json.load(json_file)
            
        if "matrix" in json_data: return

    json_data = {"matrix": 0}
    with open(path, "w") as outfile:
        json.dump(json_data, outfile)

def download_file_from_google_drive():
    if not os.path.exists("weight/yolov5m6.pt"):
        print("download model from google drive")
        yolov5m6_id = "1QUaufxw06NVPyn_tIm0qBdOy5ewQ5ffi"
        gdd.download_file_from_google_drive(file_id=yolov5m6_id, dest_path=f"weight/yolov5m6.pt", showsize=True)

def attemp_download_weight(args):
    if not os.path.exists("./weight"): os.makedirs("./weight")
    
    config_path = "./config.json"
    check_config(config_path)
    
    try:
        with open(config_path) as json_file:
            json_data = json.load(json_file)
    
        data = requests.get(f"{args.server_url}/deeplearning/models", timeout=1).json()
        matrix = data["matrix"]
        model_url = data["file"]
        
        if json_data["matrix"] < matrix or not os.path.exists("weight/yolov5m6.pt"):
            print("download model from django")
            json_data["matrix"] = matrix
            with open("./weight/config.json", "w") as json_file: json.dump(json_data, json_file)
            urllib.request.urlretrieve(model_url, "weight/yolov5m6.pt") 
            
    except:       
        download_file_from_google_drive()

    

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
    
    try:
        model = torch.hub.load("ultralytics/yolov5", "custom", path=weight_path)
    except:
        os.remove("weight/yolov5m6.pt")
        download_file_from_google_drive()
        model = torch.hub.load("ultralytics/yolov5", "custom", path=weight_path)

    # Inference
    results = model(input_image_path)
    img = cv2.imread(input_image_path)
    
    class_list = ["항공모함", "방탄조끼", "포", "모니터", "군용 차량", "노트북", "군복", "미사일", "모니터", "서류", "부대마크", "리볼버", "소총", "탱크", "군 항공기", "군 표지판"]
    scenario_log_list = [("설마 한미연합훈련 중 카메라를 사용하시는 건 아니겠죠?", 2), ("지금 훈련 중이신가요? 훈련모습 촬영은 규정에 어긋납니다!", 3), ("혹시 지금 군사 기밀을 노출하진 않으셨나요?", 5),
        ("군용 차량을 촬영하셨네요.차종 및 번호판 식별 위험이있습니다.", 2), ("군 표지판 촬영은 부대 위치가 식별될 위험이 있습니다.", 3), ("부대마크 및 명칭 노출은 군사보안에 위배되는 사항입니다.")]

    class_senerio_map = {0: 0, 1:1, 2:1, 3: 2, 4:3, 5:2, 6:1, 7:1, 8:2, 9:1, 10:5, 11:1, 12:1, 13:1, 14:1, 15:4}
    
    if activeBlur == True:
        # TODO : Blur
        print("Not yet!")
    else:
        flag=0
        object_list = set()
        
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
            class_num = int(class_num)
            if class_num >= 16: continue
            object_list.add(class_num)
        
            xmin = int(xmin); xmax = int(xmax); ymin = int(ymin); ymax = int(ymax)
            src = img[ymin: ymax, xmin: xmax]   # 관심영역 지정
            small = cv2.resize(src, None, fx=MOSAIC_RATIO, fy=MOSAIC_RATIO, interpolation=cv2.INTER_NEAREST)
            src = cv2.resize(small, src.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)
            
            img[ymin: ymax, xmin: xmax] = src   # 원본 이미지에 적용

        if args.strength == 0 and flag==0 :
          for data in keep_data:
            
            img[data[1]:data[3],data[0]:data[2]]=data[4]
          
        cv2.imwrite(output_image_path, img)
        
        risk_level=0
        
        warn_object_txt = ",".join(map(lambda x: class_list[x], object_list))
        if object_list:
            warn_text = f"{warn_object_txt} (이/가) 감지되었습니다."
            
            for _object in object_list:
                senario_index = class_senerio_map[_object]
                warn_text += scenario_log_list[senario_index][0]
                risk_level = max(risk_level, scenario_log_list[senario_index][1])
        else:
            warn_text = "아무런 객체가 검출되지 않았습니다."
        
        with open(output_warning_path, "w") as f:
            f.write(warn_text)
            
        with open(output_log_path, "w") as f:
            log_text="user_id:"+f"{args.user_id}/object:"+f"{warn_object_txt}/risk level:"+f"{risk_level}"
            f.write(log_text)
            
        try:
            print("send log")
            data = {'log': str(warn_object_txt), 'username': str(args.user_id)} 
            res = requests.post(f"{args.server_url}/deeplearning/log/api", data=data, timeout=1)
        except:
            print("send fail")



parser = argparse.ArgumentParser(description="Process some integers.")
parser.add_argument("--input_image_path", "-i", help="Input image path")
parser.add_argument("--output_image_path", "-o", help="Output image path")
parser.add_argument("--weight_path", "-w", help="Weight path")
parser.add_argument("--blur", "-b", action="store_true")

parser.add_argument("--output_warning_path", "-o2", help="Warning text path")
parser.add_argument("--server_url", "-u", default='http://3.143.240.128:8080', help="Django URL")


parser.add_argument("--strength", "-s", type=int, default=1, choices=[0,1]) # test 후 결과에 따라 강도 조정 예정 --> 찬호님이 자동 적응 mosaic 진행중
parser.add_argument("--user_id", "-d", help="user_id") # user_id from front
parser.add_argument("--output_log_path", "-o3", help="output_log_path") # user_id from front
# TODO: arg로 mosaic 강도를 입력받고, 그 만큼 면적을 줄여서 return
# TODO: output_warning_path를 입력받아 군복, 방탄조끼 class가 포함되어 있을 시 경고문 전달? 해결


args = parser.parse_args()
attemp_download_weight(args)
detect(args)
