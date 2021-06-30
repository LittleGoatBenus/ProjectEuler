

def factorial(x):
    total = 1
    totallist = []
    sum = 0
    for i in range(1,x+1):
        total *= i

    totalstr = str(total)


    for n in range(0,len(totalstr)):

        sum += int(totalstr[n])


    print(sum)


factorial(100)
