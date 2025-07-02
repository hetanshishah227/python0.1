my_list = [3, 5, 8, 11, 110, 34, 111]
largest = my_list[0]
for num in my_list:
    if num > largest:
        largest = num
        print(largest)
    