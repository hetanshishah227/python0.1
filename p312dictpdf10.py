marks = {
    "ram": 33,
    "rahul": 45
}
marks["devesh"]= 30
print(marks)

marks.setdefault("rita",12)
print(marks)

marks.setdefault("richa",)
marks["richa"]=102
print(marks)