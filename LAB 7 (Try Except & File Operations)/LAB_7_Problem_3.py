values = [10, 20, 30, 40, 50]

try:
    index = int(input("Enter the index: "))
    print(values[index])
except IndexError:
    print("Index is out of range")
except ValueError:
    print("Index must be an integer")
