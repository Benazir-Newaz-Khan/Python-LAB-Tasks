import os

try:
    directory = input("Enter the directory: ")
    filename = input("Enter the file name: ")
    path = os.path.join(directory, filename)

    with open(path, "w") as file:
        file.write("Hello Python\n")

    with open(path, "a") as file:
        file.write("This line was appended.\n")

    with open(path, "r") as file:
        print(file.read())

    created_path = os.path.join(directory, "created_file.txt")
    with open(created_path, "x") as file:
        file.write("Created using x mode.")

    print("Files created successfully.")
except FileExistsError:
    print("The file already exists.")
except Exception as e:
    print("Error:", e)
