import time
from datetime import datetime

def print_time() -> tuple[str, str]:
    epoch = time.time()
    text = f"Seconds since January 1, 1970: {epoch:,.4f} or {epoch:.2e} in scientific notation"
    time_str = datetime.now().strftime('%b %d %Y')
    return text, time_str

if __name__ == "__main__":
    delta, now = print_time()
    print(f"{delta}\n{now}")
