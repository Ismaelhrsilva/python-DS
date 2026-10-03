from typing import Any

def NULL_not_found(object: Any) -> int:
    obj = type(object)

    if object is None:
        print(f"Nothing: {object} {obj}")
    elif isinstance(object, float) and not (object==object):
        print(f"Cheese: {object} {obj}")
    elif isinstance(object, str) and object == "":
        print(f"Empty: {object} {obj}")
    elif isinstance(object, bool) and object is False:
        print(f"Fake: {object} {obj}")
    elif isinstance(object, int) and object == 0:
        print(f"Zero: {object} {obj}")
    else:
        print("Type not Found")
        return 1
    return 0

