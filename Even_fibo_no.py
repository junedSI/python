a=1
b=2
sum=0
n = int(input("Enter range:"))
while b<=n:
    if b%2==0:
        sum+=b

    c=a+b
    a=b
    b=c
print("Sum of even-valued term:",sum)
