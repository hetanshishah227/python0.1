try:
    n1=int(input("Enter a number=> "))
    n2=int(input("Enter another number=> "))
    c=n1/n2
    print("division of 2 numbers=>",c)
except ValueError:
    print("why u enter string")
except ZeroDivisionError:
    print("why u enter zero")
except:
    print("error")
finally:
   print("bye")

#in python there are 3 types of errors:
#syntax error22
#runtime error
#logical error