try:
    age_1= int(input("enter the age"))
    print(age_1)
    c=age_1/0
except(ValueError):
    print("age cannot be a string")
except(ZeroDivisionError):
    print("division by zero is not possible")
    
