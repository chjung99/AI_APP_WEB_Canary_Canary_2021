from instagrapi import Client
from instagrapi.types import Location, StoryMention, StoryLocation, StoryLink, StoryHashtag
import datetime
import json
import tqdm
import os
from AI.yolov5 import detect

CHECK_PER_INTERVAL = 100
IMAGE_DOWNLOAD_ROOT = './images'
LAST_CHECK_TIME = datetime.datetime(2021, 10, 6, 13, 7, 50, 823287, tzinfo=datetime.timezone.utc) # Interval마다 변경될 예정

if __name__ == '__main__':
	if __package__ is None:
		import sys
		from os import path
		print(path.dirname(path.dirname(path.dirname( path.dirname( path.abspath(__file__) ) )) ))
		sys.path.append(path.dirname(path.dirname(path.dirname( path.dirname( path.abspath(__file__) ) )) ))
		from AI.yolov5 import detect
	else:
		from ......AI.yolov5 import detect


def getLoginedClient(cl, instagramID, instagramPW):
    try:
        cl.account_info()
    except:
        cl.login(instagramID,instagramPW)

# Thread : 채팅방
# Message : 채팅

def listUnreadThread(cl):
    unreadThreadList = cl.direct_threads(CHECK_PER_INTERVAL, 'unread')
    return unreadThreadList
    pass

def getUnreadMessageListFromThread(thread):
    totalMessagesNumber = len(thread.messages)
    for i in range(0, totalMessagesNumber):
        if thread.messages[i].timestamp <= LAST_CHECK_TIME:
            break
    return thread.messages[0 : i+1]

def getMediaTypeOfMessage(message):
    # In case of text
    if message.media == None:
        return -1
    else:
        return message.media.media_type

def makeDirectorySaveImages(message):
    path = f'{IMAGE_DOWNLOAD_ROOT}/{message.user_id}'
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except OSError:
        print("Error : Creating directory " + path)
    return path

def getImageFromMessage(message, cl):
    # Media Type {Photo : 1}
    if getMediaTypeOfMessage(message) == 1:
        print("Media Type : Photo. Downloading...")
        downloadPath = makeDirectorySaveImages(message)
        cl.photo_download(message.media.id, downloadPath)
    else:
        print("No Unread Images. Pass...")

def downloadImageForDetect(cl):
    unreadThreadList = listUnreadThread(cl)
    for i in range(len(unreadThreadList)):
        print("==Thread Number : %d =="  % i)
        unreadMessagesList = getUnreadMessageListFromThread(unreadThreadList[i])
        for j in range(len(unreadMessagesList)):
            print("==Message Number : %d ==" % j)
            getImageFromMessage(unreadMessagesList[j], cl)
    
def main():
    # Instagram Client Login
    with open('./instagram_config.json') as json_file:
        instagram_config = json.load(json_file)
    id = instagram_config['id']
    password = instagram_config['password']

    cl = Client()
    getLoginedClient(cl, id, password)

    # TODO : Unread한 DM에서 사진 경로 받기
    downloadImageForDetect(cl)

# main()
