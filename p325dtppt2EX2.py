#exercise2
import time

current = time.localtime(time.time())
h =current.tm_hour
if 4 <= h <= 12:
    print("good morning")
elif 12 < h < 16:
    print("good afternoon")
elif 16 <= h <= 20:
    print("good evening")
elif 20 < h < 4:
    print("good night")
