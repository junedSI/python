import math

def find_largest_prime_factor(num):
    for i in range(2, int(math.sqrt(num))+1):       # 2 is the first prime no thats why starting from 2.
        while num % i == 0:
            largest_prime_factor = i                # setting it to divisible no.
            num = num // i                          #round off to the nearest whole number
    if num > largest_prime_factor:
        largest_prime_factor = num
    return largest_prime_factor


num = int(input("Number to find its largest prime factor:\n"))
print("Largest prime factor of", num, ":", find_largest_prime_factor(num))
