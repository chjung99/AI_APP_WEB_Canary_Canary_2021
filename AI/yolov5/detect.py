import torch
import argparse
import cv2
import os
import json
import requests
import urllib.request
from google_drive_downloader import GoogleDriveDownloader as gdd

MOSAIC_RATIO = 0.05
#progress_path = "image/progress_"

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
        #with open(progress_path, "w") as pro:
            #pro.write("서버에 접속 중...\n")

        matrix = data["matrix"]
        model_url = data["file"]
        
        if json_data["matrix"] < matrix or not os.path.exists("weight/yolov5m6.pt"):
            print("download model from django")
            json_data["matrix"] = matrix
            with open(config_path, "w") as json_file: json.dump(json_data, json_file)
            urllib.request.urlretrieve(model_url, "weight/yolov5m6.pt") 
            
    except:       
        download_file_from_google_drive()

    

# def mosaic()

def detect(args):
# Model
    #with open(progress_path, "a") as pro:
        #pro.write("보안위반 가능성 오브젝트 검사 중...\n")
    input_image_path = args.input_image_path
    # output_image_path = args.output_image_path
    
    weight_path = args.weight_path
    activeBlur = args.blur
    # strength = args.strength
    # output_warning_path = args.output_warning_path
    # output_log_path=args.output_log_path
    
    try:
        model = torch.hub.load("ultralytics/yolov5", "custom", path=weight_path)
    except:
        os.remove("weight/yolov5m6.pt")
        download_file_from_google_drive()
        model = torch.hub.load("ultralytics/yolov5", "custom", path=weight_path)

    # Inference
    results = model(input_image_path)

    return results


def mosaic(results, args):
    #with open(progress_path, "a") as pro:
        #pro.write("보안위반 가능성 오브젝트 처리 중...\n")
    input_image_path = args.input_image_path
    output_image_path = args.output_image_path
    
    # weight_path = args.weight_path
    active_Blur = args.blur
    strength = args.strength
    output_warning_path = args.output_warning_path
    output_log_path=args.output_log_path

    img = cv2.imread(input_image_path)

    warning_law = '군사기밀 유출시 군사기밀보호법, 보안업무규정, 정보 및 보안업무기획·조정규정, 정보통신기반 보호법, 군사기지 및 군사시설 보호법, 군형법 80조에 의거한 처벌 가능성이 있습니다.'
    # 근거 : https://www.dssc.mil.kr/dssckr/123/subview.do
    warning_sns = "군인의 근무, 훈련 중 휴대전화 및 카메라 사용은 근무태만 및 군 SNS 행동강령 위반에 해당될 수도 있습니다. SNS에 군 사기와 기강을 훼손하는 글을 올리지 않게 주의해주시기 바랍니다."
    avoid_responsibility = "본 프로그램의 결과는 법적 효력이 없으며, 보안 사고 발생 시 모든 책임은 사용자 측에 있습니다."
    DSSC_support_not_violation = """\
        일상적인 軍 복무 경험담 및 병영생활 이야기
        부분적인 군사시설을 배경으로 촬영한 사진(위치 및 구조가 판단되지 않는 범위)
        ＊ 단, 사진에 군사비밀(자료)이 포함될 경우 신고대상임.
        소규모 부대 현행작전 등 단순한 軍 활동 내용
        과거 군 교육ㆍ훈련사진
        무기체계의 제원 및 외형사진 등 공공기관ㆍ대외학술지를 통해 이미 공개된 내용
        ＊ 단, 특별 관리하는 무기체계 및 비공개된 무기체계 자료에 대한 내용은 신고대상임.
        인터넷 위성지도 서비스 등을 통해 軍 시설에 대한 현황을 표시한 내용
        자신이 복무했던 부대 위치 및 찾아가는 방법
        ＊ 단, 대규모 부대의 위치 및 좌표, 고유명칭ㆍ통상명칭 등을 한번에 표시한 것은 신고대상임."""
    # 출처 : https://www.dssc.mil.kr/dssckr/151/subview.do

    
    img = cv2.imread(input_image_path)

    class_list = ["항공모함", "방탄조끼", "포", "모니터", "군용 차량", "노트북", "군복", "미사일", "모니터", "서류", "부대마크", "리볼버", "소총", "탱크", "군 항공기", "군 표지판"]

    scenario_log_list = [("설마 한미연합훈련 중 카메라를 사용하시는 건 아니겠죠?", 2), ("지금 훈련 중이신가요? 훈련모습 촬영은 규정에 어긋납니다!", 3), ("혹시 지금 군사 기밀을 노출하진 않으셨나요?", 5),
        ("군용 차량을 촬영하셨네요.차종 및 번호판 식별 위험이있습니다.", 2), ("군 표지판 촬영은 부대 위치가 식별될 위험이 있습니다.", 3), ("부대마크 및 명칭 노출은 군사보안에 위배되는 사항입니다.", 3)]


    class_senerio_map = {0: 0, 1:1, 2:1, 3: 2, 4:3, 5:2, 6:1, 7:1, 8:2, 9:1, 10:5, 11:1, 12:1, 13:1, 14:1, 15:4}
    
    if active_Blur == True:
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

        if strength == 0 and flag == 0 :
          for data in keep_data:
            
            img[data[1]:data[3],data[0]:data[2]]=data[4]
          
        cv2.imwrite(output_image_path, img)

        #with open(progress_path, "a") as pro:
            #pro.write("경고문 작성 중...\n")
        
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

        warn_text += warning_law
        warn_text += avoid_responsibility
        
        with open(output_warning_path, "w") as f:
            f.write(warn_text)
            
        with open(output_log_path, "w") as f:
            log_text="user_id:"+f"{args.user_id}/object:"+f"{warn_object_txt}/risk level:"+f"{risk_level}"
            f.write(log_text)
            
        #with open(progress_path, "a") as pro:
            #pro.write("처리된 이미지 반환 중...\n")  
            
        try:
            print("send log")
            data = {'log': str(warn_object_txt), 'username': str(args.user_id)} 
            res = requests.post(f"{args.server_url}/deeplearning/log", data=data, timeout=1)
        except:
            print("send fail")




parser = argparse.ArgumentParser(description="Process some integers.")
parser.add_argument("--input_image_path", "-i", help="Input image path")
parser.add_argument("--output_image_path", "-o", help="Output image path")
parser.add_argument("--weight_path", "-w", help="Weight path")
parser.add_argument("--blur", "-b", action="store_true")

parser.add_argument("--output_warning_path", "-o2", help="Warning text path")
parser.add_argument("--server_url", "-u", default='http://3.143.240.128:8080', help="Django URL")

parser.add_argument("--strength", "-s", type=int, default=1, choices=[0,1])
parser.add_argument("--user_id", "-d", help="user_id") # user_id from front
parser.add_argument("--output_log_path", "-o3", help="output_log_path") # user_id from front

args = parser.parse_args()

#progress_path += (args.user_id + '.txt')

attemp_download_weight(args)

results = detect(args)
mosaic(results, args)

