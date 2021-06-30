largestpalindrome = []

def palindrome(number):
    revs_number = 0  
     
    original_num = number
     
    # reverse the integer number using the while loop  
     
    while (number > 0):  
        # Logic  
        remainder = number % 10  
        revs_number = (revs_number * 10) + remainder  
        number = number // 10  
       
        if revs_number == original_num:
            largestpalindrome.append(revs_number)
           
           
           
        else:
            pass



for i in range(999,99,-1):
    for j in range(999, 99, -1):
        number = i * j
        palindrome(number)

print(max(largestpalindrome))
