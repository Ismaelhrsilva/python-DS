import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Print the shape of a 2D list, slice its rows from start to end
    and return the slice as a list, after printing its new shape.

    start and end must be int (bool is rejected) and family a list
    that converts to a 2D array (all rows with the same size).
    On invalid input, print the error and return an empty list.
    """
    try:
        assert isinstance(start, int) and not isinstance(start, bool), \
            "start is not an integer"
        assert isinstance(end, int) and not isinstance(end, bool), \
            "end is not an integer"
        assert isinstance(family, list), "family is not a list"

        family = np.array(family)
        assert family.ndim == 2, "family is not a valid 2D array"

        print(f"My shape is : {family.shape}")
        new = family[start:end]
        print(f"My new shape is : {new.shape}")
        return new.tolist()
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return []
    except ValueError:
        print("AssertionError: family rows must have the same size")
        return []
