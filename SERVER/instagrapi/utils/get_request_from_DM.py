from argparse import *
from instagrapi import *
from parse import *
from get_client import *

# For debug
'''
cl = Client()
get_logined_cliendt(cl, 'osam_canary', 'admin0408')
'''

def get_media_type_of_message(message):
    # In case of text
    if message.media == None:
        return -1
    else:
        return message.media.media_type

def print_help():
    print("==== How to use ====\n1. DM detection\nPlease send me '/detect DM'\nThen, send me one photo")
    print("2. Feed detection\nPlease send me '/detect feed'\nThen, send me a number 'n' of feed. (Most recent feed number is 0)")
    print("3. Story detection\nPlease send me '/detect story'\nThen, send me a name of story.")

def print_invalid():
    print("Invalid execution! If you need help, please send me '/help'")

def detect_DM(message):
    print("Please send me a photo")

def detect_feed(message):
    print("Please send me a feed number as n:m. (Most recent feed number is 0)")

def detect_story(message):
    print("Please send me a story name")

def get_request_from_DM(message):
    if get_media_type_of_message(message) == -1:  # Check 'text'
        detection_mode = parse('/{}', message.text)
        if detection_mode == None:
            print_help()
        else:
            if detection_mode[0] == 'help':
                print_help()
            elif detection_mode[0] == 'DM':
                detect_DM(message)
            elif detection_mode[0] == 'feed':
                detect_feed(message)
            elif detection_mode[0] == 'story':
                detect_story(message)
            else:
                print_invalid()
    else:
        print_help()

# For debug

class message:
    media = None
    text = ''

msg = message()
msg.text = input("In : ")
get_request_from_DM(msg)