numbers = []

n = int(input("Enter the number of elements: "))

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

search = int(input("Enter the value to search: "))

found = False

for i in range(len(numbers)):
    if numbers[i] == search:
        print("Value found at index", i)
        found = True
        break

if found == False:
    print("Value not found.")