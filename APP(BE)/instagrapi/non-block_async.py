import asyncio
from datetime import datetime

async def wash(cloth):
    # cloth type에 따른 wash(세탁) 시간
    cloth_type = {'a' : 2, 'b': 3,  'c': 4}
    return_clothes = []
    execute_time = 0

    # cloth_type에 정의되지 않은 옷일 경우 -> wash time = 5초
    if cloth_type.get(cloth, None) == None:
        wash_time = 5
    else:
        wash_time = cloth_type[cloth]

    while True:
        print(f'Washing cloth {cloth} ... {wash_time - execute_time} time left.')
        # 1초를 await를 이용하여 기다려준다.
        await asyncio.sleep(1)
        # 세탁을 돌리고 있는 시간 = execute_time은 1초 씩 증가
        execute_time += 1
        # 만약 세탁시간을 다 채우면 break
        if execute_time >= wash_time:
            break
    # 이후 dry를 해야 하기에 dry function await (끝날때까지 대기)
    await dry("wash_" + cloth)


async def dry(cloth):
    # dry 시간은 2초 소요
    await asyncio.sleep(2)
    print(f'Dry cloth {cloth} ... complete.')
            
# 청소기/Cleaner 함수 - 위 wash+dry와 별개 형태의 프로세스
async def cleaner(room_nums):
    for room_idx in range(room_nums):
        # 각 방을 Clean 하는데는 1초 소요
        await asyncio.sleep(1)
        print(f'Clean room idx {room_idx} ... complete.')

# main 함수 -> 실행 함수이다.
async def main():
    clothes = ['a', 'b', 'c', 'd']
    room_nums = 10

    st = datetime.now()
    print(f"started at {st}")

    # 해야 할 일 들 = tasks
    tasks = []
    
    # 옷들은 wash -> dry 프로세스
    for cloth in clothes:
        # tasks list에 asyncio를 통해 생성한 task들을 append
        tasks.append(asyncio.create_task(
            wash(cloth)))

    # 방들은 cleaner 프로세스
    # tasks list에 asyncio를 통해 생성한 task들을 append
    tasks.append(asyncio.create_task(
        cleaner(room_nums))) #이 경우 cleaner함수에 room_nums 인자를 넣고 실행


    for tmp_task in tasks:
        # tasks 리스트를 for 문을 통해 각 task가 끝나면 다음 tmp_task로 넘어감(await 이용하여)
        await tmp_task

    et = datetime.now()
    print(f"finished at {et}")
    print(f"time for task: {et-st}")

if __name__ == "__main__":
    asyncio.run(main())