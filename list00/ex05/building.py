import sys






def main():
    print("What is the text to count?")
    txt = sys.argv[1]
    print(txt)
    count_dict = {"upper": 0, "lower": 0, "ponct": 0, "digits": 0, "spaces": 0}
    for l in txt:
        if l.isupper():
            count_dict["upper"] = count_dict["upper"] + 1
        if l.islower():
            count_dict["lower"] = count_dict["lower"] + 1
    print(count_dict["upper"])
    print(count_dict["lower"])


if __name__ == "__main__":
    main()
