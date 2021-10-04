from genericpath import exists
import os
import cv2
import tqdm

def setUpImageRoute():
    dataRoot = input('Input the root directory of YOLO train image (You SHOULD have images and label folder)')
    if(os.path.exists(f'{dataRoot}/images') & os.path.exists(f'{dataRoot}/labels')):
        print('Image Route Setup compilt')
        return dataRoot
    else:
        print('Invalid image route')

def getTooLargeLabelImage(dataRoot):
    imageDirectory = os.path(f'{dataRoot}/images')
    labelDirectory = os.path(f'{dataRoot}/labels')

    # TODO : If label is too big compare to image size, collect the name of image and return as tuple
    

def doMosaicWith4Images(dataRoot):
    # TODO : Resize Image and Label
    print('aa')