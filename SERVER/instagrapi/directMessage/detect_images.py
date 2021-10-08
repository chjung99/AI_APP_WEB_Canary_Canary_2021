from instagrapi import *
# TODO : image를 download 한 후, Canary_YOLOv5 에서 detect.py 돌리기
# 처리 완료 했으면 이미지 삭제하기

def detectWithCanary():
    testNeededUserNumber = len(os.listdir(f'{IMAGE_DOWNLOAD_ROOT}'))
    return testNeededUserNumber
    # for i in range(testNeededUserNumber):
