import os
import sys
import csv
import json 
import shutil
import zipfile
import argparse
import cv2

from glob import glob
from tqdm import tqdm
from google_drive_downloader import GoogleDriveDownloader as gdd

DATA_ROOT_DIR = 'dataset'
TRAIN_DATA_DIR = f'train'
VAL_DATA_DIR = f'val'

LABEL_MAP_FILE = './label_map.json'
LABEL_MAP_FILE_ID = '1pJlcGT34hoZVlIRBXfHLUPJJpMGT8zMK'

def download(train):
    DATASET_DIR = f'{DATA_ROOT_DIR}/{TRAIN_DATA_DIR}' if train else f'{DATA_ROOT_DIR}/{VAL_DATA_DIR}'
    
    LABEL_FILE = f'./{DATASET_DIR}/label.csv'
    LABEL_FILE_ID = '1iwnfmQn8HXA1uCAaA5MfEZ3cUC3x2v0x' if train else '1p4q3vPK82qJxy39a4Eu-NawtIm0uQO1P'
    IMAGE_FILE_NAME = f'./{DATASET_DIR}/image.zip'
    IMAGE_FILE_ID = '1KnYXKmHouQKVG93qbmJijCoSCeeMOkDM' if train else '1K8xBzpDBfOIGoehCXbVs3hl_uY1moHRn'
    
    if os.path.exists(f'./{DATASET_DIR}/images/') and os.path.exists(f'./{DATASET_DIR}/labels/'): return
    
    if os.path.exists(f'./{DATASET_DIR}/images/'): 
        shutil.rmtree(f'./{DATASET_DIR}/images/')
    os.makedirs(f'./{DATASET_DIR}/images/')
        
    if os.path.exists(f'./{DATASET_DIR}/labels/'): 
        shutil.rmtree(f'./{DATASET_DIR}/labels/')
    os.makedirs(f'./{DATASET_DIR}/labels/')
    
    # Google Drive에서 데이터 다운
    gdd.download_file_from_google_drive(file_id=LABEL_FILE_ID, dest_path=LABEL_FILE, showsize=True)
    gdd.download_file_from_google_drive(file_id=LABEL_MAP_FILE_ID, dest_path=LABEL_MAP_FILE, showsize=True)
    gdd.download_file_from_google_drive(file_id=IMAGE_FILE_ID, dest_path=IMAGE_FILE_NAME, showsize=True)
    
    if not os.listdir(f'./{DATASET_DIR}/images/'):
        print("Extract Data...")
        with zipfile.ZipFile(IMAGE_FILE_NAME, 'r') as zip_ref:
            for file in tqdm(iterable=zip_ref.namelist(), total=len(zip_ref.namelist())):
                zip_ref.extract(member=file, path=f'./{DATASET_DIR}/images/')
        os.remove(IMAGE_FILE_NAME)
    
    # ImageNet data label읽기
    with open(LABEL_FILE, newline='') as f:
        reader = csv.reader(f)
        data = [tuple(row) for row in reader]
        data = data[1:]
    
    with open(LABEL_MAP_FILE) as json_file:
        label_map = json.load(json_file)
    
    if train:
        print("Make image")
        for image_dir in tqdm(os.listdir(f'./{DATASET_DIR}/images/')):
            for image in os.listdir(f'./{DATASET_DIR}/images/{image_dir}/'):
                shutil.move(f'./{DATASET_DIR}/images/{image_dir}/{image}', f'./{DATASET_DIR}/images/{image}')
            os.rmdir(f'./{DATASET_DIR}/images/{image_dir}/')
    
    images = set([ i.split('.')[0] for i in os.listdir(f'./{DATASET_DIR}/images/')])
    
    # 데이터 전처리
    print("Make label")
    for datom in tqdm(data):
        image_id, prediction_string = datom
        if not image_id in images: continue
        
        prediction_string = prediction_string.split()
        image = cv2.imread(f'./{DATASET_DIR}/images/{image_id}.JPEG')
        image_height, image_width, _ = image.shape
        
        with open(f'./{DATASET_DIR}/labels/{image_id}.txt', 'w') as f:
            for i in range(0, len(prediction_string), 5):
                if not prediction_string[i] in label_map: continue
                x_center      = ((int(prediction_string[i + 1]) + int(prediction_string[i + 3])) / 2) / image_width
                y_center      = ((int(prediction_string[i + 2]) + int(prediction_string[i + 4])) / 2) / image_height
                object_width  = (int(prediction_string[i + 3]) - int(prediction_string[i + 1])) / image_width
                object_height = (int(prediction_string[i + 4]) - int(prediction_string[i + 2])) / image_height
                f.write(f'{label_map[prediction_string[i]]} {x_center} {y_center} {object_width} {object_height}\n')
    
    # os.remove(LABEL_FILE)

    iamges = set([ i.split('.')[0] + '.JPEG' for i in os.listdir(f'./{DATASET_DIR}/labels/')])
    
    print('Remove not annotated image')
    for image in tqdm(os.listdir(f'./{DATASET_DIR}/images/')):
        if not image in iamges:
            os.remove(f'./{DATASET_DIR}/images/{image}')
            
download(True)
download(False)
with open(LABEL_MAP_FILE) as json_file:
    label_map = json.load(json_file)

print('Make dataset.yaml')

data = f"""path: {DATA_ROOT_DIR}  # dataset root dir
train: {TRAIN_DATA_DIR}  # train images (relative to 'path') 128 images
val: {VAL_DATA_DIR}  # val images (relative to 'path') 128 images
test:  # test images (optional)

# Classes
nc: {len(label_map)}  # number of classes
names: {list(label_map.keys())}  # class names"""

with open(f'{DATA_ROOT_DIR}/dataset.yaml', 'w') as f:
    f.write(data)