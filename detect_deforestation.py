import rasterio
import numpy as np
import matplotlib.pyplot as plt

# Load masks
with rasterio.open("data/processed/T1_mask.tif") as src:
    mask_t1 = src.read(1)

with rasterio.open("data/processed/T2_mask.tif") as src:
    mask_t2 = src.read(1)

# Forest loss = was forest in T1, not forest in T2
deforestation = np.logical_and(mask_t1 == 1, mask_t2 == 0)

# Plot results
plt.figure(figsize=(12,4))

plt.subplot(1,3,1)
plt.title("Forest T1")
plt.imshow(mask_t1, cmap="gray")

plt.subplot(1,3,2)
plt.title("Forest T2")
plt.imshow(mask_t2, cmap="gray")

plt.subplot(1,3,3)
plt.title("Deforestation Areas")
plt.imshow(deforestation, cmap="Reds")

plt.show()
