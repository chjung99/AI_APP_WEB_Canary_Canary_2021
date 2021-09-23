import torch.nn as nn
import torchvision.models as models

class MyModel(nn.Module):
    def __init__(self):
        super(MyModel, self).__init__()
        self.model = models.resnet18()
        
    def forward(self, x):
        return self.model(x)