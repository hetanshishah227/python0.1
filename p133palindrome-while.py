#palindrome number--A palindrome number is a number that reads the same backward as forward.
#21 → reversed is 121
#1331 → reversed is 1331
#12321 → reversed is 12321

reverse_num = 0
num = int(input("Enter a number to check if it is palindrome=>"))
c=num
while num > 0:

    digit = num % 10
    reverse_num = reverse_num * 10 + digit
    num = num // 10

print("The reverse of the entered number is=>",reverse_num," \nnum = ",c)

if reverse_num == c:
    print("It is palindrome")
else:
    print("It is not palindrome")