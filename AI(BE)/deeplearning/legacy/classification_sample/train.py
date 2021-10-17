import argparse

import torch
import torch.nn as nn
import torch.utils.data
from torch.optim.adam import Adam
import torchvision.datasets

from model import Model
from dataset import Dataset

parser = argparse.ArgumentParser()

parser.add_argument('--image_size', type=int, default=224, help='the height / width of the input image to network')
parser.add_argument('--data_dir', type=str, default='dataset', help='path of dataset directory')
parser.add_argument('--num_epochs', type=int, default=100, help='the number of epochs')
parser.add_argument('--lr', type=int, default=1e-3, help='learning rate')
parser.add_argument('--batch_size', type=int, default=4, help='batch size')
parser.add_argument('--num_classes', type=int, default=2, help='num classes')

args = parser.parse_args()

def train(net, data_loader, num_epochs, lr):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    net = net.to(device)
    optimizer = Adam(net.parameters(), lr=lr)
    criterion = nn.CrossEntropyLoss()
    num_steps = len(data_loader)
    
    for epoch in range(num_epochs):
        for step, (images, labels) in enumerate(data_loader):
            # images = images.repeat(1, 3, 1, 1)
            
            images = images.to(device)
            labels = labels.to(device)
            
            preds = net(images)
            loss = criterion(preds, labels)
            
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            
            print(preds, labels)
            
            print(f'[{epoch}/{num_epochs}][{step}/{num_steps}] {loss.data}')


dataset = Dataset(args.data_dir, args.image_size)

# import torchvision.transforms as transforms
# transform=transforms.Compose([
#     transforms.Resize(args.image_size),
#     transforms.ToTensor(),
#     transforms.Normalize((0.1307,), (0.3081,))
# ])
# dataset = torchvision.datasets.MNIST('./', train=True, download=True, transform=transform)

data_loader = torch.utils.data.DataLoader(dataset=dataset, batch_size=args.batch_size, shuffle=True)
net = Model(args.num_classes)

train(net, data_loader, args.num_epochs, args.lr)