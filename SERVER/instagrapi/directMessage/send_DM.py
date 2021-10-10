# TODO : detect 된 결과를 DM으로 보내주기

from instagrapi import *
import os
from tqdm import tqdm
import json

IMAGE_DOWNLOAD_ROOT = '/workspaces/AI_APP_WEB_Canary_Canary/SERVER/instagrapi/directMessage/images'
IMAGE_OUTPUT_ROOT = '/workspaces/AI_APP_WEB_Canary_Canary/SERVER/instagrapi/directMessage/images_detect_output'
WARNING_OUTPUT_ROOT = '/workspaces/AI_APP_WEB_Canary_Canary/SERVER/instagrapi/directMessage/warning'

def get_logined_client(cl, instagramID, instagramPW):
    try:
        cl.account_info()
    except:
        cl.login(instagramID,instagramPW)

def get_waiting_user_list():
    return os.listdir(IMAGE_OUTPUT_ROOT)

def get_waiting_DM_list(user_id):
    return os.listdir(f'{IMAGE_OUTPUT_ROOT}/{user_id}')

def remove_all_file(file_path):
    if os.path.exists(file_path):
        for file in os.scandir(file_path):
            os.remove(file.path)
        return 'Remove All Files'
    else:
        return 'Directory Not Found'

def delete_detected_images(user_id):
    remove_all_file(f'{IMAGE_DOWNLOAD_ROOT}/{user_id}')
    remove_all_file(f'{IMAGE_OUTPUT_ROOT}/{user_id}')
    remove_all_file(f'{WARNING_OUTPUT_ROOT}/{user_id}')

def main():    # Instagram Client Login
    with open('/workspaces/AI_APP_WEB_Canary_Canary/SERVER/instagrapi/directMessage/instagram_config.json') as json_file:
        instagram_config = json.load(json_file)
    id = instagram_config['id']
    password = instagram_config['password']

    cl = Client()
    get_logined_client(cl, id, password)

    waiting_user_list = get_waiting_user_list()
    waiting_user_list_length = len(waiting_user_list)

    for i in tqdm(range(0, waiting_user_list_length)):
        waiting_DM_list = get_waiting_DM_list(waiting_user_list[i])
        waiting_DM_list_length = len(waiting_DM_list)
        for j in tqdm(range(0, waiting_DM_list_length)):
            cl.direct_send_photo(f'{IMAGE_OUTPUT_ROOT}/{waiting_user_list[i]}/{waiting_DM_list[j]}', user_ids = [waiting_user_list[i]])
            # user_ids : It should be list
        delete_detected_images(waiting_user_list[i])

# main()