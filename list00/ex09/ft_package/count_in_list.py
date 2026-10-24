def count_in_list(items: list, target) -> int:
    """Return how many times target appears in items."""
    count = 0
    for item in items:
        if item == target:
            count += 1
    return count
