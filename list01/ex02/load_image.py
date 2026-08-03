import os

import numpy as np
from matplotlib import image as mpimg


def ft_load(path: str) -> np.ndarray | None:
    """
    Load an image from disk, print its shape and return its pixels.

    Reads the image located at `path` with matplotlib.image.imread and
    prints the shape of the resulting array. JPG and JPEG images are
    loaded as uint8 arrays of shape (H, W, 3) in RGB format.

    Parameters
    ----------
    path : str
        Filesystem path to the image to load.

    Returns
    -------
    numpy.ndarray or None
        The image data as a NumPy array, or None if the image could not
        be loaded. Every error is caught and reported with a clear
        message instead of raising.
    """
    try:
        if not isinstance(path, str):
            raise TypeError(f"path must be a str, not {type(path).__name__}")
        if not os.path.isfile(path):
            raise FileNotFoundError(f"no such file: {path}")

        image = mpimg.imread(path)
        print(f"The shape of image is: {image.shape}")
        return image
    except Exception as error:
        print(f"{type(error).__name__}: {error}")
        return None
