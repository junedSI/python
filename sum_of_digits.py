def sum_of_digits(n):
    return sum([int(d) for d in str(n)])

n=int(input("enter the no:"))
print("Sum of the digits of 21000:", sum_of_digits(n))
