age=int(input("Enter your age="))

if age > 40 or age < 18:
    print("Not eligible to work")
else:
    gender = input("Enter your gender(M or F)").lower()
    days = int(input("Enter the number of days you've worked-"))
    if gender=="m":
        if 18 <= age < 30:
            print("Your wage per day is 70\nYour total wage earned is", 700 * days)
        elif 30 <= age <= 40 and gender=="m":
            print("Your wage per day is 800 \nYour total wage earned is", 800*days)


    elif gender=="f":
        if 18 <= age < 30:
          print("Your wage per day is 750\nYour total wage earned is",750*days)

        elif 30 <= age <= 40 and gender=="f":
          print("Your wage per day is 800\nYour total wage earned is", 850*days)


""" direct print after age input , bring output print to next line"""





