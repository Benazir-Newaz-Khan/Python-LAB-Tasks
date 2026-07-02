def count_elements(list1):
    count = {}

    for item in list1:
        if item in count:
            count[item] = count[item] + 1
        else:
            count[item] = 1

    for key in count:
        print(key, "=>", count[key])

numbers = [10, 20, 30, 30, 30, 30, 20, 40]

count_elements(numbers)