import rasterio
import matplotlib.pyplot as plt

with rasterio.open("data/processed/T1_NDVI.tif") as src:
    ndvi = src.read(1)

plt.figure(figsize=(6,6))
plt.imshow(ndvi, cmap="RdYlGn")
plt.colorbar(label="NDVI Value")
plt.title("NDVI Map - T1")
plt.show()
