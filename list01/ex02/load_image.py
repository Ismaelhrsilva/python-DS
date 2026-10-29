import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """
    Load a JPG/JPEG image, print its shape and return its RGB pixels.

    The image is converted to RGB, so the returned array always has
    shape (height, width, 3) with uint8 values. On any error a clear
    message is printed and an empty array is returned.
    """
    try:
        assert isinstance(path, str), "path is not a string"

        img = Image.open(path)
        assert img.format == "JPEG", "image is not JPG/JPEG"

        img_array = np.array(img.convert("RGB"))
        print(f"The shape of image is: {img_array.shape}")
        return img_array
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        return np.array([])
