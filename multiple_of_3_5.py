n = int(input('Enter the range\n'))
count=0
for i in range(n):
    if (i%3==0) or (i%5==0):
        count = count + i
print(count)
        