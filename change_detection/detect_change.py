import numpy as np

def detect_deforestation(mask_t1, mask_t2):
    return np.clip(mask_t1 - mask_t2, 0, 1)
