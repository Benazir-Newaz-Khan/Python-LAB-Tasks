numbers = [10, 20, 30, 20, 50]

new_list = []

for num in numbers:
    duplicate = False

    for item in new_list:
        if num == item:
            duplicate = True
            break

    if duplicate == False:
        new_list.append(num)

print(new_list)