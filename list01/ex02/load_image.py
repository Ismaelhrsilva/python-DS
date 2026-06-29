import os

import numpy as np
from matplotlib import image as mpimg


def ft_load(path: str) -> np.ndarray:
    if not os.path.exists(path):
        raise FileNotFoundError(f"Image not found: {path}")

    image = np.empty(0)
    try:
        image = mpimg.imread(path)
        print(f"The shape of image is: {image.shape}")
        print(image)
    except Exception:
        raise

    return image
