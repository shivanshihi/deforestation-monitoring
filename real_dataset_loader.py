import numpy as np
import os

def load_real_data():

    image_dir = "data/patches/images"
    mask_dir = "data/patches/masks"

    images = []
    masks = []

    for filename in os.listdir(image_dir):
        img = np.load(os.path.join(image_dir, filename))
        mask = np.load(os.path.join(mask_dir, filename.replace("img", "mask")))

        images.append(img)
        masks.append(mask)

    X = np.array(images).astype(np.float32)
    y = np.array(masks).astype(np.float32)

    # Normalize NDVI
    X = (X - X.min()) / (X.max() - X.min())

    # Expand dims
    X = np.expand_dims(X, axis=-1)
    y = np.expand_dims(y, axis=-1)

    return X, y
