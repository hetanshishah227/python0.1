f1=open("abc","r")
f2=open("spacex","w")
while True:
    ch=f1.read(1)
    if not ch:
        break
    if ch==" ":
        pass
    else:
        f2.write(ch)
f1.close()
f2.close()
print("space not copied")