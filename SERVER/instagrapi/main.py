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

async def main():

    sched = BlockingScheduler({'apscheduler.job_defaults.max_instances': 2})
    # sched = BlockingScheduler()
    # Schedule job_function to be called every two seconds
    # while True:
    sched.add_job(check_unread, 'interval', seconds=2)
    sched.start()
    print('schedule started')
         # for each_task in tasks:

    #tasks = [] -> tasks list의 전역 함수 선언...?

if __name__ == "__main__":
    asyncio.run(main())