Fib = 1
Fib1 = 1
Fib2 = 1
total = 0


while Fib < 4000000:
    if (Fib % 2 == 0):
        total = Fib + total
       
    print(Fib)
    Fib = Fib1 + Fib2
    Fib2 = Fib1
    Fib1 = Fib
   
print(total)
