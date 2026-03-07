import sys

def main():
    if (len(sys.argv) == 1):
        return
    if (len(sys.argv) > 2):
        print("AssertionError: more than one argument is provided")
        return
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("AssertionError: argument is not an integer")
        return
    print("I'm Even.") if n % 2 == 0 else print("I'm Odd.")


if __name__ == "__main__":
    main()
