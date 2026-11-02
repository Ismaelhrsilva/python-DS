from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def ft_zoom():
    """
    Load animal.jpeg, zoom on a 400x400 area in grayscale and display it.

    Prints the original image, the new shape and the zoomed pixels.
    Any error is reported with a clear message instead of a traceback.
    """
    try:
        img = ft_load("animal.jpeg")
        if img.size == 0:
            return

        print(img)
        zoom = img[50:450, 450:850]
        zoom = zoom.mean(axis=2, keepdims=True).astype(np.uint8)
        print(f"New shape after slicing: {zoom.shape}")
        print(zoom)

        plt.imshow(zoom, cmap="gray")
        plt.show()
    except KeyboardInterrupt:
        print("\nInterrupted by user")
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    ft_zoom()
