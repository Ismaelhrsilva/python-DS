import os


def _get_cols() -> int:
    """Return terminal width in columns, defaulting to 80 on failure."""
    try:
        return os.get_terminal_size().columns
    except OSError:
        return 80


def _build_bar(frac: float, bar_width: int) -> str:
    """Build a progress bar string of given width at the given fraction."""
    filled = int(bar_width * frac)
    if filled == 0:
        return " " * bar_width
    if filled < bar_width:
        return "=" * (filled - 1) + ">" + " " * (bar_width - filled)
    return "=" * (bar_width - 1) + ">"


def _format_time(seconds: float) -> str:
    """Convert seconds to MM:SS string format."""
    m, s = divmod(int(seconds), 60)
    return f"{m:02d}:{s:02d}"


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
        elapsed = os.times()[4] - start
        rate = i / elapsed if elapsed > 0 else 0
        eta = (elapsed / i) * (total - i) if i > 0 else 0
        left = f"{int(frac * 100):3d}%| ["
        right = (f"]| {i}/{total}"
                 f" [{_format_time(elapsed)}<{_format_time(eta)},"
                 f" {rate:.2f}it/s]")
        bar_width = max(1, _get_cols() - len(left) - len(right))
        print("\r" + left + _build_bar(frac, bar_width) + right,
              end="", flush=True)
        yield n

    elapsed = os.times()[4] - start
    rate = total / elapsed if elapsed > 0 else 0
    left = "100%| ["
    right = (f"]| {total}/{total}"
             f" [{_format_time(elapsed)}<00:00, {rate:.2f}it/s]")
    bar_width = max(1, _get_cols() - len(left) - len(right))
    print("\r" + left + _build_bar(1.0, bar_width) + right)
