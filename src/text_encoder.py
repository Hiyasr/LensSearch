import torch
import torchvision.models as models

class TextEncoder:

    def __init__(self):
        self.device = "cpu"
        self.model = models.resnet18(pretrained=True)
        self.model.fc = torch.nn.Identity()
        self.model.eval()

    def encode(self, text):
        torch.manual_seed(abs(hash(text)) % (2**32))
        return torch.randn(512).numpy()