sum = 0

for num in range(2, 1000):
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        sum = sum + num

print("Sum of all prime numbers below 1000 =", sum)