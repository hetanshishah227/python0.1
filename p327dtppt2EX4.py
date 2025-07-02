import time
current = time.localtime(time.time())
h = current.tm_hour
m = current.tm_min
s = current.tm_sec
if 24 == h and 00 == m and 00 == s:
    print(h-12,":",m,":",s," am")
if 24 < h < 12:
    print(h,":",m,":",s," am")
if 12 == h and m >= 00 and s >= 00:
    print(h,":",m,":",s," pm")
if 13 <= h < 24:
    print(h-12,":",m,":",s," pm")

