import os
import random
from glob import glob

import torch.utils.data
import torchvision.transforms as transforms
from PIL import Image

class Dataset(torch.utils.data.Dataset):
    # 데이터 불러오기 위한 메타데이터 생성
    def __init__(self, data_folder, image_size):
        
        if not os.path.exists(data_folder):
            raise Exception(f"[!] {data_folder} not exists.")
        
        self.label_info = {}
        self.data_info = []
        
        for i, dir in enumerate(os.listdir(data_folder)):
            self.label_info[i] = dir
            
            pathes = glob(os.path.join(data_folder, dir, '*'))
            label = [i] * len(pathes)
            
            self.data_info += list(zip(label, pathes))
            
        
        random.shuffle(self.data_info)
        
        self.transforms = transforms.Compose([
            transforms.CenterCrop(image_size),
            transforms.ToTensor(),
        ])
            
    # i번쨰 데이테를 불러올 때 무엇을 할지 정의
    def __getitem__(self, i):
        label, path = self.data_info[i]
        image = Image.open(path)
        image = self.transforms(image)
        return image, label
    
    # 전체 데이터의 길이 정의
    def __len__(self):
        return len(self.data_info)