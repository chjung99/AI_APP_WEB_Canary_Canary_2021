from argparse import *
from instagrapi import *
from parse import *

# sys.path.insert(0,'/workspaces/AI_APP_WEB_Canary_Canary/SERVER/instagrapi/async_utils_connect_test/utils/')
# from .image_path import Roots
# from .make_directory import *


import sys
from os import path
sys.path.append('/workspaces/AI_APP_WEB_Canary_Canary/APP(BE)/instagrapi/async_utils_connect_test/utils')
from make_directory import * # make_directory 함수들 import
from image_path import Roots

async_img_download_root = Roots.IMAGE_DOWNLOAD_ROOT 

def get_media_type_of_message(message):
    # In case of text
    if message.media == None:
        return -1
    else:
        return message.media.media_type

# async로 형식 전환중
async def send_help(cl,user_id):
    # Thread_id로도 DM 전송 가능하지만 user_id의 범용성이 더 높기에 user_id 채택
    # cl.direct_answer(thread_id,'=== How To Use=== \n 1. 포스트 검사하기 : 명령어 \n 2. 스토리 검사하기')
    cl.direct_send('=== How To Use=== \n 1. 포스트 검사하기 : 명령어 \n 2. 스토리 검사하기', user_ids=[user_id])
    
# 지원하지 않은 명령어
async def send_invalid(cl,user_id):
    # cl.direct_answer(thread_id,"지원하지 않은 명령어 입니다. 도움말을 보시려면 '도움 또는 Help'를 전송해주세요")
    cl.direct_send("지원하지 않은 명령어 입니다. 도움말을 보시려면 '도움 또는 Help'를 전송해주세요", user_ids=[user_id])

async def post_check(cl,user_id,thread_id):
    cl.direct_send('게시물 순서를 입력해주세요. \n최근 게시물부터 1->2->3 입니다')
    post_num = cl.direct_messages(thread_id) # 해당 Thread의 메세지를 읽어온다 -> 가장 최근은 [0]
    user_posts = cl.user_medias(user_id) # cl.user_medias_v1(user_id) -> low level method
    request_post = user_posts[post_num] # 사용자가 검사를 요청한 게시물 : request_post
    target_pk = request_post.pk
    target_type = request_post.media_type
    user_pk = cl.user_info(user_id).pk
    
    if target_type == 1:
        cl.photo_download(target_pk,f'{async_img_download_root}/{user_pk}')
    elif target_type == 8:
        cl.album_download(target_pk,f'{async_img_download_root}/{user_pk}')
    else:
        cl.direct_send('지원하지 않는 형식의 게시물입니다. 현재는 사진과 앨범 게시물들만 검사 가능합니다')

##### 
def get_pk_from_user(users):
    return users.pk

async def get_recent_three_unchecked_medias(cl,user_id):
    # osam_testbot.user_id = 50160424289
    # user의 posts를 list로 저장 : user_posts_for_test
    MY_PK = 49617754574 

    raw_medias_len = cl.user_info(user_id).media_count   # total media length
    print(f'raw_medias_len : {raw_medias_len}')

    raw_user_medias = cl.user_medias(user_id, raw_medias_len) # default amount = 20
    # print(raw_user_medias)

    user_medias_for_test = [] # 검사할 Posts 대상들의 리스트 
    
    # 검사 대상을 3개의 Post로 한정 짓는다.
    count_three = 0
    for idx in range(0,raw_medias_len):
        print(idx)
        test_target_media_id = raw_user_medias[idx].id
        print(f'test_target_media_id : {test_target_media_id}')

        media_likers_list = cl.media_likers(test_target_media_id)
        # print(f'media_likers_list : {media_likers_list}')

        _media_likers_pk_list = list(map(get_pk_from_user, media_likers_list)) 
        print(f'_media_likers_pk_list : {_media_likers_pk_list}')

        if not MY_PK in _media_likers_pk_list:     
            user_medias_for_test.append(raw_user_medias[idx])
            count_three += 1

        cl.media_like(test_target_media_id)

        if count_three >= 3:
            break
    
    print(f'user_medias_for_test : {user_medias_for_test}')
    
    await download_media(cl,user_medias_for_test,user_id)

    print('3 Posts Downloading process done')

#####

# Media(Album & Photo) Download Function
async def download_media(cl,medias,user_id):

    # User들의 사진을 저장할 directory 생성
    input_path = save_imgs_INPUT(user_id)
    print(input_path)

    medias_len = len(medias)
    for idx in range(medias_len):
        media_pk = medias[idx].pk
        media_type = medias[idx].media_type
        user_info = cl.media_user(media_pk)
        if media_type == 1:
            cl.photo_download(media_pk,f'{Roots.IMAGE_DOWNLOAD_ROOT}/{user_info.pk}')
        elif media_type == 8:
            cl.album_download(media_pk,f'{async_img_download_root}/{user_info.pk}')
        else:
            print(f'{idx} 미디어의 media type이 지원이 불가합니다')