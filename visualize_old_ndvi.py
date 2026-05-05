import rasterio
import matplotlib.pyplot as plt

# Load NDVI image
with rasterio.open("data/processed/T_old_NDVI.tif") as src:
    ndvi = src.read(1)

# Display NDVI
plt.figure(figsize=(6,6))
plt.imshow(ndvi, cmap="RdYlGn")
plt.colorbar()
plt.title("Old NDVI Map")
plt.show()

# Print NDVI range
print("Minimum NDVI:", ndvi.min())
print("Maximum NDVI:", ndvi.max())