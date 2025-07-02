t=float(input("Enter a temperature "))
if t<0:
    print("Freezing temperature")
elif 0 < t < 10:
    print(" Very cold atmosphere")

elif 10 < t < 20:
    print("Cold atmosphere")

elif 20 < t < 30:
    print("Normal Atmosphere")

elif 30 < t < 40:
    print("Hot atmosphere")

elif t > 40:
    print("Hot Atmosphere")
