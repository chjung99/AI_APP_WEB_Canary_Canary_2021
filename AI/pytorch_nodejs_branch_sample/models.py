import torch.nn as nn
import torchvision.models as models

class MyModel(nn.Module):
    def __init__(self):
        self.model = models.vgg16()
        
    def forward(self, x):
        return self.model(x)