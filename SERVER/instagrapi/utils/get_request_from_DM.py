from argparse import *
from instagrapi import *
from parse import *

IMAGE_DOWNLOAD_ROOT = '/workspaces/AI_APP_WEB_Canary_Canary/SERVER/instagrapi/images'
IMAGE_OUTPUT_ROOT = '/workspaces/AI_APP_WEB_Canary_Canary/SERVER/instagrapi/images_detect_output'
WARNING_OUTPUT_ROOT = '/workspaces/AI_APP_WEB_Canary_Canary/SERVER/instagrapi/warning'

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

def send_help(thread):
    cl.direct_send(thread_ids = [thread.id], text = "==== How to use ====\n1. DM detection\nPlease send me one photo")
    cl.direct_send(thread_ids = [thread.id], text = "2. Feed detection\nPlease send me '/feed n'\n(Most recent feed number is 1)")
    cl.direct_send(thread_ids = [thread.id], text = "3. Story detection\nPlease send me '/story n'\n(Most recent story number is 1)")

def send_invalid(thread):
    cl.direct_send(thread_ids = [thread.id], text = "Invalid execution! If you need help, please send me '/help'")

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