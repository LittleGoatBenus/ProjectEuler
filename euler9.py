run = True

while run:
    for a in range(1,1001,1):
        for b in range(1,1001,1):
   
                mult = (a)**2 + (b)**2
                c = (mult)**0.5
                if c.is_integer():
                   
                    if a + b + c == 1000:
                        print("FOUND FOUND FOUND",a,b,c)
                        run = False
                       
                       
                    else:
                        print("1 exception met",a,b,c)
                       
                else:
                    print("no")
