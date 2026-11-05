from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def main():
    """
    Load animal.jpeg, cut a 400x400 grayscale square and transpose it.

    The transpose is done by hand (no library call). Prints the shape and
    pixels before and after the transpose, then displays the result.
    Any error is reported with a clear message instead of a traceback.
    """
    try:
        animal = ft_load("animal.jpeg")
        if animal.size == 0:
            return

        animal_zoom = animal[50:450, 450:850]
        animal_zoom = animal_zoom.mean(axis=2, keepdims=True).astype(np.uint8)
        print(f"The shape of image is: {animal_zoom.shape}")
        print(animal_zoom)

        animal_zoom = animal_zoom[:, :, 0]
        line, column = animal_zoom.shape
        animal_transposed = np.zeros((column, line), dtype=animal_zoom.dtype)
        for i in range(line):
            for j in range(column):
                animal_transposed[j, i] = animal_zoom[i, j]

        print(f"New shape after Transpose: {animal_transposed.shape}")
        print(animal_transposed)
        plt.imshow(animal_transposed, cmap="gray")
        plt.show()
    except KeyboardInterrupt:
        print("\nInterrupted by user")
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
