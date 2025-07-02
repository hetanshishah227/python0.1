reverse_num = 0
num = int(input("Enter a number to check the sum of its digits=>"))

while num > 0:

    digit = num % 10
    reverse_num = reverse_num + digit
    num = num // 10

print(reverse_num)


