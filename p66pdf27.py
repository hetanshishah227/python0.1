yr=int(input("Enter the number of years you have served to this company="))
salary=int(input("Enter your salary="))

if yr>5:
    print("Congratulations!You've received a bonus of ",0.05*salary)
else:
    print("Thank you for serving this company for",yr,"years.")
