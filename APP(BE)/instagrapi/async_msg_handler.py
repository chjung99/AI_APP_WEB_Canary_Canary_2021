import time
import asyncio
from instagrapi import Client
from utils import get_request_from_DM # local Utils function import

cl = Client()
cl.login('osam_canary','admin0408')
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
                thread_id = unread_threads[idx].id # thread ID 추출
                cl.direct_answer(thread_id,'msg received')
                print(msg) # 사용자의 msg 출력
                messages.append((msg,thread_id)) # messages list에 msg와 thread_id 를 추가

# messages를 읽어온 후 가장 최신의 msg부터 각자 handling 한다.(concurrently라는 가정 하)
async def msg_handler(messages):
    while True:
        if messages:
            print(messages)
            print('Msg READ')
            # 읽은 msgs는 삭제 처리
            msg_data = messages.pop(0)

            msg = msg_data[0]
            thread_id = msg_data[1]
            
            if msg_data[0] == 'Test':
                await img_process(msg)
            elif msg_data[0] == 'Help' or '도움':
                # thread_id = msg_data[1] # Thread_id 의 idx : 1
                await get_request_from_DM.send_help(thread_id)
            else:
                print('지원되지 않은 명령어 입니다')
            
        else:
            print('no messages left')
            await asyncio.sleep(1)

async def img_process(msg):
    await asyncio.sleep(3)
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
