import asyncio
from datetime import datetime
from instagrapi import Client
from apscheduler.schedulers.blocking import BlockingScheduler

cl = Client()
cl.login('osam_canary','admin0408')
tasks = []

async def check_unread():
    unread_threads = cl.direct_threads(20,'unread')
    unread_len = len(unread_threads)
    print(f'unread msgs remaining : {unread_len}')
    for idx in range(unread_len):
        msg = unread_threads[idx].messages[0].text # 해당 Thread의 최신 message = messages[0]
        tasks.append(asyncio.create_task(msg_handler(msg)))

    # if unread_threads > 0:
    #     return True
    # else:
    #     return False

async def msg_handler(msg):
    if msg == '테스트':
        print('Instagrapi Testing 성공')
    else :
        print('지원 하지 않은 명령어입니다')
    

# main 함수 -> 실행 함수이다.
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