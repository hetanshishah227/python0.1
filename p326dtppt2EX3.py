#exercise3
import time

current = time.localtime(time.time())
h = current.tm_hour
if 24 <= h <= 12:
 print(h,"AM")
else:
 print(h-12,"PM")
