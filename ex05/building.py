import sys
#atenção! tem novas regras para esse exercício.

def main():
    if len(sys.argv) == 1:
        print("What is the text to count?")
        text = sys.stdin.read()
    elif len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
        return
    else:
        text = sys.argv[1]

    dict_count = {
        'upper': 0,
        'lower':0,
        'space':0,
        'digit':0,
        'punctuation':0}

    for i in text:
        if i.isupper():
            dict_count['upper'] += 1
        elif i.islower():
            dict_count['lower'] += 1
        elif i.isspace():
            dict_count['space'] += 1
        elif i.isdigit():
            dict_count['digit'] += 1
        elif not i.isalnum():
            dict_count['punctuation'] += 1

    print(f"The text contains {sum(dict_count.values())} characters:")
    print(f"{dict_count['upper']} upper letters")
    print(f"{dict_count['lower']} lower letters")
    print(f"{dict_count['punctuation']} punctuation marks")
    print(f"{dict_count['space']} spaces")
    print(f"{dict_count['digit']} digits")


if __name__ == "__main__":
    main()
