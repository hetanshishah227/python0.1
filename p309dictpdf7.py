marks = {
    "ram": 33,
    "rahul": 15,
    "devesh": 30,
    "jayul": 34,
    "jiya": 16,
    "sadhana": 11,
    "meena": 19
}
print(marks)
n = input("enter a key to delete=>").lower()
marks.pop(n) #or del marks[n]
print(marks)