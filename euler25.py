#generating a fibonacci seq
from typing import Any, Union

fib = 1
pfib = 0
ppfib = 0
count = 1

while len(str(fib)) < 1000:
    count += 1
    print(fib)
    ppfib = pfib
    pfib = fib
    fib = pfib + ppfib

print(count)
