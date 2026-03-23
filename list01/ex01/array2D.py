import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Slice a 2D list by row range and return the result as a list.

    Parameters
    ----------
    family : list
        A 2D list (list of lists) to be sliced.
    start : int
        Start row index (inclusive).
    end : int
        End row index (exclusive). Supports negative indices.

    Returns
    -------
    list
        Sliced rows as a Python list. Returns [] if family has
        inconsistent row sizes.

    Raises
    ------
    AssertionError
        If family is not a list or start/end are not integers.
    """
    if not isinstance(start, int) or isinstance(start, bool):
        raise AssertionError("start in not an integer")
    if not isinstance(end, int) or isinstance(end, bool):
        raise AssertionError("end in not an integer")
    if not isinstance(family, list):
        raise AssertionError("family in not a list")

    try:
        family_array = np.array(family)
        new_family_array = family_array[start:end]
    except ValueError as e:
        print(f"Error: {e}")
        return []

    print(f"My shape is : {family_array.shape}")
    print(f"My new shape is : {new_family_array.shape}")
    return new_family_array.tolist()
