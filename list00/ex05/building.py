import sys


def main():
    """
    Count character dict_count in a string and display a summary.

    Usage:
        python building.py "text to analyze"
        python building.py  (prompts for input, finish with Ctrl+D)

    Raises:
        AssertionError: if more than one argument is provided.

    Output example:
        The text contains 171 characters:
        2 upper letters
        121 lower letters
        2 punctuation marks
        20 spaces
        15 digits
    """
    if len(sys.argv) == 1:
        print("What is the text to count?")
        text = sys.stdin.read()
    else:
        try:
            assert len(sys.argv) == 2, "more than one argument is provided"
        except AssertionError as e:
            print(f"AssertionError: {e}")
            return
        text = sys.argv[1]

    dict_count = {}
    for i in text:
        if i.isupper():
            dict_count['upper'] = dict_count.get("upper", 0) + 1
        elif i.islower():
            dict_count['lower'] = dict_count.get("lower", 0) + 1
        elif i.isspace():
            dict_count['space'] = dict_count.get("space", 0) + 1
        elif i.isdigit():
            dict_count['digit'] = dict_count.get("digit", 0) + 1
        elif not i.isalnum():
            dict_count['punctuation'] = dict_count.get("punctuation", 0) + 1

    print(f"The text contains {len(text)} characters:")
    print(f"{dict_count.get('upper', 0)} upper letters")
    print(f"{dict_count.get('lower', 0)} lower letters")
    print(f"{dict_count.get('punctuation', 0)} punctuation marks")
    print(f"{dict_count.get('space', 0)} spaces")
    print(f"{dict_count.get('digit', 0)} digits")


if __name__ == "__main__":
    main()
