import time
import asyncio
from instagrapi import Client

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
                messages.append(msg) # messages list에 msg를 추가

async def read_msg(messages):
    while True:
        if messages:
            print(messages)
            print('Msg READ')
            msg = messages.pop(0)
            if msg == 'Test':
                await img_process(msg)
            
        else:
            print('no messages left')
            await asyncio.sleep(1)

async def img_process(msg):
    await asyncio.sleep(3)
    print(f'{msg} : img_processing done')

async def main(messages) :
    await asyncio.gather(
        check_unread(messages),
        read_msg(messages), # 하나의 함수당 Thread 1로 작동하는 개념 (동시에 하나의 명령씩 수행 가능)
        read_msg(messages),
        read_msg(messages),
    )
    
if __name__ == "__main__":
    asyncio.run(main(messages))

# print(f"stated at {time.strftime('%X')}")
# asyncio.run(main(messages))
# print(f"finish at {time.strftime('%X')}")
