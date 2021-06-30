def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors



for i in range(0,10000000000000000000000000000,1):
    Tn = int((i*(i+1))/2)
    x = prime_factors(Tn)
    prev = 0
    total = []
    div = 1
    broken = False

    for j in x:

        if prev != j:
            print("for number",Tn,"prime factor",j,"occurs")
            p = int(x.count(j))
            total.append(p)
            print(total)
            if j == x[-1]:
                for z in total:
                    div *= (z+1)
                    if div >= 500:
                        print(Tn)
                        broken = True
        prev = j
    if broken:
        break
