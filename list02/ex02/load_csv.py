import pandas as pd


def load(path: str) -> pd.DataFrame | None:
    """
    Load a CSV file and return it as a pandas DataFrame.

    Prints the dimensions of the dataset as
    "Loading dataset of dimensions (rows, columns)".
    Returns None and prints the error if the file can't be loaded
    (bad path, bad format, empty dataset...).
    """
    try:
        df = pd.read_csv(path)
        if df.empty:
            raise AssertionError("Error at opening")
        print(f"Loading dataset of dimensions {df.shape}")
        return df
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        return None
