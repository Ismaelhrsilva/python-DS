import sys


def main():
    """Count the character types of a text and print a summary.

    The text comes from the single command-line argument. If no argument
    is given, the user is prompted to type it; the Enter key is counted
    as a space, and Ctrl+D ends the input without one.

    Counts upper-case letters, lower-case letters, punctuation marks,
    spaces and digits.

    Prints an AssertionError if more than one argument is provided.
    Ctrl+C exits cleanly, without a traceback.
    """
    try:
        assert len(sys.argv) < 3, "more than one argument is provided"
        if len(sys.argv) == 1:
            print("What is the text to count?")
            txt = sys.stdin.readline()
        else:
            txt = sys.argv[1]
        count_dict = {"upper": 0,
                      "lower": 0,
                      "ponct": 0,
                      "digits": 0,
                      "spaces": 0}
        for char in txt:
            if char.isupper():
                count_dict["upper"] += 1
            elif char.islower():
                count_dict["lower"] += 1
            elif char.isdigit():
                count_dict["digits"] += 1
            elif char.isspace():
                count_dict["spaces"] += 1
            elif not char.isalnum():
                count_dict["ponct"] += 1

        print(f'The text contains {sum(count_dict.values())} characters:')
        print(f'{count_dict["upper"]} upper letters')
        print(f'{count_dict["lower"]} lower letters')
        print(f'{count_dict["ponct"]} punctuation marks')
        print(f'{count_dict["spaces"]} spaces')
        print(f'{count_dict["digits"]} digits')
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except KeyboardInterrupt:
        print()


if __name__ == "__main__":
    main()
