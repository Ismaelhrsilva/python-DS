import os


def ft_tqdm(lst: range) -> None:
    """Display a progress bar while iterating over a range.

    A lightweight reimplementation of tqdm that prints an updating
    progress bar to the terminal, showing percentage and iteration count.
    Adapts the bar width to the current terminal size.

    Args:
        lst: The range (or any sized iterable) to iterate over.

    Yields:
        Each element from lst, one at a time.
    """
    total = len(lst)

    for i, n in enumerate(lst):
        frac = i / total
        pct = int(frac * 100)
        try:
            cols = os.get_terminal_size().columns
        except OSError:
            cols = 80
        left = f"{pct:3d}%| ["
        right = f"]| {i}/{total}"
        bar_width = max(1, cols - len(left) - len(right))
        filled = int(bar_width * frac)
        if filled == 0:
            bar = " " * bar_width
        elif filled < bar_width:
            bar = "=" * (filled - 1) + ">" + " " * (bar_width - filled)
        else:
            bar = "=" * bar_width
        print("\r" + left + bar + right, end="", flush=True)
        yield n

    try:
        cols = os.get_terminal_size().columns
    except OSError:
        cols = 80
    left = "100%| ["
    right = f"]| {total}/{total}"
    bar_width = max(1, cols - len(left) - len(right))
    bar = "=" * (bar_width - 1) + ">"
    print("\r" + left + bar + right)
