from instagrapi import Client
from instagrapi.types import Location, StoryMention, StoryLocation, StoryLink, StoryHashtag
from tqdm import tqdm
import datetime
import json
import os
from utils.get_client import *
from utils.image_path import *

CHECK_PER_INTERVAL = 100
last_check_time = datetime.datetime(2021, 10, 6, 13, 7, 50, 823287, tzinfo=datetime.timezone.utc) # initial value. 함수가 호출 될 때마다 변경 

'''
# used in case of debug
cl = Client()
get_logined_client(cl, id, password)
'''

# Thread : 채팅방
# Message : 채팅

def list_unread_thread(cl):
    unread_thread_list = cl.direct_threads(CHECK_PER_INTERVAL, 'unread')
    return unread_thread_list
    pass

def get_unread_message_list_from_thread(thread):
    total_messages_number = len(thread.messages)
    last_check_time = datetime.datetime.now()
    for i in range(0, total_messages_number):
        if thread.messages[i].timestamp <= last_check_time:
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

def download_imaged_from_DM(cl):
    unread_thread_list = list_unread_thread(cl)
    for i in range(len(unread_thread_list)):
        print("==Thread Number : %d =="  % i)
        unread_messages_list = get_unread_message_list_from_thread(unread_thread_list[i])
        for j in range(len(unread_messages_list)):
            print("==Message Number : %d ==" % j)
            get_image_from_message(unread_messages_list[j], cl)
    
# download_imaged_from_DM(cl)