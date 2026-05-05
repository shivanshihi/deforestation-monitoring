from patchify import patchify
import rasterio
import numpy as np

def create_patches(image_path):
    with rasterio.open(image_path) as src:
        img = src.read()
    
    patches = patchify(img, (img.shape[0], 256, 256), step=256)
    return patches
