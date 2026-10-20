import sys


def main():
    """Encode a string argument into Morse Code and print it."""
    MORSE = {
        " ": "/ ",
        "A": ".- ",
        "B": "-... ",
        "C": "-.-. ",
        "D": "-.. ",
        "E": ". ",
        "F": "..-. ",
        "G": "--. ",
        "H": ".... ",
        "I": ".. ",
        "J": ".--- ",
        "K": "-.- ",
        "L": ".-.. ",
        "M": "-- ",
        "N": "-. ",
        "O": "--- ",
        "P": ".--. ",
        "Q": "--.- ",
        "R": ".-. ",
        "S": "... ",
        "T": "- ",
        "U": "..- ",
        "V": "...- ",
        "W": ".-- ",
        "X": "-..- ",
        "Y": "-.-- ",
        "Z": "--.. ",
        "0": "----- ",
        "1": ".---- ",
        "2": "..--- ",
        "3": "...-- ",
        "4": "....- ",
        "5": "..... ",
        "6": "-.... ",
        "7": "--... ",
        "8": "---.. ",
        "9": "----. ",
    }

    try:
        assert len(sys.argv) == 2, "the arguments are bad"
        text = sys.argv[1]
        text_morse = []
        for letter in text:
            assert letter.upper() in MORSE, "the arguments are bad"
            text_morse.append(MORSE[letter.upper()])
        print("".join(text_morse).rstrip())

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
