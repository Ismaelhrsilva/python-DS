from typing import Any
def all_thing_is_obj(object: Any) -> int:
    obj = type(object)

    if obj == str:
        print(f"{object} is in the kitchen : {obj}")
    elif obj in (list, tuple, set, dict):
        print(f"{obj.__name__.capitalize()} : {obj}")
    else:
        print("Type not found")
    return 42
