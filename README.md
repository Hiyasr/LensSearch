# LensSearch — Multimodal Image Retrieval System

## Overview

LensSearch is a command-line based image retrieval system that allows users to search for images using text queries. The system uses a pretrained deep learning model to extract image features and performs similarity search using FAISS.

This project demonstrates the practical application of computer vision, deep learning, and vector similarity search.

---

## Features

* Automated image dataset generation
* Image feature extraction using pretrained CNN (ResNet18)
* Fast similarity search using FAISS
* Command-line interface (CLI)
* Modular and scalable project structure

---

## Project Structure

```
LensSearch/
│
├── src/
│   ├── image_encoder.py
│   ├── search_engine.py
│   ├── text_encoder.py
│
├── database/          # Stores feature index (kept empty in repo)
├── download_images.py # Script to download dataset
├── flatten.py         # Dataset preprocessing
├── main.py            # Entry point
├── requirements.txt
└── README.md
```

---

## Dataset Notice

The `images/` folder is not included in this repository due to size constraints.

To generate the dataset locally, run:

```
python download_images.py
```

---

## Installation & Setup

### 1. Clone the Repository

```
git clone https://github.com/YOUR_USERNAME/LensSearch.git
cd LensSearch
```

---

### 2. Create Virtual Environment

Windows:

```
python -m venv venv
venv\Scripts\activate
```

Mac/Linux:

```
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```
pip install -r requirements.txt
```

---

## Running the Project

### Step 1 — Download Images

```
python download_images.py
```

---

### Step 2 — Run Search Engine

```
python main.py
```

---

## Usage

After running the program, enter a search query:

```
Search images: car
```

The system will return the most similar images based on feature embeddings.

---

## Technologies Used

* Python
* PyTorch
* TorchVision
* FAISS
* NumPy
* PIL

---

## How It Works

1. Images are downloaded and stored locally
2. A pretrained CNN extracts feature embeddings
3. Features are stored in a FAISS index
4. User query is converted into a vector
5. Nearest neighbor search retrieves similar images

---

## Important Notes

* This project is fully executable via command line
* No GUI setup is required
* Ensure Python and dependencies are properly installed
* Dataset is generated dynamically using provided script

---

## Author

Hiya Singh
Computer Vision Project Submission  
