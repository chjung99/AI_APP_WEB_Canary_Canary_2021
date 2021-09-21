import os
import csv
import json 
import shutil
import zipfile

from glob import glob
from tqdm import tqdm
from google_drive_downloader import GoogleDriveDownloader as gdd

LABEL_FILE = './dataset/label.csv'
LABEL_FILE_ID = '1iwnfmQn8HXA1uCAaA5MfEZ3cUC3x2v0x'
LABEL_MAP_FILE = './label_map.json'
LABEL_MAP_FILE_ID = '1pJlcGT34hoZVlIRBXfHLUPJJpMGT8zMK'
IMAGE_FILE_ID = '1KnYXKmHouQKVG93qbmJijCoSCeeMOkDM'
IMAGE_FILE_NAME = './dataset/image.zip'

if not os.path.exists('./dataset/images/'): os.makedirs('./dataset/images/')
if not os.path.exists('./dataset/labels/'): os.makedirs('./dataset/labels/')

# Google Drive에서 데이터 다운
gdd.download_file_from_google_drive(file_id=LABEL_FILE_ID, dest_path=LABEL_FILE, showsize=True)
gdd.download_file_from_google_drive(file_id=LABEL_MAP_FILE_ID, dest_path=LABEL_MAP_FILE, showsize=True)
gdd.download_file_from_google_drive(file_id=IMAGE_FILE_ID, dest_path=IMAGE_FILE_NAME, showsize=True)

if not os.listdir('./dataset/images/'):
    print("Extract Data...")
    with zipfile.ZipFile(IMAGE_FILE_NAME, 'r') as zip_ref:
        for file in tqdm(iterable=zip_ref.namelist(), total=len(zip_ref.namelist())):
            zip_ref.extract(member=file, path='./dataset/images/')
    os.remove(IMAGE_FILE_NAME)

# ImageNet data label읽기
with open(LABEL_FILE, newline='') as f:
    reader = csv.reader(f)
    data = [tuple(row) for row in reader]
    data = data[1:]

with open(LABEL_MAP_FILE) as json_file:
    label_map = json.load(json_file)

print("Make image")
for image_dir in tqdm(os.listdir('./dataset/images/')):
    for image in os.listdir(f'./dataset/images/{image_dir}/'):
        shutil.move(f'./dataset/images/{image_dir}/{image}', f'./dataset/images/{image}')
    os.rmdir(f'./dataset/images/{image_dir}/')

images = os.listdir(f'./dataset/images/')

# 데이터 전처리
print("Make label")
for datom in tqdm(data):
    image_id, prediction_string = datom
    prediction_string = prediction_string.split()
    
    if not image_id.split('_')[0] in label_map: continue
    with open(f'./dataset/labels/{image_id}.txt', 'w') as f:
        for i in range(0, len(prediction_string), 5):
            if not prediction_string[i] in label_map: continue
            f.write(f'{label_map[prediction_string[i]]} {prediction_string[i + 1]} {prediction_string[i + 2]} {prediction_string[i + 3]} {prediction_string[i + 4]}\n')

