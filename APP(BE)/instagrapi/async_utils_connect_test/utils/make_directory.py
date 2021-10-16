import sys
import os

class Roots:
    SYS_PATH_ROOT = '/workspaces/AI_APP_WEB_Canary_Canary'
    IMAGE_DOWNLOAD_ROOT = '/workspaces/AI_APP_WEB_Canary_Canary/SERVER/instagrapi/async_utils_connect_test/insta_imgs'
    IMAGE_OUTPUT_ROOT = '/workspaces/AI_APP_WEB_Canary_Canary/SERVER/instagrapi/async_utils_connect_test/insta_imgs_detected'
    WARNING_OUTPUT_ROOT = '/workspaces/AI_APP_WEB_Canary_Canary/SERVER/instagrapi/async_utils_connect_test/insta_imgs_warnings'
    LOG_OUTPUT_ROOT = '/workspaces/AI_APP_WEB_Canary_Canary/SERVER/instagrapi/async_utils_connect_test/log'


def save_imgs_INPUT(user_input_path):
    path = f'{Roots.IMAGE_DOWNLOAD_ROOT}/{user_input_path}'
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except OSError: 
        print("Error : Creating directory " + path)
    return path


def save_imgs_OUTPUT(user_output_path):
    path = f'{Roots.IMAGE_OUTPUT_ROOT}/{user_output_path}'
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except OSError: 
        print("Error : Creating directory " + path)
    return path

def save_warning(user_output_path):
    path = f'{Roots.WARNING_OUTPUT_ROOT}/{user_output_path}'
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except OSError:
        print("Error : Creating directory " + path)
    return path

def save_log(user_output_path):
    path = f'{Roots.LOG_OUTPUT_ROOT}/{user_output_path}'
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except OSError:
        print("Error : Creating directory " + path)
    return path