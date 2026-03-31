import torchvision.datasets as datasets
import torchvision.transforms as transforms
from PIL import Image
import os

# Folder where images will be saved
SAVE_DIR = "images"
os.makedirs(SAVE_DIR, exist_ok=True)

print("Downloading dataset...")

# CIFAR10 dataset (60,000 images)
dataset = datasets.CIFAR10(
    root="data",
    train=True,
    download=True
)

print("Saving images locally...")

for i, (img, label) in enumerate(dataset):
    img.save(f"{SAVE_DIR}/img_{i}.png")

print("Images ready ✅")