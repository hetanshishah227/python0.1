n=int(input("Enter limit=>"))
f=1
for i in range(1,n+1):
   f=f*i
   print(i,end=" x ")
print("\nFactorial =>",f)