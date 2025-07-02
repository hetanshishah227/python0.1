n=int(input("Enter limit =>"))
f=1
i=1
while i<=n:
    print(i,end=" X ")
    i=i+1
    f=f*i
print("\nfactorial is=",f)