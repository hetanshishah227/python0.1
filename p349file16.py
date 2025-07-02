f1=open("abc","r")
f2=open("vowel","w")
f3=open("consonants","w")
while True:
    ch=f1.read(1)
    if not ch:
        break
    if ch.lower() in "aeiou":
        f2.write(ch)
    elif ch.lower() not in "aeiou":
        f3.write(ch)
    else:
        f2.write(ch)
        f3.write(ch)
f1.close()
f2.close()
f3.close()
print("copied")