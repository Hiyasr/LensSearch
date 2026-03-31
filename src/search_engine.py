import os

class LensSearch:

    def __init__(self):
        self.images = []

    def build_index(self):
        dataset_path = "images"

        if not os.path.exists(dataset_path):
            print("Dataset folder not found!")
            return

        self.images = os.listdir(dataset_path)
        print(f"Indexed {len(self.images)} images")

    def search(self, query):
        # dummy search (replace later)
        return self.images[:5]