import torch
from torchvision import models
import torch.nn as nn

class Model(nn.Module):
    # 보통 모델 구조 정의
    def __init__(self, num_classes):
        super(Model, self).__init__()
        
        # feature extraction 정의
        self.features = models.vgg16(pretrained=True).features
        
        # linear classifier를 위한 average pooling
        self.avgpool = nn.AdaptiveAvgPool2d((7, 7))
        
        # linear classifier
        self.classifier = nn.Sequential(
            nn.Linear(512 * 7 * 7, 4096),
            nn.ReLU(True),
            nn.Dropout(),
            nn.Linear(4096, 4096),
            nn.ReLU(True),
            nn.Dropout(),
            nn.Linear(4096, num_classes),
        )
        
    # 모델을 call 했을 때 데이터를 어떻게 처리할지 정의
    # img -> model(img) -> result
    def forward(self, x):
        x = self.features(x)
        x = self.avgpool(x)
        x = torch.flatten(x, 1)
        x = self.classifier(x)
        return x