from instagrapi import Client
from instagrapi.types import Location, StoryMention, StoryLocation, StoryLink, StoryHashtag
from tqdm import tqdm
import datetime
import json
import os

CHECK_PER_INTERVAL = 100
IMAGE_DOWNLOAD_ROOT = '/workspaces/AI_APP_WEB_Canary_Canary/SERVER/instagrapi/directMessage/images'
LAST_CHECK_TIME = datetime.datetime(2021, 10, 6, 13, 7, 50, 823287, tzinfo=datetime.timezone.utc) # Interval마다 변경될 예정

def get_logined_client(cl, instagramID, instagramPW):
    try:
        cl.account_info()
    except:
        cl.login(instagramID,instagramPW)

# Thread : 채팅방
# Message : 채팅

def list_unread_thread(cl):
    unread_thread_list = cl.direct_threads(CHECK_PER_INTERVAL, 'unread')
    return unread_thread_list
    pass

def get_unread_message_list_from_thread(thread):
    total_messages_number = len(thread.messages)
    for i in range(0, total_messages_number):
        if thread.messages[i].timestamp <= LAST_CHECK_TIME:
            break
    return thread.messages[0 : i+1]

def get_media_type_of_message(message):
    # In case of text
    if message.media == None:
        return -1
    else:
        return message.media.media_type

def make_directory_save_images(message):
    path = f'{IMAGE_DOWNLOAD_ROOT}/{message.user_id}'
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except OSError:
        print("Error : Creating directory " + path)
    return path

def get_image_from_message(message, cl):
    # Media Type {Photo : 1}
    if get_media_type_of_message(message) == 1:
        print("Media Type : Photo. Downloading...")
        download_path = make_directory_save_images(message)
        cl.photo_download(message.media.id, download_path)
    else:
        print("No Unread Images. Pass...")

def download_image_for_detect(cl):
    unread_thread_list = list_unread_thread(cl)
    for i in range(len(unread_thread_list)):
        print("==Thread Number : %d =="  % i)
        unread_messages_list = get_unread_message_list_from_thread(unread_thread_list[i])
        for j in range(len(unread_messages_list)):
            print("==Message Number : %d ==" % j)
            get_image_from_message(unread_messages_list[j], cl)
    
def main():
    # Instagram Client Login
    with open('/workspaces/AI_APP_WEB_Canary_Canary/SERVER/instagrapi/directMessage/instagram_config.json') as json_file:
        instagram_config = json.load(json_file)
    id = instagram_config['id']
    password = instagram_config['password']

    cl = Client()
    get_logined_client(cl, id, password)

    # TODO : Unread한 DM에서 사진 경로 받기
    download_image_for_detect(cl)

# main()
