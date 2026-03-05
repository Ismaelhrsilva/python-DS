from datetime import datetime

time_now  = datetime.now()
time_base = datetime(1970,1,1)
delta_time = time_now - time_base
delta_time_seconds = delta_time.total_seconds()


print(f"Seconds since January 1, 1970: {delta_time_seconds:,.4f} or {delta_time_seconds:.2e} in scientific notation")
print(time_now.strftime('%b %-d %Y'))
