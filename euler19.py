#        jan   feb  mar  apr  may jun  jul  aug  sept oct  nov  dec
month = ["01","02","03","04","05","06","07","08","09","10","11","12"]
days =  [1,2,3,4,5,6,7]
c_sun = 0
d_count = 0
d_store = 0
run = True

for year in range(1901,2001):
    for i in month:
        if i == month[0] or i == month[2] or i == month[4] or i == month[6] or i == month[7] or i == month[9] or i == month[11]:
            #months with 31 days
            print(i)
            d_store = d_count
            for day in range(1,32):
                d_count += 1
                if day == 1 and d_count == 1:
                    c_sun += 1
                if d_count == 7:
                    d_count = 0
            d_store = d_count


        else:
            if i == month[1]:
                if (year % 4) == 0:
                    #leap year 29 days
                    print(i,"leap year")
                    d_store = d_count
                    for day in range(1, 30):
                        d_count += 1
                        if day == 1 and d_count == 1:
                            c_sun += 1
                        if d_count == 7:
                            d_count = 0
                            d_store = d_count

                else:
                    #28 days
                    print(i)
                    d_store = d_count
                    for day in range(1, 29):
                        d_count += 1
                        if day == 1 and d_count == 1:
                            c_sun += 1
                        if d_count == 7:
                            d_count = 0
                            d_store = d_count

            else:
                #months with 30 days
                print(i)
                d_store = d_count
                for day in range(1, 31):
                    d_count += 1
                    if day == 1 and d_count == 1:
                        c_sun += 1
                    if d_count == 7:
                        d_count = 0
                        d_store = d_count


print(c_sun)
