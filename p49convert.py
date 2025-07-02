ch=input("Enter character=")
if ch.islower():
    print(ch.upper())
elif ch.isupper():
    print(ch.lower())
else:
    print("ch=",ch)
    