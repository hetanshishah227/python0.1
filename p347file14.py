f1=open("abc","r")
f2=open("upperlower","w")
while True:
    ch=f1.read(1)
    if not ch:
        break
    if ch.isupper():
        f2.write(ch.lower())
    elif ch.islower():
        f2.write(ch.upper())
    else:
        f2.write(ch)
f1.close()
f2.close()
print("copied")

