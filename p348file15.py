f1=open("abc","r")
f2=open("upper","w")
f3=open("lower","w")
while True:
    ch=f1.read(1)
    if not ch:
        break
    if ch.isupper():
        f2.write(ch)
    if ch.islower():
        f3.write(ch)
f1.close()
f2.close()
f3.close()
print("copied")
