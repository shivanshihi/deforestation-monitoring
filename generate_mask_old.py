import rasterio
import numpy as np

with rasterio.open("data/processed/T_old_NDVI.tif") as src:
    ndvi = src.read(1)
    profile = src.profile

mask = (ndvi > 0.4).astype(np.uint8)

profile.update(dtype=rasterio.uint8)

with rasterio.open("data/processed/T_old_mask.tif", "w", **profile) as dst:
    dst.write(mask, 1)

print("Old forest mask created.")
