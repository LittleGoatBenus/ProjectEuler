nums = [1,2,3,4,5,6,7,8,9]
temp = []
sum = 0
onebyfour = []
twobytwo = []
twobythree = []
results = []
final = []

for a in range(1,10):

    for b in range(1000,10000):
        temp.clear()
        solution = a * b
        string = str(solution)
        stringa = str(a)
        stringb = str(b)

        for i in range(0,len(str(solution))):
            temp.append(int(string[i]))

        for j in range(0,len(str(a))):

            temp.append(int(stringa[j]))

        for k in range(0,len(str(b))):

            temp.append(int(stringb[k]))

        sort = sorted(temp)

        if sort == nums:
            print(a, "*", b,"yes")
            results.append(solution)

for a in range(10,100):

    for b in range(100,1000):
        temp.clear()
        solution = a * b
        string = str(solution)
        stringa = str(a)
        stringb = str(b)

        for i in range(0,len(str(solution))):
            temp.append(int(string[i]))

        for j in range(0,len(str(a))):

            temp.append(int(stringa[j]))

        for k in range(0,len(str(b))):

            temp.append(int(stringb[k]))

        sort = sorted(temp)

        if sort == nums:
            print(a, "*", b,"yes")
            results.append(solution)


for a in range(10,100):

    for b in range(10, 100):
        temp.clear()
        solution = a * b
        string = str(solution)
        stringa = str(a)
        stringb = str(b)

        for i in range(0,len(str(solution))):
            temp.append(int(string[i]))

        for j in range(0,len(str(a))):

            temp.append(int(stringa[j]))

        for k in range(0,len(str(b))):

            temp.append(int(stringb[k]))

        sort = sorted(temp)

        if sort == nums:
            print(a, "*", b,"yes")
            results.append(solution)

for element in results:
    if element not in final:
        final.append(element)

print(final)

for e in final:
    sum += e

print(sum)
