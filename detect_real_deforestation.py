import rasterio
import numpy as np
import matplotlib.pyplot as plt

with rasterio.open("data/processed/T_old_mask.tif") as src:
    old_mask = src.read(1)

with rasterio.open("data/processed/T2_mask.tif") as src:
    new_mask = src.read(1)

# Forest loss
deforestation = np.logical_and(old_mask == 1, new_mask == 0)

# Forest gain (optional)
reforestation = np.logical_and(old_mask == 0, new_mask == 1)

plt.figure(figsize=(15,4))

plt.subplot(1,4,1)
plt.title("Old Forest")
plt.imshow(old_mask, cmap="gray")

plt.subplot(1,4,2)
plt.title("New Forest")
plt.imshow(new_mask, cmap="gray")

plt.subplot(1,4,3)
plt.title("Deforestation")
plt.imshow(deforestation, cmap="Reds")

plt.subplot(1,4,4)
plt.title("Reforestation")
plt.imshow(reforestation, cmap="Greens")

plt.show()
