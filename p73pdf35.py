sugar=int(input("Enter your fasting sugar level="))
if sugar < 80:
    print("Low sugar level")

elif 80 <= sugar <= 100:
    print("Normal sugar level")

else:
    print("High sugar level")
    