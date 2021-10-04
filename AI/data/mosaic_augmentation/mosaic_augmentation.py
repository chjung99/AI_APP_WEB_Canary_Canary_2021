from genericpath import exists
import os
#import cv2
import tqdm

def getImageRoot():
    dataRoot = input('Input the root directory of YOLO train image (You SHOULD have images and label folder) : ')
    if(os.path.exists(f'{dataRoot}/images') & os.path.exists(f'{dataRoot}/labels')):
        print('Image Route Setup compilt')
        return dataRoot
    else:
        print('Invalid image route')
        exit()

def getTooLargeLabelImage(dataRoot):
    imageDirectory = '{dataRoot}/images'
    labelDirectory = '{dataRoot}/labels'

    dataLen = len(os.listdir(imageDirectory))
    # TODO : If label is too big compare to image size, collect the name of image and return as list

    for i in range(dataLen):
        img = cv2.imwrite(imageDirectory/)


def doMosaicWith4Images(dataRoot):
    # TODO : Resize Image and Label
    print('aa')

def main():
    dataRoot = getImageRoot()
    getTooLargeLabelImage(dataRoot)

if __name__ == '__main__':
    main()