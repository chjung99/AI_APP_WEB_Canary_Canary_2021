# TODO : detect 된 결과를 DM으로 보내주기
from instagrapi import *
import os
from tqdm import tqdm
import json

from image_path import Roots
from get_client import *

# used in case of debug
'''
cl = Client()
get_logined_client(cl)
'''

def get_waiting_user_list():
    return os.listdir(Roots.IMAGE_OUTPUT_ROOT)

def get_waiting_DM_list(user_id):
    return os.listdir(f'{Roots.IMAGE_OUTPUT_ROOT}/{user_id}')

def get_waiting_warning_list(user_id):
    return os.listdir(f'{Roots.WARNING_OUTPUT_ROOT}/{user_id}')

def remove_all_file(file_path):
    if os.path.exists(file_path):
        for file in os.scandir(file_path):
            os.remove(file.path)
        return 'Remove All Files'
    else:
        return 'Directory Not Found'

def delete_detected_images(user_id):
    remove_all_file(f'{Roots.IMAGE_DOWNLOAD_ROOT}/{user_id}')
    os.rmdir(f'{Roots.IMAGE_DOWNLOAD_ROOT}/{user_id}')
    remove_all_file(f'{Roots.IMAGE_OUTPUT_ROOT}/{user_id}')
    os.rmdir(f'{Roots.IMAGE_OUTPUT_ROOT}/{user_id}')
    remove_all_file(f'{Roots.WARNING_OUTPUT_ROOT}/{user_id}')
    os.rmdir(f'{Roots.WARNING_OUTPUT_ROOT}/{user_id}')

async def send_DM(cl):    # Instagram Client Login
    waiting_user_list = get_waiting_user_list()
    waiting_user_list_length = len(waiting_user_list)

    for i in tqdm(range(0, waiting_user_list_length)):
        waiting_DM_list = get_waiting_DM_list(waiting_user_list[i])
        waiting_DM_list_length = len(waiting_DM_list)

        waiting_warning_list = get_waiting_warning_list(waiting_user_list[i])

        for j in tqdm(range(0, waiting_DM_list_length)):

            with open(f'{Roots.WARNING_OUTPUT_ROOT}/{waiting_user_list[i]}/{waiting_warning_list[j]}', 'r') as file:
                warning_txt = file.read()

            cl.direct_send_photo(f'{Roots.IMAGE_OUTPUT_ROOT}/{waiting_user_list[i]}/{waiting_DM_list[j]}', user_ids = [waiting_user_list[i]])
            cl.direct_send(warning_txt, user_ids = [waiting_user_list[i]])
            # user_ids : It should be list
        delete_detected_images(waiting_user_list[i])

# send_DM(cl)