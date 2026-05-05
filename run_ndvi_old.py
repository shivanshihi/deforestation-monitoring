from ndvi import compute_ndvi

compute_ndvi(
    "data/raw/T_old_B04.tif",
    "data/raw/T_old_B08.tif",
    "data/processed/T_old_NDVI.tif"
)

print("Old NDVI created successfully.")
