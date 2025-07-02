#An Armstrong number (also known as a narcissistic number, pluperfect digital invariant (PPDI),
# or pluperfect number) is a number that is equal to the sum of its own digits each raised to
# the power of the number of digits.
# 1,2,3,...9= 1^1=1,
#              9^1=9
#153 is an Armstrong number:
#It has 3 digits---1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153

reverse_num = 0
num = int(input("Enter a number to check if it is armstrong=>"))
c = num
while num > 0:

    digit = num % 10
    reverse_num = reverse_num + digit * digit * digit
    num = num // 10

if reverse_num == c:
    print("The entered number is armstrong")
else:
    print("The entered number is not armstrong")
