def all_thing_is_obj(object: any) -> int:
    obj = type(object)
    name_obj = obj.__name__.capitalize()
    text = f"{name_obj} : {obj}"

    if name_obj in ("List", "Tuple", "Set", "Dict"):
        print(text)
    elif name_obj == "Str":
        print(f"{object} is in the kitchen : {obj}")
    else:
        print("Type not found")
    return 42


