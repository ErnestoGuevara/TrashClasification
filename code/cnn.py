import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.models as models


class ResNet(nn.Module):
    def __init__(self):
        super().__init__()
        output_layer = 6
        # Use a model resnet50
        self.network = models.resnet50(pretrained=True)
        # Replace last layer
        num_ftrs = self.network.fc.in_features
        self.network.fc = nn.Linear(num_ftrs, output_layer)

    def forward(self, xb):
        x = torch.sigmoid(self.network(xb))

        return x


