# 🌍 Deforestation Monitoring using Deep Learning & Satellite Imagery

## 📌 Project Overview
This project presents an automated system to detect deforestation using Sentinel-2 satellite imagery and deep learning techniques. The system computes vegetation indices (NDVI), segments forest regions using a U-Net model, and compares satellite images from different time periods to identify forest loss.

---

## 🎯 Objectives
- Monitor forest cover using satellite data
- Detect deforestation between two time periods
- Apply deep learning (U-Net) for semantic segmentation
- Visualize vegetation and forest change

---

## 🛰️ Dataset
- Source: Copernicus Sentinel-2
- Bands used:
  - **B04 (Red)**
  - **B08 (Near Infrared - NIR)**

These bands are used to compute NDVI, which highlights vegetation density.

---

## ⚙️ Methodology

### 1️⃣ NDVI Calculation
NDVI is computed using:

\[
NDVI = \frac{NIR - Red}{NIR + Red}
\]

- High NDVI → Dense vegetation  
- Low NDVI → Sparse vegetation / non-forest  

---

### 2️⃣ Forest Mask Generation
NDVI is converted into a binary forest map:

- NDVI > 0.4 → Forest  
- NDVI ≤ 0.4 → Non-Forest  

---

### 3️⃣ Patch Extraction
- Images are divided into **256×256 patches**
- Overlapping patches are used for better training

---

### 4️⃣ Deep Learning Model
- Model: **U-Net Convolutional Neural Network**
- Task: Pixel-wise image segmentation
- Loss Function: Dice Loss
- Optimizer: Adam

---

### 5️⃣ Deforestation Detection
Forest maps from two time periods are compared:
Deforestation = Forest(T_old) AND NOT Forest(T_new)


This identifies areas where forest has been lost.

---

## 🧠 Workflow


Satellite Images
↓
Download B04 & B08 Bands
↓
NDVI Calculation
↓
Forest Mask Generation
↓
Patch Extraction
↓
U-Net Training
↓
Prediction
↓
Temporal Comparison
↓
Deforestation Map


---

## 🛠️ Technologies Used

| Tool | Purpose |
|------|--------|
| Python | Programming |
| TensorFlow | Deep Learning |
| NumPy | Numerical operations |
| Rasterio | Satellite image processing |
| Matplotlib | Visualization |
| Patchify | Patch creation |

---

## ▶️ How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
2. Run the project (Demo)
python visualize_old_ndvi.py
python predict.py
python detect_real_deforestation.py
📊 Output

The system produces:

NDVI Map (Vegetation visualization)
Forest Segmentation Map
Deforestation Detection Map
Interpretation:
🟢 Green → Vegetation
⚪ White → Forest
⚫ Black → Non-Forest
🔴 Red → Deforestation
🟩 Green → Reforestation
📁 Project Structure
deforestation-monitoring/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── patches/
│
├── ndvi.py
├── run_ndvi.py
├── run_ndvi_T2.py
├── run_ndvi_old.py
│
├── generate_mask.py
├── generate_mask_T2.py
├── generate_mask_old.py
│
├── create_patches.py
├── real_dataset_loader.py
│
├── unet.py
├── train.py
├── predict.py
│
├── detect_deforestation.py
├── detect_real_deforestation.py
│
├── requirements.txt
└── README.md

🚀 Key Features
Uses real satellite imagery
NDVI-based vegetation detection
Deep learning-based segmentation
Temporal analysis for change detection
Visual output for easy interpretation

⚠️ Limitations
Small dataset (limited training samples)
NDVI threshold may vary across regions
Model accuracy depends on data quality

🔮 Future Improvements
Use larger dataset for better training
Integrate Google Earth Engine (GEE)
Improve model accuracy with augmentation
Automate data collection pipeline

📚 Conclusion
This project demonstrates how remote sensing and deep learning can be combined to monitor forest changes effectively. It provides a scalable approach for environmental monitoring and conservation.

👩‍💻 Author
Shivanshi
