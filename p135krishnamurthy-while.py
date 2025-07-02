#A Krishnamurthy number (also known as a Strong number or Peterson number) is a number that is equal to
# the sum of the factorials of its digits.
#145= 1! + 4! + 5! = 1 + 24 + 120 = 145
# 1! = 1 , 2! = 2
#1!+2!+3!=1+2+6=9 != 123(not krishnamurthy number)

num = int(input("Enter a number to check if it is a krishnamurthy number=>"))
reverse_num = 0
c = num

while num > 0:
    digit = num % 10
    f=1
    for i in range(digit,1,-1):
        f=f*i

    reverse_num = reverse_num + f
    num = num // 10

if reverse_num == c:
    print("It is a krishnamurthy number")

else:
    print("It is not a krishnamurthy number")

