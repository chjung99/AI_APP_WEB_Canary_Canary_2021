import os
from google_drive_downloader import GoogleDriveDownloader as gdd
import shutil
import csv
import json 
from tqdm import tqdm

LABEL_FILE = './dataset/label.csv'
LABEL_FILE_ID = '1iwnfmQn8HXA1uCAaA5MfEZ3cUC3x2v0x'
LABEL_MAP_FILE = './label_map.json'
LABEL_MAP_FILE_ID = '1pJlcGT34hoZVlIRBXfHLUPJJpMGT8zMK'

if not os.path.exists('./dataset/images/'): os.makedirs('./dataset/images/')
if not os.path.exists('./dataset/labels/'): os.makedirs('./dataset/labels/')
    
gdd.download_file_from_google_drive(file_id=LABEL_FILE_ID, dest_path=LABEL_FILE, showsize=True)
gdd.download_file_from_google_drive(file_id=LABEL_MAP_FILE_ID, dest_path=LABEL_MAP_FILE, showsize=True)
                                    
with open(LABEL_FILE, newline='') as f:
    reader = csv.reader(f)
    data = [tuple(row) for row in reader]
    data = data[1:]

with open(LABEL_MAP_FILE) as json_file:
    label_map = json.load(json_file)

for datom in tqdm(data):
    image_id, prediction_string = datom
    prediction_string = prediction_string.split()
    # shutil.move(f'')
    
    
    with open(f'./dataset/labels/{image_id}.txt', 'w') as f:
        for i in range(0, len(prediction_string), 5):
            if not prediction_string[0] in label_map: continue
            f.write(f'{label_map[prediction_string[i]]} {prediction_string[i + 1]} {prediction_string[i + 2]} {prediction_string[i + 3]} {prediction_string[i + 4]}\n')
    