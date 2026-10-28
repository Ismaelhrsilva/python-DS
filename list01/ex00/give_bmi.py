import numpy as np


def give_bmi(
    height: list[int | float], weight: list[int | float]
) -> list[int | float]:
    """
    Compute the BMI (weight / height ** 2) for each height/weight pair.

    Both lists must contain only int or float values (bool is rejected),
    have the same size and contain only values greater than zero.
    On invalid input, print the error and return an empty list.
    """
    try:
        assert isinstance(height, list), "height is not a list"
        assert isinstance(weight, list), "weight is not a list"
        assert all(
            isinstance(x, (int, float)) and not isinstance(x, bool)
            for x in height
        ), "height must contain only int or float"
        assert all(
            isinstance(x, (int, float)) and not isinstance(x, bool)
            for x in weight
        ), "weight must contain only int or float"
        assert len(height) == len(weight), \
            "height and weight must have the same size"
        assert all(h > 0 for h in height), \
            "height contains a value lower or equal to zero"
        assert all(w > 0 for w in weight), \
            "weight contains a value lower or equal to zero"

        height_array = np.array(height)
        weight_array = np.array(weight)
        bmi = weight_array / height_array ** 2

        return bmi.tolist()
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Return a list of booleans: True where the BMI is above the limit.

    bmi must be a non-empty list of positive int or float values and
    limit a positive int (bool is rejected in both).
    On invalid input, print the error and return an empty list.
    """
    try:
        assert isinstance(bmi, list), "bmi is not a list"
        assert all(
            isinstance(x, (int, float)) and not isinstance(x, bool)
            for x in bmi
        ), "bmi must contain only int or float"
        assert len(bmi) > 0, "bmi is empty"
        assert all(b > 0 for b in bmi), \
            "bmi contains a value lower or equal to zero"
        assert isinstance(limit, int) and not isinstance(limit, bool), \
            "limit is not an integer"
        assert limit > 0, "limit is lower or equal to zero"

        bmi_array = np.array(bmi)
        return (bmi_array > limit).tolist()
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return []
