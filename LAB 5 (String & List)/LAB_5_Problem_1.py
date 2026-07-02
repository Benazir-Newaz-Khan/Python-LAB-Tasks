string = input("Enter a string: ")

words = string.split()

for word in words:
    reverse = ""

    for i in range(len(word) - 1, -1, -1):
        reverse = reverse + word[i]

    print(reverse, end=" ")