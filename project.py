try:
    discount = int(input("Enter the discount in numbers:"))
    result = (55 - discount) 
except ValueError:
    print("Use numbers and nothing else!!")
except ZeroDivisionError:
    print("Cannot divide by 0!")
else:
    print("Please pay",result)