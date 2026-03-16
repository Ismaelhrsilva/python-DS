def count_in_list(lst: list, obj: object) -> int:
    """
    Counts the occurrences of a item in a list.

    Args:
        lst (list): The list that we going to count the occurrences.
        obj (object): The thing we want to count.

    Return:
        int: the number of occurrences that obj show up in the lst
    """
    
    return sum(1 for x in lst if x == obj)
