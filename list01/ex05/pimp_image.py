import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array: np.ndarray) -> np.ndarray:
    """Inverts the color of the image received."""
    array_modified = 255 - array
    plt.imshow(array_modified)
    plt.title("Invert")
    plt.show()
    return array_modified


def ft_red(array: np.ndarray) -> np.ndarray:
    """Keeps only the red channel of the image received."""
    array_modified = array.copy()
    array_modified[:, :, 1] = 0
    array_modified[:, :, 2] = 0
    plt.imshow(array_modified)
    plt.title("Red")
    plt.show()
    return array_modified


def ft_green(array: np.ndarray) -> np.ndarray:
    """Keeps only the green channel of the image received."""
    array_modified = array.copy()
    array_modified[:, :, 0] = 0
    array_modified[:, :, 2] = 0
    plt.imshow(array_modified)
    plt.title("Green")
    plt.show()
    return array_modified


def ft_blue(array: np.ndarray) -> np.ndarray:
    """Keeps only the blue channel of the image received."""
    array_modified = array.copy()
    array_modified[:, :, 0] = 0
    array_modified[:, :, 1] = 0
    plt.imshow(array_modified)
    plt.title("Blue")
    plt.show()
    return array_modified


def ft_grey(array: np.ndarray) -> np.ndarray:
    """Converts the image received to grey, keeping its shape."""
    array_modified = array.copy()
    grey = np.sum(array, axis=2) / 3
    array_modified[:, :, 0] = grey
    array_modified[:, :, 1] = grey
    array_modified[:, :, 2] = grey
    plt.imshow(array_modified)
    plt.title("Grey")
    plt.show()
    return array_modified
