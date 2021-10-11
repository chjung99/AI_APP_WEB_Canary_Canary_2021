import torch
import pandas as pd
from skimage import io, transform
import numpy as np
from torch.utils.data import Dataset, DataLoader
import torchvision
from torchvision import transforms, utils
import os
import cv2
import torchvision.transforms as T
import torchvision.transforms.functional as FT
from torch.utils.data import DataLoader
from datetime import datetime
import time
import torch.optim
import torch.backends.cudnn as cudnn
from utils import *
from dataset import *




root_dir='/content/drive/MyDrive/osam/dataset'
annotation_dir='/content/drive/MyDrive/osam/LOC_train_solution.csv'
txt_file='/content/drive/MyDrive/osam/sol_train_idx2.txt'


val_root_dir='/content/drive/MyDrive/osam/sub'
val_annotation_dir='/content/drive/MyDrive/osam/LOC_val_solution.csv'
val_txt_file='/content/drive/MyDrive/osam/sol_val_idx2.txt'

label_map={'n02687172':0,
'n02916936': 1,
'n02950826': 2,
'n03180011': 3,
'n03594945': 4,
'n03642806': 5,
'n03763968': 6,
'n03773504': 7,
'n03782006': 8,
'n03786901': 9,
'n04008634': 10,
'n04086273': 11,
'n04090263': 12,
'n04389033': 13,
'n04552348': 14,
'n06794110': 15,}

transform = T.Compose([T.Resize([320,320]), T.ToTensor(),T.Normalize(mean=[0.485, 0.456, 0.406],
                                 std=[0.229, 0.224, 0.225])])

epochs_since_improvement = 0  
best_loss = 100.
workers = 2
batch_size=128 #128
print_freq = 1
lr = 1e-3  
momentum = 0.9  
weight_decay = 5e-4  
device='cuda'
torch.manual_seed(1)
torch.cuda.manual_seed(1)
jobs_dir='/content/drive/MyDrive/osam/jobs'
cudnn.benchmark = True
start_epoch = 0  
checkpoint=None
num_classes=16 #18+back


def main():
    """
    Training and validation.
    """
    global epochs_since_improvement, start_epoch, label_map, best_loss, epoch, checkpoint, decay_lr_at

    # Initialize model or load checkpoint
    if checkpoint is None:
        model = torchvision.models.detection.ssdlite320_mobilenet_v3_large(num_classes=num_classes,pretrained_backbone=True,trainable_backbone_layers=6)
        
        # Initialize the optimizer, with twice the default learning rate for biases, as in the original Caffe repo
        biases = list()
        not_biases = list()
        for param_name, param in model.named_parameters():
          biases = list()
          not_biases = list()
          if param.requires_grad:
              if param_name.endswith('.bias'):
                  biases.append(param)
              else:
                  not_biases.append(param)
        optimizer = torch.optim.SGD(params=[{'params': biases, 'lr': 2 * lr}, {'params': not_biases}],
                                    lr=lr, momentum=momentum, weight_decay=weight_decay)
        
        
    else:
        checkpoint = torch.load(checkpoint)
        start_epoch = checkpoint['epoch'] + 1
        epochs_since_improvement = checkpoint['epochs_since_improvement']
        best_loss = checkpoint['best_loss']
        print('\nLoaded checkpoint from epoch %d. Best loss so far is %.3f.\n' % (start_epoch, best_loss))
        model = checkpoint['model']
        optimizer = checkpoint['optimizer']
        
        
    # Move to default device
    model = model.to(device)
    

    # Custom dataloaders
    train_dataset = ImageNetDataset(txt_file,root_dir,annotation_dir,transform=transform,mode='TRAIN')
        
    train_loader =  DataLoader(train_dataset, batch_size=batch_size, shuffle=True,num_workers=workers) # note that we're passing the collate function here
    val_dataset = ImageNetDataset(val_txt_file,val_root_dir,val_annotation_dir,transform=transform,mode='VAL')

    val_loader =  DataLoader(val_dataset, batch_size=batch_size, shuffle=True,num_workers=workers) # note that we're passing the collate function here

    for epoch in range(start_epoch,300):
        
        
        
        
        # One epoch's validation
        train(train_loader=train_loader,model=model,optimizer=optimizer,epoch=epoch)
        val_loss = validate(val_loader=val_loader,
                            model=model)
        
        # Did validation loss improve?
        is_best = val_loss < best_loss
        best_loss = min(val_loss, best_loss)
        
        if not is_best:
            
            epochs_since_improvement += 1
            print("\nEpochs since last improvement: %d\n" % (epochs_since_improvement,))

        else:
            
            epochs_since_improvement = 0
        if epoch % 1 ==0:    
          # Save checkpoint
          save_checkpoint(epoch, epochs_since_improvement, model, optimizer, val_loss, best_loss, is_best,jobs_dir)



def train(train_loader, model,optimizer, epoch):

  model.train()  # training mode enables dropout

  batch_time = AverageMeter()  # forward prop. + back prop. time
  data_time = AverageMeter()  # data loading time
  losses = AverageMeter()  # loss

  start = time.time()
  
  for i, (images, boxes,labels) in enumerate(train_loader):
    
    images = images.to(device)
    
    targets=[]
    
    for j in range(images.shape[0]):
      d={}
      d['boxes'] = boxes[j].to(device)
      d['labels'] = labels[j].to(device)
      targets.append(d)
    
    out=model(images,targets)
    
    loss=out['bbox_regression']+(out['classification'])/(4.0)
    
    optimizer.zero_grad()
    
    loss.backward()
    
    optimizer.step()
    
    losses.update(loss.item(), images.size(0))
    batch_time.update(time.time() - start)

    start = time.time()

    
    # targets=[targets]
    # targets[0]['labels']=targets[0]['labels'].squeeze(0)
    if i % print_freq == 0:
              print('Epoch: [{0}][{1}/{2}]\t'
                    'Batch Time {batch_time.val:.3f} ({batch_time.avg:.3f})\t'
                    'Data Time {data_time.val:.3f} ({data_time.avg:.3f})\t'
                    'Loss {loss.val:.4f} ({loss.avg:.4f})\t'.format(epoch, i, len(train_loader),
                                                                    batch_time=batch_time,
                                                                    data_time=data_time, loss=losses))
  del out,images, boxes, labels  # free some memory since their histories may be stored



def validate(val_loader, model):
    
    # model.eval()  # eval mode disables dropout

    batch_time = AverageMeter()
    losses = AverageMeter()

    start = time.time()

    # Prohibit gradient computation explicity because I had some problems with memory
    with torch.no_grad():
        # Batches
        for i, (images, boxes, labels) in enumerate(val_loader):

            # Move to default device
            images = images.to(device)
    
            targets=[]
            
            for j in range(images.shape[0]):
              d={}
              d['boxes'] = boxes[j].to(device)
              d['labels'] = labels[j].to(device)
              targets.append(d)
            
            out=model(images,targets)
            
            loss=out['bbox_regression']+(out['classification'])/(4.0)

            losses.update(loss.item(), images.size(0))
            batch_time.update(time.time() - start)

            start = time.time()

            # Print status
            if i % print_freq == 0:
                print('[{0}/{1}]\t'
                      'Batch Time {batch_time.val:.3f} ({batch_time.avg:.3f})\t'
                      'Loss {loss.val:.4f} ({loss.avg:.4f})\t'.format(i, len(val_loader),
                                                                      batch_time=batch_time,
                                                                      loss=losses))

    print('\n * LOSS - {loss.avg:.3f}\n'.format(loss=losses))
    
    return losses.avg





if __name__ == '__main__':
    main()
