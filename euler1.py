num = 0

for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        ptint(i)
        num += i

print(num)
