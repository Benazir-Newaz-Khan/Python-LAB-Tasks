try:
    number = float(input("Enter a number: "))
    print(number / 0)
except ZeroDivisionError:
    print("Cannot divide by zero")
