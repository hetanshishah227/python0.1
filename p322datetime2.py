import time
current = time.localtime(time.time())

d=current.tm_mday
m=current.tm_mon
y=current.tm_year

print(d,"/",m,"/",y)