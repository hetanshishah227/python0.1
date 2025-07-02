f1=open("abc","r")
c=0
while True:
    ch=f1.read(1)
    if not ch:
        break
    if ch=="a" or "e" or "i" or "u" or "A" or "E" or "I" or "U":
        c+=1
f1.close()
print("vowel count=>",c)
