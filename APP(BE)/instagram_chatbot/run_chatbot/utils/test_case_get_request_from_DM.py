from instagrapi import *

cl = Client()
cl.login('osam_canary', 'admin0408!')

'''
async def read_all_posts(cl,user_id):
    # test user_id = 50160424289
    # user의 posts를 list로 저장 : user_posts
    user_posts = cl.user_medias_v1(user_id)
    posts_len = len(user_posts)
    for idx in range(posts_len):
        post_pk = user_posts[idx].pk
        post_type = user_posts[idx].media_type
        if post_type == 1:
            cl.photo_download(post_pk,async_img_download_root)
        elif post_type == 8:
            cl.album_download(post_pk,async_img_download_root)
        else:
            print('사진의 media type이 아닙니다')
    print('reading process done')
'''

def read_all_photos_from_medias(cl, user_id):
    media_len = cl.user_info(user_id).media_count
    print(media_len)
    media_list = cl.user_medias(user_id, media_len)
    print(media_list)
    for i in range(media_len):
        print(media_list[i].media_type)
        if media_list[i].media_type == 1:
            cl.photo_download(media_list[i].pk, folder = './')
        elif media_list[i].media_type == 8:
            cl.album_download(media_list[i].pk, folder = './')

def test_read_all_post(cl):
    user_id = 50160424289
    read_all_photos_from_medias(cl, user_id)

test_read_all_post(cl)
