#exercise 1
import time

current = time.localtime(time.time())
y = current.tm_year
if y%4==0:
    print("leap year")
else:
    print("not a leap year")
