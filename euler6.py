sum100 = 0
sum_of_squares = 0

for i in range(1,101):
   
    sum100 = i +sum100
   
for j in range(1,101):
    sum_of_squares = (j)**2 + sum_of_squares

   
square_of_sums = (sum100)**2

print("the diffrence is",square_of_sums - sum_of_squares)
