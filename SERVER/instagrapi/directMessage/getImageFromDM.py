from instagrapi import Client
from instagrapi.types import Location, StoryMention, StoryLocation, StoryLink, StoryHashtag

cl = Client()
cl.login('osam_canary','admin0408')

# TODO : Unread한 DM에서 사진 경로 받기
thread = cl.direct_messages(1)[0]    
print(thread.pk)

# TODO : image를 download 한 후, Canary_YOLOv5 에서 detect.py 돌리기

# TODO : detect 된 결과를 DM으로 보내주기
