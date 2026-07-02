starts_with = lambda string, sub: string.startswith(sub)

string = input("Enter a string: ")
sub = input("Enter a substring: ")

if starts_with(string, sub):
    print("The string starts with the substring.")
else:
    print("The string does not start with the substring.")