#strftime

from datetime import datetime

now = datetime.now()#current date and time
#print(now)
year = now.strftime("%Y")
print("year:",year)

month = now.strftime("%m")
print("month:",month)

print("Full date and time:", now.strftime("%Y-%m-%d %H:%M:%S"))
print("Date (dd/mm/yyyy):", now.strftime("%d/%m/%Y"))
print("Date (mm-dd-yyyy):", now.strftime("%m-%d-%Y"))
print("Time (24-hour):", now.strftime("%H:%M:%S"))
print("Time (12-hour with AM/PM):", now.strftime("%I:%M:%S %p"))
print("Day of the week:", now.strftime("%A"))
print("Short day name:", now.strftime("%a"))
print("Month name:", now.strftime("%B"))
print("Short month name:", now.strftime("%b"))
print("Day of the month:", now.strftime("%d"))
print("Month number:", now.strftime("%m"))
print("Year (short):", now.strftime("%y"))
print("Year (full):", now.strftime("%Y"))