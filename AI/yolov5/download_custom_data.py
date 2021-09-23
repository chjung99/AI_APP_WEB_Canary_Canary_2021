import os
import sys
import csv
import json 
import shutil
import zipfile
import argparse
import cv2
import numpy as np

from glob import glob
from tqdm import tqdm
from google_drive_downloader import GoogleDriveDownloader as gdd
from xml.etree.ElementTree import parse

DATA_ROOT_DIR = 'dataset'
TRAIN_DATA_DIR = f'train'
VAL_DATA_DIR = f'val'

DATA_ID = '1b-0r6JX70k1tCI4B10ZIqZ474CLgnp1Y'
DATA_PATH = f'{DATA_ROOT_DIR}/custom.zip'

LABEL_MAP_FILE = './label_map.json'
LABEL_MAP_FILE_ID = '1jZoQkr5E8xrSvmPhRqDXDqm88OedlT--'

if not os.path.exists(f'{DATA_ROOT_DIR}/{TRAIN_DATA_DIR}/images/'): os.makedirs(f'{DATA_ROOT_DIR}/{TRAIN_DATA_DIR}/images/')
if not os.path.exists(f'{DATA_ROOT_DIR}/{TRAIN_DATA_DIR}/labels/'): os.makedirs(f'{DATA_ROOT_DIR}/{TRAIN_DATA_DIR}/labels/')
if not os.path.exists(f'{DATA_ROOT_DIR}/{VAL_DATA_DIR}/images/'): os.makedirs(f'{DATA_ROOT_DIR}/{VAL_DATA_DIR}/images/')
if not os.path.exists(f'{DATA_ROOT_DIR}/{VAL_DATA_DIR}/labels/'): os.makedirs(f'{DATA_ROOT_DIR}/{VAL_DATA_DIR}/labels/')

gdd.download_file_from_google_drive(file_id=DATA_ID, dest_path=DATA_PATH, showsize=True)
gdd.download_file_from_google_drive(file_id=LABEL_MAP_FILE_ID, dest_path=LABEL_MAP_FILE, showsize=True)

with open(LABEL_MAP_FILE) as json_file:
        label_map = json.load(json_file)
        
with zipfile.ZipFile(DATA_PATH, 'r') as zip_ref:
    for file in tqdm(iterable=zip_ref.namelist(), total=len(zip_ref.namelist())):
        zip_ref.extract(member=file, path=f'./{DATA_ROOT_DIR}/')

def make_data(dir_name):
    if not os.path.exists(f'{DATA_ROOT_DIR}/images/{dir_name}/'): os.makedirs(f'{DATA_ROOT_DIR}/images/{dir_name}/')
    if not os.path.exists(f'{DATA_ROOT_DIR}/labels/{dir_name}/'): os.makedirs(f'{DATA_ROOT_DIR}/labels/{dir_name}/')
    
    images = os.listdir(f'{DATA_ROOT_DIR}/custom_data/{dir_name}/Images/')
    
    for image in tqdm(images):
        tree = parse(f'{DATA_ROOT_DIR}/custom_data/{dir_name}/Annotations/{image.split(".")[0]}.xml')
        root = tree.getroot()
        
        with open(f'{DATA_ROOT_DIR}/labels/{dir_name}/{image.split(".")[0]}.txt', 'w') as f:
            image_width, image_height = float(root.find('size').find('width').text), float(root.find('size').find('height').text)
            objs = root.findall('object')
            
            for obj in objs:
                label = obj.find('name').text
                bbox = obj.find('bndbox')
                
                xmin, ymin, xmax, ymax = float(bbox.find('xmin').text), float(bbox.find('ymin').text), float(bbox.find('xmax').text), float(bbox.find('ymax').text)
                x_center        = (xmax + xmin) / 2 / image_width
                y_center        = (ymax + ymin) / 2 / image_height
                object_width    = (xmax - xmin) / image_width
                object_height   = (ymax - ymin) / image_height
                
                f.write(f'{label} {x_center} {y_center} {object_width} {object_height}\n')
        
        shutil.move(f'{DATA_ROOT_DIR}/custom_data/{dir_name}/Images/{image}', f'{DATA_ROOT_DIR}/images/{dir_name}/{image}')
        
def split(dir_name, train_ratio=0.95):
    data_len = len(os.listdir(f'{DATA_ROOT_DIR}/images/{dir_name}/'))
    train_index = set(np.random.randint(int(train_ratio * 0.9), size=data_len).flatten())
    
    images = os.listdir(f'{DATA_ROOT_DIR}/images/{dir_name}/')
    
    for i in tqdm(range(data_len)):
        if i in train_index:
            shutil.move(f'{DATA_ROOT_DIR}/images/{dir_name}/{images[i]}', f'{DATA_ROOT_DIR}/{TRAIN_DATA_DIR}/images/{images[i]}')
            shutil.move(f'{DATA_ROOT_DIR}/labels/{dir_name}/{images[i].split(".")[0]}.txt', f'{DATA_ROOT_DIR}/{TRAIN_DATA_DIR}/labels/{images[i].split(".")[0]}.txt')
        else:
            shutil.move(f'{DATA_ROOT_DIR}/images/{dir_name}/{images[i]}', f'{DATA_ROOT_DIR}/{VAL_DATA_DIR}/images/{images[i]}')
            shutil.move(f'{DATA_ROOT_DIR}/labels/{dir_name}/{images[i].split(".")[0]}.txt', f'{DATA_ROOT_DIR}/{VAL_DATA_DIR}/labels/{images[i].split(".")[0]}.txt')
            

print('Download mark data')
make_data('mark_annotation')
print('Download paper data')
make_data('paper_annotation')
shutil.rmtree(f'{DATA_ROOT_DIR}/custom_data')

print('Split mark data')
split('mark_annotation')
print('Split mapaperrk data')
split('paper_annotation')

shutil.rmtree(f'{DATA_ROOT_DIR}/images')
shutil.rmtree(f'{DATA_ROOT_DIR}/labels')

