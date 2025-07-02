light=input("Enter the traffic light color=").lower()\

if light=="red":
    print("Car has to stop")

elif light=="yellow":
    print("Car has to wait")

elif light=="green":
    print("Car is allowed to go")

else:
    print("Unrecognized light")
