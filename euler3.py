LargePrime = []


def IsPrime(larg):
    for i in range (2, larg):
        if (larg % i)== 0:
            print(larg, "is not a prime number")
            print(i, "times", larg //i,"is",larg)
            break
        else:
            largPrime = larg
            print(largPrime, "is a prime number")
     

def factor(num):
    n = 1
    larg = 0
    large = 0
   
    for i in range (600851475143):
        if (num % n == 0) and (num % 2 is not 0):
            if n > larg:
                larg = n

                LargePrime.append(larg)
                print(LargePrime)

        n = n + 1


factor(600851475143)
IsPrime(LargePrime)
