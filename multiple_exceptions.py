try:
    num1, num2 = eval(input("Enter two number separated by a comma: "))
    result = num1/num2
    print(result)

except ZeroDivisionError:
    print("Cannot divide by 0!!")

except SyntaxError:
    print("No comma!!")

except:
    print("Wrong input!!")

else:
    print("No exceptions")

finally:
    print("This will run everytime")
