import sys

if len(sys.argv) > 2:
    print("AssertionError: more than one argument is provided")
elif len(sys.argv) == 1:
    pass
else:
    try:
        number = int(sys.argv[1])

        if number % 2 ==  0:
            print("I'm Even.")
        elif number % 2 == 1:
            print("I'm Odd.")
    except ValueError:
        print("AssertionError: argument is not an integer")
