n = int(input('enter range'))
for a in range(1, n):            #range for a
    for b in range(a+1, n):      #range for b will start from a+1 1*1=1
        c = n - a - b            #coz a+b+c=1000
        if a*a + b*b == c*c:
            print(a, b, c)          #values a,b,c
            print(a*b*c)            #product of a,b,c
            break
