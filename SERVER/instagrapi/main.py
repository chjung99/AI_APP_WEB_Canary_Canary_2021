from instagrapi import *
from tqdm import tqdm
import datetime
import json
import os
import asyncio
from apscheduler.schedulers.blocking import BlockingScheduler

from directMessage.image_download_from_DM import *
from directMessage.detect_images import *
from directMessage.send_DM import *

CHECK_PER_INTERVAL = 100
LAST_CHECK_TIME = datetime.datetime(2021, 10, 6, 13, 7, 50, 823287, tzinfo=datetime.timezone.utc) # Interval마다 변경될 예정

TASK = []

IMAGE_DOWNLOAD_ROOT = '/workspaces/AI_APP_WEB_Canary_Canary/SERVER/instagrapi/directMessage/images'
IMAGE_OUTPUT_ROOT = '/workspaces/AI_APP_WEB_Canary_Canary/SERVER/instagrapi/directMessage/images_detect_output'
WARNING_OUTPUT_ROOT = '/workspaces/AI_APP_WEB_Canary_Canary/SERVER/instagrapi/directMessage/warning'

cl = Client()
with open('/workspaces/AI_APP_WEB_Canary_Canary/SERVER/instagrapi/directMessage/instagram_config.json') as json_file:
    instagram_config = json.load(json_file)
id = instagram_config['id']
password = instagram_config['password']

get_logined_client(cl, id, password)

