for a in range(1, 1000):            #range for a
    for b in range(a+1, 1000):      #range for b will start from a+1
        c = 1000 - a - b            
        if a*a + b*b == c*c:
            print(a, b, c)          #values a,b,c
            print(a*b*c)            #product of a,b,c
            break
