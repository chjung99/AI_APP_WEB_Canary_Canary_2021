import time
import asyncio
import os
from multiprocessing import Process

from instagrapi import Client

# from utils.get_client import *
# from utils.download_image_from_DM import *
# from utils.detect_images import *
# from utils.send_DM import *
from utils.get_request_from_DM import * # local Utils function import


cl = Client()
cl.login('osam_canary','admin0408!')
# cl.login('osam_testbot','admin0408')
# cl.login('osam_canary1','admin0408')
msg_wait_list = [] #전체 처리해야 될 메세지
Processes = [] #처리해야 할 process 리스트

class Message():

    def __init__(self):
        pass

    async def check_unread(self): # global msg_wait_list를 pass
        while True: 
            global msg_wait_list
            await asyncio.sleep(1) # 1초 interval로 Thread 읽어옴
            unread_threads = cl.direct_threads(20,'unread')
            unread_len = len(unread_threads)
            print(f'unread msgs remaining : {unread_len}')
            if unread_len > 0:
                for idx in range(unread_len):
                    msg = unread_threads[idx].messages[0].text
                    user_id = unread_threads[idx].messages[0].user_id # 메세지 전송한 user의 id 추출
                    thread_id = unread_threads[idx].id # thread ID 추출
                    cl.direct_answer(thread_id,'msg received')
                    print(f'사용자의 입력 : {msg}') # 사용자의 msg 출력
                    msg_wait_list.append((msg,user_id,thread_id)) # msg_wait_list에 msg와 thread_id 를 추가
            

    async def msg_handler(self):
        while True:
            global msg_wait_list
            if msg_wait_list:
                print(msg_wait_list)
                print('Msg READ')
                # 읽은 msgs는 삭제 처리
                msg_data = msg_wait_list.pop(0)

                msg = msg_data[0]
                user_id = msg_data[1]
                thread_id = msg_data[2]

                print(f'input message to HANDLE : {msg_data}')
                
                if msg == 'Test':
                    print('Test Route')
                elif msg == '도움':
                    print('Help Route')
                    # thread_id = msg_data[1] # Thread_id 의 idx : 1
                    await send_help(cl,user_id) # cl = Client Pass
                elif msg == '게시물 3개 검사':
                    print('Post Check Route')
                    await get_recent_three_unchecked_medias(cl,user_id)
                elif msg == '게시물 검사':
                    await post_check(cl,user_id,thread_id)
                else:
                    print('Invalid Command Route')
                    await send_invalid(cl,user_id)
                    

            else:
                print('no messages left')
                await asyncio.sleep(1)


    def read_process(self):
        asyncio.run(self.check_unread())
    
    def handle_process(self):
        asyncio.run(self.msg_handler())

#### 

# messages를 읽어온 후 가장 최신의 msg부터 각자 handling 한다.(concurrently라는 가정 하)

# async def msg_handler(msg_wait_list):
#     while True:
#         if msg_wait_list:
#             print(msg_wait_list)
#             print('Msg READ')
#             # 읽은 msgs는 삭제 처리
#             msg_data = msg_wait_list.pop(0)

#             msg = msg_data[0]
#             user_id = msg_data[1]
#             thread_id = msg_data[2]

#             print(f'input message : {msg_data}')
            
#             if msg == 'Test':
#                 print('Test Route')
#             elif msg == '도움':
#                 print('Help Route')
#                 # thread_id = msg_data[1] # Thread_id 의 idx : 1
#                 await send_help(cl,user_id) # cl = Client Pass
#             elif msg == '게시물 3개 검사':
#                 print('Post Check Route')
#                 await get_recent_three_unchecked_medias(cl,user_id)
#             elif msg == '게시물 검사':
#                 await post_check(cl,user_id,thread_id)
#             else:
#                 print('Invalid Command Route')
#                 await send_invalid(cl,user_id)
                

#         else:
#             print('no messages left')
#             await asyncio.sleep(1)


def sync_func():
    while True:
        print('This is SYNC_FUNC')
        time.sleep(3)
        print('Sleep Done')
    
if __name__ == "__main__":
    # async function들은 Class 이용해서 process activate
    # msg 읽어오기
    read_msg = Process(target=Message().read_process)
    read_msg.start()
    Processes.append(read_msg)

    #msg handling
    handle_msg = Process(target=Message().handle_process)
    handle_msg.start()
    Processes.append(handle_msg)

    for p in Processes:
        p.join()
        print(msg_wait_list)
    
    # # Test1
    # while True:
    #     read_msg = Process(target=Message().read_process)
    #     read_msg.start()
    #     Processes.append(read_msg)

    #     #msg handling
    #     handle_msg = Process(target=Message().handle_process)
    #     handle_msg.start()
    #     Processes.append(handle_msg)

    #     for p in Processes:
    #         p.join()