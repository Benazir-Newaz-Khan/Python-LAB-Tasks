def palindrome(string):
    if string == string[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

text = input("Enter a string: ")
palindrome(text)