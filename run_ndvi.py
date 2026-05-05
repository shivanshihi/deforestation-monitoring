from ndvi import compute_ndvi

compute_ndvi(
    "data/raw/T1_B04.tif",
    "data/raw/T1_B08.tif",
    "data/processed/T1_NDVI.tif"
)

print("NDVI created successfully.")
