import rasterio
import numpy as np

with rasterio.open("data/processed/T1_NDVI.tif") as src:
    ndvi = src.read(1)
    profile = src.profile

# Threshold
mask = (ndvi > 0.4).astype(np.uint8)

profile.update(dtype=rasterio.uint8)

with rasterio.open("data/processed/T1_mask.tif", "w", **profile) as dst:
    dst.write(mask, 1)

print("Forest mask created.")
