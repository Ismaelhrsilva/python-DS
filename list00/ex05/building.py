import sys

def main():
    if len(sys.argv) == 1:
        txt = input("What is the text to count?\n")
    else:
        txt = sys.argv[1]
    count_dict = {"upper": 0, "lower": 0, "ponct": 0, "digits": 0, "spaces": 0}
    for l in txt:
        if l.isupper():
            count_dict["upper"] += 1
        elif l.islower():
            count_dict["lower"] += 1
        elif l.isdigit():
            count_dict["digits"] += 1
        elif l.isspace():
            count_dict["spaces"] += 1
        elif not l.isalnum() and not l.isspace():
            count_dict["ponct"] += 1

    print(f'The text contains {sum(count_dict.values())} characters:')
    print(f'{count_dict["upper"]} upper letters')
    print(f'{count_dict["lower"]} lower letters')
    print(f'{count_dict["ponct"]} punctuation  marks')
    print(f'{count_dict["spaces"]} spaces')
    print(f'{count_dict["digits"]} digits')


if __name__ == "__main__":
    main()
