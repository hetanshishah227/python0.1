f1=open("abc","r")
while True:
    ch=f1.read(1)
    if not ch:
        break
    if ch.lower() not in "aeiou":
        print(ch,end="")
f1.close()
