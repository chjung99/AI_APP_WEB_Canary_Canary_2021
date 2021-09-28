import os
import cv2
import torch
import pandas as pd
import torchvision.transforms.functional as FT
from torch.utils.data import Dataset, DataLoader

class ImageNetDataset(Dataset):
    


    def __init__(self,txt_file, root_dir,annotation_dir, transform=None,mode=None):
        """
        Args:
            
            root_dir (string): 모든 이미지가 존재하는 디렉토리 경로
            transform (callable, optional): 샘플에 적용될 Optional transform

        """
        f = open(txt_file,'r')
        lines=f.readlines()
        lines=list(map(lambda s: s.strip(), lines))

        self.idx_txt=lines
        self.annotation_dir=annotation_dir
        self.root_dir = root_dir
        self.transform = transform

        self.mode=mode

    def __len__(self):
        
        return len(self.idx_txt)

    def __getitem__(self, idx):
      
      if self.mode=='TRAIN':
        img_name=self.idx_txt[idx].split(" ")[0]
        folder_name=img_name.split("_")[0]
        img_path=os.path.join(self.root_dir,folder_name,img_name+'.JPEG')
        img = cv2.imread(img_path)  #(height, width, channel) 
        
        solution=pd.read_csv(self.annotation_dir)
        
        cond=solution['ImageId'] == img_name
        ans_ls=solution[cond]['PredictionString'].item().split(' ')
        ans_ls=ans_ls[:5]#For example, n01978287 240 170 260 240 means it's label n01978287, with a bounding box of coordinates (x_min, y_min, x_max, y_max)

        boxes=[]
        labels=[]
        # d={}
        # labels.append(label_map[ans_ls[0]])
        # boxes.append(ans_ls[1:])
        # import pdb;pdb.set_trace()
        for i in range(len(ans_ls)%4):
          labels.append(label_map[ans_ls[5*i]])
          boxes.append(ans_ls[5*i+1:5*i+5])
          
        labels=torch.tensor(labels,dtype=torch.int64)
        boxes=torch.FloatTensor(np.array(boxes,dtype=np.float64))

      elif self.mode=='VAL':
        
        img_name=self.idx_txt[idx].split(" ")[0]
        
        img_path=os.path.join(self.root_dir,img_name+'.JPEG')
        img = cv2.imread(img_path)  #(height, width, channel) 
        
        solution=pd.read_csv(self.annotation_dir)
        
        cond=solution['ImageId'] == img_name
        ans_ls=solution[cond]['PredictionString'].item().split(' ')
        ans_ls=ans_ls[:5]#For example, n01978287 240 170 260 240 means it's label n01978287, with a bounding box of coordinates (x_min, y_min, x_max, y_max)

        boxes=[]
        labels=[]
        # d={}
        # labels.append(label_map[ans_ls[0]])
        # boxes.append(ans_ls[1:])
        # import pdb;pdb.set_trace()
        for i in range(len(ans_ls)%4):
          labels.append(label_map[ans_ls[5*i]])
          boxes.append(ans_ls[5*i+1:5*i+5])
          
        labels=torch.tensor(labels,dtype=torch.int64)
        boxes=torch.FloatTensor(np.array(boxes,dtype=np.float64))        
        # d['boxes']=boxes
        # d['labels']=labels
      else:
        import pdb;pdb.set_trace()
#         The input to the model is expected to be a list of tensors, each of shape [C, H, W], one for each image, and should be in 0-1 range. Different images can have different sizes.

# The behavior of the model changes depending if it is in training or evaluation mode.

# During training, the model expects both the input tensors, as well as a targets (list of dictionary), containing:

# boxes (FloatTensor[N, 4]): the ground-truth boxes in [x1, y1, x2, y2] format, with 0 <= x1 < x2 <= W and 0 <= y1 < y2 <= H.

# labels (Int64Tensor[N]): the class label for each ground-truth box
        
      if self.transform:
          img=FT.to_pil_image(img)
          img = self.transform(img)
        
        
      return img,boxes,labels
