import numpy as np


def give_bmi(
    height: list[int | float], weight: list[int | float]
) -> list[int | float]:
    """
    Compute BMI for each height/weight pair.

    Parameters
    ----------
    height : list[int | float]
        List of heights (in meters).
    weight : list[int | float]
        List of weights (in kilograms).

    Returns
    -------
    list[int | float]
        BMI values (weight / height^2) for each pair.

    Raises
    ------
    AssertionError
        If lists have different sizes or contain non-numeric values.
    """
    if len(height) != len(weight):
        raise AssertionError("height and weight have not the same size")
    for h, w in zip(height, weight):
        if not isinstance(h, (int, float)) or isinstance(h, bool):
            raise AssertionError("height has a non-numeric value")
        if not isinstance(w, (int, float)) or isinstance(w, bool):
            raise AssertionError("weight has a non-numeric value")

    h_array = np.array(height)
    w_array = np.array(weight)
    bmi = w_array / h_array ** 2
    return bmi.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Return a boolean list indicating which BMI values exceed the limit.

    Parameters
    ----------
    bmi : list[int | float]
        List of BMI values.
    limit : int
        Numeric threshold to compare against.

    Returns
    -------
    list[bool]
        True for each BMI value strictly greater than limit.

    Raises
    ------
    AssertionError
        If bmi contains non-numeric values or limit is not an int.
    """
    for b in bmi:
        if not isinstance(b, (int, float)) or isinstance(b, bool):
            raise AssertionError("bmi has a non-numeric value")
        if not isinstance(limit, int) or isinstance(limit, bool):
            raise AssertionError("bmi has a non-numeric value")
    bmi = np.array(bmi)
    return (bmi > limit).tolist()
