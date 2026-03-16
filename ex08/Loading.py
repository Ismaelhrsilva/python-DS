import os


def ft_tqdm(lst: range) -> None:
    """Display a progress bar while iterating over a range.

    A lightweight reimplementation of tqdm that prints an updating
    progress bar to the terminal, showing percentage, iteration count,
    elapsed time, ETA and iteration rate.
    Adapts the bar width to the current terminal size.

    Args:
        lst: The range (or any sized iterable) to iterate over.

    Yields:
        Each element from lst, one at a time.
    """
    total = len(lst)
    start = os.times()[4]

    for i, n in enumerate(lst):
        frac = i / total
        pct = int(frac * 100)
        elapsed = os.times()[4] - start
        rate = i / elapsed if elapsed > 0 else 0
        eta = (elapsed / i) * (total - i) if i > 0 else 0
        m_el, s_el = divmod(int(elapsed), 60)
        m_eta, s_eta = divmod(int(eta), 60)
        try:
            cols = os.get_terminal_size().columns
        except OSError:
            cols = 80
        left = f"{pct:3d}%| ["
        right = (f"]| {i}/{total}"
                 f" [{m_el:02d}:{s_el:02d}<{m_eta:02d}:{s_eta:02d},"
                 f" {rate:.2f}it/s]")
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

    elapsed = os.times()[4] - start
    rate = total / elapsed if elapsed > 0 else 0
    m_el, s_el = divmod(int(elapsed), 60)
    try:
        cols = os.get_terminal_size().columns
    except OSError:
        cols = 80
    left = "100%| ["
    right = f"]| {total}/{total} [{m_el:02d}:{s_el:02d}<00:00, {rate:.2f}it/s]"
    bar_width = max(1, cols - len(left) - len(right))
    bar = "=" * (bar_width - 1) + ">"
    print("\r" + left + bar + right)
