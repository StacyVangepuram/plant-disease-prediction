# Plant Disease Prediction System 

A web-based application that helps identify plant diseases from images of their leaves. The system uses a Deep Learning model to classify diseases across 38 different categories and provides detailed information including symptoms, treatment, prevention, and active seasons.

## Features 
* **Image Upload:** Simple web interface to upload pictures of plant leaves.
* **Accurate Predictions:** Powered by a PyTorch `DenseNet-121` model achieving **~99.8% validation accuracy**.
* **Comprehensive Database:** Instant access to a localized database providing:
  * Disease Symptoms
  * Treatment Options
  * Prevention Strategies
  * Peak/Active Seasons
* **Confidence Score:** Displays how certain the AI is about its prediction.

## Tech Stack 
* **Web Framework:** Flask
* **Deep Learning Framework:** PyTorch, Torchvision, TIMM (PyTorch Image Models)
* **Image Processing:** Pillow (PIL)
* **Frontend:** HTML, CSS

## Supported Plants and Diseases 
The model is trained to recognize 38 classes, covering healthy leaves and common diseases for:
* Apple, Blueberry, Cherry, Corn (Maize), Grape, Orange, Peach, Bell Pepper, Potato, Raspberry, Soybean, Squash, Strawberry, and Tomato.

## Installation & Setup 

### 1. Prerequisites
Ensure you have Python 3.8+ installed. You will need the following core libraries:
```bash
pip install flask torch torchvision timm pillow
```

*(Optional dependencies for running the training notebook: `numpy`, `matplotlib`, `seaborn`, `scikit-learn`)*

### 2. Clone the Repository
```bash
git clone https://github.com/StacyVangepuram/plant-disease-prediction.git
cd plant-disease-prediction
```

### 3. Ensure Model File Exists
Make sure the pre-trained weights file is present in the `model` directory:
* `model/densenet_weights.pth`

### 4. Run the Application
Start the Flask development server:
```bash
python app.py
```
*Note: Do not use `streamlit run`. This is a Flask application.*

### 5. Open in Browser
Once the server is running, open your web browser and navigate to:
```
http://127.0.0.1:5000
```

## How It Works 
1. **Upload:** User uploads an image via the web UI.
2. **Preprocessing:** The image is resized to 224x224 and normalized.
3. **Inference:** `utils.py` passes the image tensor to the DenseNet-121 model.
4. **Information Retrieval:** The predicted class name is used as a key to look up disease specifics in the `plant_disease_database` dictionary.
5. **Rendering:** Flask renders the results dynamically into the HTML template.

## Dataset 
The model was trained on the augmented Kaggle New Plant Diseases Dataset, consisting of approximately 87,000 images of diseased and healthy plants across 38 classes.

---
*Created as an AI-powered tool for smarter agriculture and gardening.*
