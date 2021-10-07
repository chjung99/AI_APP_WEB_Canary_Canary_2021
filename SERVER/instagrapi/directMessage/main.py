from instagrapi import Client
from instagrapi.types import Location, StoryMention, StoryLocation, StoryLink, StoryHashtag
import datetime
import json

id = 'osam_canary'
password = 'admin0408'

CHECK_PER_INTERVAL = 100
IMAGE_DOWNLOAD_PATH = './images'
LAST_CHECK_TIME = datetime.datetime(2021, 10, 6, 13, 7, 50, 823287, tzinfo=datetime.timezone.utc) # Interval마다 변경될 예정

def getLoginedClient(instagramID, instagramPW):
    cl = Client()
    cl.login(instagramID,instagramPW)
    return cl

# Thread : 채팅방
# Message : 채팅

def listUnreadThread(cl):
    unreadThreadList = cl.direct_threads(CHECK_PER_INTERVAL, 'unread')
    return unreadThreadList

def getUnreadMessageListFromThread(thread):
    totalMessages = len(thread.messages)
    for i in range(totalMessages):
        if thread.messages[i].timestamp <= LAST_CHECK_TIME:
            break
    return thread.messages[0 : i-1]

def getItemTypeOfMessage(message):
    return message.item_type

def getImageFromMessage(message, cl):
    if getItemTypeOfMessage(message) == 'image':
        cl.photo_download(message.media.id, IMAGE_DOWNLOAD_PATH)
    else:
        print("Not Image... Pass")

def downloadImageForDetect(cl):
    unreadThreadList = listUnreadThread(cl)

    for i in range(len(unreadThreadList)):
        unreadMessagesList = getUnreadMessageListFromThread(unreadThreadList[i])
        for j in range(len(unreadMessagesList)):
            getImageFromMessage(unreadMessagesList[j], cl)
        
def main():
    # Instagram Client Login
    with open('./instagram_config.json') as json_file:
        instagram_config = json.load(json_file)
    id = instagram_config['id']
    password = instagram_config['password']

    cl = getLoginedClient(id, password)

    # TODO : Unread한 DM에서 사진 경로 받기
    downloadImageForDetect(cl)

    # TODO : image를 download 한 후, Canary_YOLOv5 에서 detect.py 돌리기
    # 처리 완료 했으면 이미지 삭제하기

    # TODO : detect 된 결과를 DM으로 보내주기

main()