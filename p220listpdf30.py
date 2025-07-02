india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city = input("Enter a city name to know in which country it is loacated=> ").lower()

if city in india:
    print("It is located in India")
elif city in pakistan:
    print("It is located in Pakistan")
elif city in bangladesh:
    print("It is located in Bangladesh")
else:
    print("Enter one of these cities correctly=> mumbai, banglore, chennai, delhi, lahore, karachi, islamabad, dhaka, khulna, rangpur")

print("Enter 2 cities to know if they are located in the same country")
print("Enter one of these cities correctly=> mumbai, banglore, chennai, delhi, lahore, karachi, islamabad, dhaka, khulna, rangpur")
city1 = input("Enter the first city=> ").lower()
city2 = input("Enter the second city=> ").lower()

if city1 in india and city2 in india:
    print("Both in India")
elif city1 in pakistan and city2 in pakistan:
    print("Both in pakistan")
elif city1 in bangladesh and city2 in bangladesh:
    print("Both in bangladesh")
else:
    print("They do not belong to the same country")