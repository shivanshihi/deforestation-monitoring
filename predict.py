import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import rasterio

# Load model
model = tf.keras.models.load_model("forest_model", compile=False)

# Load NDVI
with rasterio.open("data/processed/T1_NDVI.tif") as src:
    ndvi = src.read(1)

# Normalize same way as training
ndvi_norm = (ndvi - ndvi.min()) / (ndvi.max() - ndvi.min())

# Take first 256x256 patch
ndvi_patch = ndvi_norm[:256, :256]
input_img = np.expand_dims(ndvi_patch, axis=(0, -1))

# Predict
prediction = model.predict(input_img)[0, :, :, 0]

# Threshold lower (0.3)
pred_mask = (prediction > 0.3).astype(np.uint8)

# Plot
plt.figure(figsize=(12,4))

plt.subplot(1,3,1)
plt.title("Original NDVI")
plt.imshow(ndvi_patch, cmap="RdYlGn")

plt.subplot(1,3,2)
plt.title("Raw Prediction")
plt.imshow(prediction, cmap="viridis")
plt.colorbar()

plt.subplot(1,3,3)
plt.title("Predicted Mask")
plt.imshow(pred_mask, cmap="gray")

plt.show()

