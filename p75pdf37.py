bmi=float(input("Enter your BMI-"))

if bmi < 18.5:
    print("Underweight")

elif 18.5 <= bmi <= 24.9:
    print("Normal")

elif 25 <= bmi <= 29.9:
    print("Overweight")

else:
    print("Obese")