found = []
max = (9**5)*5
lower = (2**5)*2
sum = 0

for i in range(lower, max+1,1):
    stringnum = str(i)
    num = 0

    for j in range(0,len(stringnum)):

        num += int(stringnum[j])**5

    if i == num:
        found.append(i)

for item in found:
    sum += item

print(sum)
print(found)
