import time
import datetime as dt
epoch = time.time()
text = f"Seconds since January 1, 1970: {epoch:,.4f} or {epoch:.2e} in scientific notation"
print(text)
print(dt.date.today().strftime("%b %d %Y"))
