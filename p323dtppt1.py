import time
current = time.localtime(time.time())

print('year:',current.tm_year)
print("month:",current.tm_mon)
print("date:",current.tm_year)
print("day:",current.tm_mday)
print("weekday:",current.tm_wday)
print("yearday:",current.tm_yday)
print("hour:",current.tm_hour)
print("minutes:",current.tm_min)
print("seconds:",current.tm_sec)