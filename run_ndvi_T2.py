from ndvi import compute_ndvi
import os

os.makedirs("data/processed", exist_ok=True)

compute_ndvi(
    "data/raw/T2_B04.tif",
    "data/raw/T2_B08.tif",
    "data/processed/T2_NDVI.tif"
)

print("T2 NDVI created successfully.")
