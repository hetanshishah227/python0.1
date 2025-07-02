f1=open("abc","r")
c1=0
c2=0
while True:
    ch=f1.read(1)
    if not ch:
        break
    if ch.isupper():
        c1+=1
    if ch.islower():
        c2+=1
f1.close()
print("upper letter count=>",c1)
print("lower letter count=>",c2)