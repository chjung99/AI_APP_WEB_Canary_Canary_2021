from instagrapi import *
from tqdm import tqdm
import datetime
import json
import os
import asyncio
from apscheduler.schedulers.blocking import BlockingScheduler

from utils.get_client import *
from utils.download_image_from_DM import *
from utils.detect_images import *
from utils.send_DM import *

TASK = []

cl = Client()
get_logined_client(cl, id, password)

def auto_progress(cl):
    download_imaged_from_DM(cl)
    detect_images()
    send_DM(cl)

async def main():

    sched = BlockingScheduler({'apscheduler.job_defaults.max_instances': 2})
    # sched = BlockingScheduler()
    # Schedule job_function to be called every two seconds
    # while True:
    sched.add_job(auto_progress(), 'interval', seconds=2, args=cl)
    sched.start()
    print('schedule started')
         # for each_task in tasks:

    #tasks = [] -> tasks list의 전역 함수 선언...?

if __name__ == "__main__":
    asyncio.run(main())