import torch
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image

class ImageEncoder:

    def __init__(self):
        self.device = "cpu"

        model = models.resnet18(pretrained=True)
        model.fc = torch.nn.Identity()   # remove classifier
        model.eval()

        self.model = model.to(self.device)

        self.transform = transforms.Compose([
            transforms.Resize((224,224)),
            transforms.ToTensor(),
        ])

    def encode(self, image_path):
        image = Image.open(image_path).convert("RGB")
        image = self.transform(image).unsqueeze(0)

        with torch.no_grad():
            embedding = self.model(image)

        return embedding.squeeze().numpy()
