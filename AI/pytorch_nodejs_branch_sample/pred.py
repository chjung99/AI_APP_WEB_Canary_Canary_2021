from models import MyModel
from torchvision import transforms
import torch
from PIL import Image

import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--image_size', type=int, default=256)
parser.add_argument('--image_path', '-p')

args = parser.parse_args()

imsize = args.image_size
loader = transforms.Compose([transforms.Scale(imsize), transforms.ToTensor()])

def image_loader(image_name, device):
    image = Image.open(image_name)
    image = loader(image)
    image = torch.FloatTensor(image)
    image = image.unsqueeze(0)
    return image.to(device)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = MyModel()

image = image_loader(args.image_path, device)
pred = model(image)

print(pred)
