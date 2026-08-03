import pandas as pd


def load(path: str) -> pd.DataFrame | None:
    """
    Load a CSV file and return it as a pandas DataFrame.

    Prints the dimensions of the dataset in the form
    "Loading dataset of dimensions (rows, columns)" before returning it.

    Parameters
    ----------
    path : str
        Filesystem path to the CSV file to load.

    Returns
    -------
    pandas.DataFrame or None
        The loaded dataset, or None if it cannot be read (bad path, bad
        format, ...). Every error is caught and reported with a clear
        message instead of raising.
    """
    # TODO: read the CSV, print its dimensions and return the DataFrame.
    #       Catch every exception, print a clear message, return None.
    return None
