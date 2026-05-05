import rasterio
import numpy as np

def compute_ndvi(red_path, nir_path, output_path):
    with rasterio.open(red_path) as red:
        red_band = red.read(1).astype(float)
        profile = red.profile

    with rasterio.open(nir_path) as nir:
        nir_band = nir.read(1).astype(float)

    ndvi = (nir_band - red_band) / (nir_band + red_band + 1e-8)
    ndvi = np.clip(ndvi, -1, 1)

    profile.update(dtype=rasterio.float32)

    with rasterio.open(output_path, 'w', **profile) as dst:
        dst.write(ndvi.astype(rasterio.float32), 1)
