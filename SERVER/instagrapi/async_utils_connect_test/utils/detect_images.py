# TODO : image를 download 한 후, Canary_YOLOv5 에서 detect.py 돌리기
# 처리 완료 했으면 이미지 삭제하기
import os
from tqdm import tqdm
import sys
from os import path
print(path.dirname(path.dirname(path.dirname(path.dirname( path.dirname( path.abspath(__file__) ) )) )))
sys.path.append(path.dirname(path.dirname(path.dirname(path.dirname( path.dirname( path.abspath(__file__) ) )) )))
from AI.yolov5.detect import *
# from SERVER.instagrapi.async_utils_connect_test.utils.image_path import Roots
from SERVER.instagrapi.async_utils_connect_test.utils.make_directory import * # make_directory 함수들 import

class Roots:
    SYS_PATH_ROOT = '/workspaces/AI_APP_WEB_Canary_Canary'
    IMAGE_DOWNLOAD_ROOT = '/workspaces/AI_APP_WEB_Canary_Canary/SERVER/instagrapi/async_utils_connect_test/insta_imgs'
    IMAGE_OUTPUT_ROOT = '/workspaces/AI_APP_WEB_Canary_Canary/SERVER/instagrapi/async_utils_connect_test/insta_imgs_detected'
    WARNING_OUTPUT_ROOT = '/workspaces/AI_APP_WEB_Canary_Canary/SERVER/instagrapi/async_utils_connect_test/insta_imgs_warnings'
    LOG_OUTPUT_ROOT = '/workspaces/AI_APP_WEB_Canary_Canary/SERVER/instagrapi/async_utils_connect_test/log'

class detectArgs:
    input_image_path = ''
    output_image_path = ''
    weight_path = ''
    blur = False
    output_warning_path = ''
    strength = 1
    user_id = 1234
    output_log_path = ''

# if __name__ == '__main__':

#     if __package__ is None:
#         import sys
#         from os import path
#         print(path.dirname(path.dirname(path.dirname(path.dirname( path.dirname( path.abspath(__file__) ) )) )))
#         sys.path.append(path.dirname(path.dirname(path.dirname(path.dirname( path.dirname( path.abspath(__file__) ) )) )))
#         from AI.yolov5.detect import *
#         from SERVER.instagrapi.async_utils_connect_test.utils.image_path import Roots
#         from SERVER.instagrapi.async_utils_connect_test.utils.make_directory import * # make_directory 함수들 import


# def test_detect_images():
#     print('Testing Detect Imgs')
#     IMAGE_NAME = 'osam_testbot_2681938662589354460.jpg'
#     IMAGE_INPUT_PATH = f'{Roots.IMAGE_DOWNLOAD_ROOT}/{IMAGE_NAME}'
#     IMAGE_OUTPUT_PATH = f'{Roots.IMAGE_OUTPUT_ROOT}/{IMAGE_NAME}'
#     WARNING_OUTPUT_PATH = f'{Roots.WARNING_OUTPUT_ROOT}/{IMAGE_NAME}'
#     LOG_OUTPUT_PATH = f'{Roots.LOG_OUTPUT_ROOT}/{IMAGE_NAME}'

#     args = detectArgs()
#     args.input_image_path = f'{IMAGE_INPUT_PATH}'
#     args.output_image_path = f'{IMAGE_OUTPUT_PATH}'
#     args.weight_path = './weight/yolov5m6.pt'
#     args.output_warning_path = f'{WARNING_OUTPUT_PATH}'
#     args.output_log_path = f'{LOG_OUTPUT_PATH}'

#     detect(args)


# Detecting Imgs and Return Output & Warnings
# def detect_images():
#     print('Start Detecting Imgs')
#     test_needed_user_list = os.listdir(f'{Roots.IMAGE_DOWNLOAD_ROOT}')
#     test_needed_user_number = len(test_needed_user_list)

#     # make_dir_save_imgs 함수를 통해 insta_imgs 폴더 속에 사용자의 Pk로 된 폴더를 생성한 후 
#     # make_directory_save_images(user_output_path)
    
#     for i in tqdm(range(0, test_needed_user_number)):
#         print("== User Number : %d ==" % i)
#         # Ouput Imgs/Warning/Log 위한 Directory 생성 함수 make_...
#         make_directory_save_images(test_needed_user_list[i])
#         make_directory_save_warning(test_needed_user_list[i])
#         make_directory_save_log(test_needed_user_list[i])

#         test_needed_photo_list = os.listdir(f'{Roots.IMAGE_DOWNLOAD_ROOT}/{test_needed_user_list[i]}')
#         test_needed_photo_number = len(test_needed_photo_list)

#         for j in tqdm(range(0, test_needed_photo_number)):
#             print("== Photo Number : %d ==" % j)
#             user_photo_path = f'{test_needed_user_list[i]}/{test_needed_photo_list[j]}'
#             IMAGE_INPUT_PATH = f'{Roots.IMAGE_DOWNLOAD_ROOT}/{user_photo_path}'
#             IMAGE_OUTPUT_PATH = f'{Roots.IMAGE_OUTPUT_ROOT}/{user_photo_path}'
#             WARNING_OUTPUT_PATH = f'{Roots.WARNING_OUTPUT_ROOT}/{user_photo_path}'+('.txt')
#             LOG_OUTPUT_PATH = f'{Roots.LOG_OUTPUT_ROOT}/{user_photo_path}'+('.txt')

#             args = detectArgs()
#             args.input_image_path = f'{IMAGE_INPUT_PATH}'
#             args.output_image_path = f'{IMAGE_OUTPUT_PATH}'
#             args.weight_path = './weight/yolov5m6.pt'
#             args.output_warning_path = f'{WARNING_OUTPUT_PATH}'
#             args.output_log_path = f'{LOG_OUTPUT_PATH}'

#             detect(args)


def media_detect():
    print('Start Detecting Imgs')
    test_needed_user_list = os.listdir(f'{Roots.IMAGE_DOWNLOAD_ROOT}')
    test_needed_user_number = len(test_needed_user_list)

    # make_dir_save_imgs 함수를 통해 insta_imgs 폴더 속에 사용자의 Pk로 된 폴더를 생성한 후 
    # make_directory_save_images(user_output_path)
    
    
    for i in tqdm(range(0, test_needed_user_number)):
        print("== User Number : %d ==" % i)
        # Ouput Imgs/Warning/Log 위한 Directory 생성 함수 make_...
        save_imgs_OUTPUT(test_needed_user_list[i])
        save_warning(test_needed_user_list[i])
        save_log(test_needed_user_list[i])

        test_needed_photo_list = os.listdir(f'{Roots.IMAGE_DOWNLOAD_ROOT}/{test_needed_user_list[i]}')
        test_needed_photo_number = len(test_needed_photo_list)

        for j in tqdm(range(0, test_needed_photo_number)):
            print("== Photo Number : %d ==" % j)
            user_photo_path = f'{test_needed_user_list[i]}/{test_needed_photo_list[j]}'
            IMAGE_INPUT_PATH = f'{Roots.IMAGE_DOWNLOAD_ROOT}/{user_photo_path}'
            IMAGE_OUTPUT_PATH = f'{Roots.IMAGE_OUTPUT_ROOT}/{user_photo_path}'
            WARNING_OUTPUT_PATH = f'{Roots.WARNING_OUTPUT_ROOT}/{user_photo_path}'+('.txt')
            LOG_OUTPUT_PATH = f'{Roots.LOG_OUTPUT_ROOT}/{user_photo_path}'+('.txt')

            args = detectArgs()
            args.input_image_path = f'{IMAGE_INPUT_PATH}'
            args.output_image_path = f'{IMAGE_OUTPUT_PATH}'
            args.weight_path = './weight/yolov5m6.pt'
            args.output_warning_path = f'{WARNING_OUTPUT_PATH}'
            args.output_log_path = f'{LOG_OUTPUT_PATH}'
            
            print(args)
            attemp_download_weight(args)
            detect(args)

# media_detect()

# test_detect_images()