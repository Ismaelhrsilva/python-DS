import sys


def filterstring(txt: str, number: int) -> list:
    """Return the words of txt whose length is greater than number.

    Arguments: txt as string, number as int
    """
    txt_list = txt.split()
    txt_filtered = [
        x for x in txt_list if (lambda word: len(word) > number)(x)
    ]
    return txt_filtered


def main():
    """Read a string and an integer from sys.argv and print the filtered words.

    Prints an AssertionError if the arguments are bad.
    """
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        number = int(sys.argv[2])
        words = filterstring(sys.argv[1], number)
        print(words)
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except ValueError:
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
