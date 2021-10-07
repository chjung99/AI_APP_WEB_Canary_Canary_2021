from instagrapi import Client
from instagrapi.types import Location, StoryMention, StoryLocation, StoryLink, StoryHashtag
import datetime

id = 'osam_canary'
password = 'admin0408'

CHECK_PER_INTERVAL = 100
LAST_CHECK_TIME = datetime.datetime(2021, 10, 6, 13, 7, 50, 823287, tzinfo=datetime.timezone.utc)

def getLoginedClient(instagramID, instagramPW):
    cl = Client()
    cl.login(instagramID,instagramPW)
    return cl

# Thread : 채팅방
# DM : 채팅

def listUnreadThread(client):
    cl = client
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

def getImageFromMessage(message):
    if getItemTypeOfMessage(message) == 'image':
        print("Success")
    else:
        print("Success22")
        
def main():
    cl = getLoginedClient(id, password)

    unreadThreadList = listUnreadThread(cl)
    for i in range(len(unreadThreadList)):
        unreadMessagesList = getUnreadMessageListFromThread(unreadThreadList[i])
        for j in range(len(unreadMessagesList)):
            image = getImageFromMessage(unreadMessagesList[j])

main()
    

# TODO : Unread한 DM에서 사진 경로 받기

# TODO : image를 download 한 후, Canary_YOLOv5 에서 detect.py 돌리기

# TODO : detect 된 결과를 DM으로 보내주기
