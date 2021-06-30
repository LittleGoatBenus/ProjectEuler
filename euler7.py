import math


def is_prime(n):  # function for if a num is prime
    if n <= 1:
        return False

    max_div = math.floor(math.sqrt(n))
    for i in range(2, 1 + max_div):
        if n % i == 0:
            return False
    return True

count = 0
run = True

while run:

    for i in range(0,100000000,1):
        if is_prime(i) == True:

            count += 1

            if count == 10001:
                print(i)
                run = False

        else:
            continue
