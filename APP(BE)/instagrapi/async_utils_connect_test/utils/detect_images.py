# -*- coding: utf-8 -*-
# TODO : image를 download 한 후, Canary_YOLOv5 에서 detect.py 돌리기
# 처리 완료 했으면 이미지 삭제하기
import os
from tqdm import tqdm
import sys
from os import path
import subprocess

# from get_client import *
from image_path import Roots
from make_directory import * # import all

'''
sys.path.append('/workspaces/AI_APP_WEB_Canary_Canary/AI(BE)/deeplearning/kwoledge_distillation_yolov5/yolov5')
from detect import *
'''

class detectArgs:
    input_image_path = ''
    output_image_path = ''
    weight_path = ''
    blur = False
    output_warning_path = ''
    strength = 1
    user_id = 1234
    output_log_path = ''

async def media_detect(user_pk):
    print('Start Detecting Imgs')
    test_needed_user_list = os.listdir(f'{Roots.IMAGE_DOWNLOAD_ROOT}')

    print(user_pk)
    print(test_needed_user_list)

    # Ouput Imgs/Warning/Log 위한 Directory 생성 함수 make_...
    if str(user_pk) in test_needed_user_list:
        save_imgs_OUTPUT(user_pk)
        save_warning(user_pk)
        save_log(user_pk)
    # make_dir_save_imgs 함수를 통해 insta_imgs 폴더 속에 사용자의 Pk로 된 폴더를 생성한 후 
    # make_directory_save_images(user_output_path)

    # image_download_root directory에 있는 user_pk 폴더의 파일 리스트를 가져온다
    test_needed_photo_list = os.listdir(f'{Roots.IMAGE_DOWNLOAD_ROOT}/{user_pk}')
    test_needed_photo_number = len(test_needed_photo_list)

    for j in tqdm(range(0, test_needed_photo_number)):
        print("== Photo Number : %d ==" % j)
        user_photo_path = f'{user_pk}/{test_needed_photo_list[j]}'
        user_warning_path = user_photo_path[:-4]
        IMAGE_INPUT_PATH = f'{Roots.IMAGE_DOWNLOAD_SHELL}/{user_photo_path}'
        IMAGE_OUTPUT_PATH = f'{Roots.IMAGE_OUTPUT_SHELL}/{user_photo_path}'
        WARNING_OUTPUT_PATH = f'{Roots.WARNING_OUTPUT_SHELL}/{user_warning_path}'+('.txt')
        LOG_OUTPUT_PATH = f'{Roots.LOG_OUTPUT_SHELL}/{user_warning_path}'+('.txt')

        args = detectArgs()
        args.input_image_path = f'{IMAGE_INPUT_PATH}'
        args.output_image_path = f'{IMAGE_OUTPUT_PATH}'
        args.weight_path = './weight/yolov5m6.pt'
        args.output_warning_path = f'{WARNING_OUTPUT_PATH}'
        args.user_id = "instagram" + f'{user_pk}'
        print(args.user_id)
        args.output_log_path = f'{LOG_OUTPUT_PATH}'

        command = f'python3 {Roots.SYS_PATH_ROOT} -i {args.input_image_path} -o {args.output_image_path} -w {args.weight_path} -o2 {args.output_warning_path} -d {args.user_id} -o3 {args.output_log_path}'
        # print(command)

        subprocess.run(command, shell=True)
        # os.system(command)
    else:
        print("No needed test\n")

# media_detect(12345678)