from matplotlib import image as mpimg
import numpy as np

def ft_load(path: str) -> array:

    img = mpimg.imread(path)

    print(f"The shape of image is: {img.shape}")
