import rasterio
import matplotlib.pyplot as plt

with rasterio.open("data/processed/T1_mask.tif") as src:
    mask = src.read(1)

plt.imshow(mask, cmap="gray")
plt.title("Forest Mask")
plt.show()
