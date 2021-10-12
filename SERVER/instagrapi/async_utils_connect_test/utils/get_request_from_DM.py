from argparse import *
from instagrapi import *
from parse import *

IMAGE_DOWNLOAD_ROOT = '/workspaces/AI_APP_WEB_Canary_Canary/SERVER/instagrapi/async_utils_connect_test/images'
IMAGE_OUTPUT_ROOT = '/workspaces/AI_APP_WEB_Canary_Canary/SERVER/instagrapi/async_utils_connect_test/images_detect_output'
WARNING_OUTPUT_ROOT = '/workspaces/AI_APP_WEB_Canary_Canary/SERVER/instagrapi/async_utils_connect_test/warning'

async_img_download_root = '/workspaces/AI_APP_WEB_Canary_Canary/SERVER/instagrapi/async_utils_connect_test/insta_imgs'

# For debug
'''
cl = Client()
cl.login('osam_canary', 'admin0408')
'''

def get_media_type_of_message(message):
    # In case of text
    if message.media == None:
        return -1
    else:
        return message.media.media_type

def make_directory_save_images(message):
    path = f'{IMAGE_DOWNLOAD_ROOT}/{message.user_id}'
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except OSError:
        print("Error : Creating directory " + path)
    return path

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
    
    if target_type == 1:
        cl.photo_download(target_pk,async_img_download_root)
    elif target_type == 8:
        cl.album_download(target_pk,async_img_download_root)
    else:
        cl.direct_send('지원하지 않는 형식의 게시물입니다. 현재는 사진과 앨범 게시물들만 검사 가능합니다')

async def read_all_posts(cl,user_id):
    # osam_testbot.user_id = 50160424289
    # user의 posts를 list로 저장 : user_posts
    raw_user_posts = cl.user_medias(user_id) # default amount = 20

    print(raw_user_posts)

    # cl.media_likers(post_id) -> Post를 좋아요한 유저 리스트
    raw_posts_len = len(raw_user_posts)
    print(f'raw_post_len : {raw_posts_len}')

    user_posts = [] # 검사할 Posts 대상들의 리스트 
    
    # 검사 대상을 3개의 Post로 한정 짓는다.
    j = 0
    for idx in range(raw_posts_len):
        post_id = raw_user_posts[idx].id
        print(post_id)
        post_likers = cl.media_likers(post_id)
        for n in range(len(post_likers)):
            if post_likers[n].pk == 49617754574: # 해당 pk 는 'osam_canary'의 PK
                break
            else:
                user_posts.append(raw_user_posts[idx])
                j += 1
        if j >= 3:
            break
    
    print(user_posts)
    posts_len = len(user_posts)

    for idx in range(posts_len):
        post_pk = user_posts[idx].pk
        post_type = user_posts[idx].media_type
        post_id = user_posts[idx].id # post_pk + '_' + user_id = post_id
        if post_type == 1:
            cl.media_like(post_id) # 사진에 좋아요를 남김으로써 검사 완료 표시
            cl.photo_download(post_pk,async_img_download_root)
        elif post_type == 8:
            cl.media_like(post_id)
            cl.album_download(post_pk,async_img_download_root)
        else:
            cl.media_like(post_id)
            print('사진의 media type이 아닙니다')

    print('3 Posts reading process done')

######

def send_invalid_bound(thread):
    cl.direct_send(thread_ids = [thread.id], text = "Invalid bound! If you need help, please send me '/help'")

def download_DM(thread):
    download_path = make_directory_save_images(thread.messages[0])
    cl.photo_download(thread.messages[0].media.id, download_path)

def download_feed(thread, photo_number):
    if str(type(photo_number)) != 'int':
        send_invalid(thread)
    else:
        target_media_pk = cl.user_medias(thread.messages[0].user_id, photo_number)[photo_number-1].pk
        if target_media_pk == None:
            send_invalid_bound(thread)
        else:
            cl.photo_download(target_media_pk, download_path)

def download_story(thread, story_number):
    if str(type(story_number)) != 'int':
        send_invalid(thread)
    else:
        target_story_pk = cl.user_storys(thread.messages[0].user_id, story_number)[story_number-1].pk
        if target_story_pk == None:
            send_invalid_bound(thread)
        else:
            cl.story_download(target_story_pk, download_path)

def get_request_from_DM(thread):
    most_recent_message = thread.messages[0]
    check_help = parse('/{}', most_recent_message.text)[0]
    detection_mode = parse('/{} {}', most_recent_message.text)[0]

    if get_media_type_of_message(most_recent_message) == -1:  # Check 'text'
        if check_help == 'help':
            send_help(thread)
        else:
            if detection_mode[0] == 'feed':
                download_feed(thread, detection_mode[1])
            elif detection_mode[0] == 'story':
                download_story(thread, detection_mode[1])
            else:
                send_invalid(thread)
    elif get_media_type_of_message(most_recent_message) == 1:   # Photo
        download_DM(thread)
    else:       # default case
        send_invalid(thread)