from patchify import patchify
import rasterio
import numpy as np
import os

os.makedirs("data/patches/images", exist_ok=True)
os.makedirs("data/patches/masks", exist_ok=True)

# Clear old patches (optional but recommended)
for folder in ["data/patches/images", "data/patches/masks"]:
    for file in os.listdir(folder):
        os.remove(os.path.join(folder, file))

# Load NDVI
with rasterio.open("data/processed/T1_NDVI.tif") as src:
    ndvi = src.read(1)

# Load mask
with rasterio.open("data/processed/T1_mask.tif") as src:
    mask = src.read(1)

# Overlapping patches (step=128)
image_patches = patchify(ndvi, (256, 256), step=128)
mask_patches = patchify(mask, (256, 256), step=128)

count = 0
for i in range(image_patches.shape[0]):
    for j in range(image_patches.shape[1]):

        img_patch = image_patches[i, j]
        mask_patch = mask_patches[i, j]

        np.save(f"data/patches/images/img_{count}.npy", img_patch)
        np.save(f"data/patches/masks/mask_{count}.npy", mask_patch)

        count += 1

print("Total patches created:", count)
