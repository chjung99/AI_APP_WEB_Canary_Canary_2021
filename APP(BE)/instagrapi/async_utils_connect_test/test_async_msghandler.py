import asyncio

from instagrapi import Client

# from utils.get_client import *
# from utils.download_image_from_DM import *
# from utils.detect_images import *
# from utils.send_DM import *

import sys
from os import path

# from utils.detect_images import *
from utils import get_request_from_DM, send_DM, get_client
from utils import detect_images

cl = Client()
get_client.get_logined_client(cl)

messages = [] 

async def check_unread(messages):
    while True: 
        await asyncio.sleep(1) # 1초 interval로 Thread 읽어옴
        unread_threads = cl.direct_threads(20,'unread')
        unread_len = len(unread_threads)
        print(f'unread msgs remaining : {unread_len}')
        if unread_len > 0:
            for idx in range(unread_len):
                msg = unread_threads[idx].messages[0].text
                user_id = unread_threads[idx].messages[0].user_id # 메세지 전송한 user의 id 추출
                thread_id = unread_threads[idx].id # thread ID 추출
                cl.direct_answer(thread_id,'메세지 처리 중 입니다')
                print(msg) # 사용자의 msg 출력
                messages.append((msg,user_id,thread_id)) # messages list에 msg와 thread_id 를 추가

# messages를 읽어온 후 가장 최신의 msg부터 각자 handling 한다.(concurrently라는 가정 하)
async def msg_handler(messages):
    while True:
        if messages:
            print(messages)
            print('Msg READ')
            # 읽은 msgs는 삭제 처리
            msg_data = messages.pop(0)

            msg = msg_data[0]
            user_id = msg_data[1]
            thread_id = msg_data[2]

            print(f'input message : {msg_data}')
            
            if msg == 'Test':
                print('Test Route')
                await test_img_process(msg)
            elif msg == '도움':
                print('Help Route')
                # thread_id = msg_data[1] # Thread_id 의 idx : 1
                await get_request_from_DM.send_help(cl,user_id) # cl = Client Pass
            elif msg == '게시물 3개 검사':
                print('Post Check Route')
                # 사용자 게시물 다운로드
                await get_request_from_DM.get_recent_three_unchecked_medias(cl,user_id)
                # 이후 detect.py 파일 구동(현재 media_detect()는 insta_imgs 파일 내 모든 파일 검사)
                await detect_images.media_detect(user_id)
                await send_DM.send_DM(cl)
            
            elif msg == '스토리 3개 검사':
                print('Story Check Route')
                await get_request_from_DM.get_recent_three_stories(cl,user_id)
                await detect_images.media_detect(user_id)
                await send_DM.send_DM(cl)

            elif msg == '게시물 검사':
                await get_request_from_DM.post_check(cl,user_id,thread_id)
            else:
                print('Invalid Command Route')
                await get_request_from_DM.send_invalid(cl,user_id)
                
        else:
            print('no messages left')
            await asyncio.sleep(1)

async def test_img_process(msg):
    await asyncio.sleep(3) # img processing 예상 소요시간 임의 설정
    print(f'{msg} : img_processing done')

# main 실행 함수
async def main(messages) :
    await asyncio.gather(
        check_unread(messages),
        msg_handler(messages), # 하나의 함수당 Thread 1로 작동하는 개념 (동시에 하나의 명령씩 수행 가능)
        msg_handler(messages),
        msg_handler(messages),
    )
    
if __name__ == "__main__":
    asyncio.run(main(messages))

# print(f"stated at {time.strftime('%X')}")
# asyncio.run(main(messages))
# print(f"finish at {time.strftime('%X')}")
