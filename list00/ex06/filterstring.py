import sys
from ft_filter import ft_filter


def validate_args() -> tuple[str, int]:
    """
    validate the arguments pass through the command line.
    Accepts 2 arguments and only if the second is an integer.
    Return:
            (string, integer) and raise AssertionError if is incorrect.
    """
    assert len(sys.argv) == 3
    assert not sys.argv[1].lstrip('-').isdigit()
    return sys.argv[1], int(sys.argv[2])


def main():
    """
        Filter words that have len greater than asked

        Args:
            string: word to be analysed
            int: len required
        Returns:
            list of words int string that has len greater than asked
    """
    try:
        text, number = validate_args()
    except (AssertionError, ValueError):
        print("AssertionError: the arguments are bad")
        return
    words = text.split(" ")
    words_acceptable = list(ft_filter(lambda w: len(w) > number, words))
    print(words_acceptable)


if __name__ == "__main__":
    main()
