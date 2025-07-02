f1=open("abc","r")
f2=open("pqr","w")
while True:
    ch=f1.read(1)
    if not ch:
        break
    f2.write(ch)
f1.close()
f2.close()
print("Copied")

"""
1) 1->2 copy space X
2) 1->2 copy vowel X
3) 1->2 copy upper , lower , lower upper
4) 1->2 upper
    ->3 lower
    
5) 1->2 vowel
    ->other


"""