import os
import shutil

root = "images"

for folder in os.listdir(root):
    path = os.path.join(root, folder)

    if os.path.isdir(path):
        for file in os.listdir(path):
            shutil.move(os.path.join(path, file), root)

        os.rmdir(path)