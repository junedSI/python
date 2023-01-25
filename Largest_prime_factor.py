import math


def find_largest_prime_factor(num):
    largest_prime_factor = 1
    for i in range(2, int(math.sqrt(num))+1):
        while num % i == 0:
            largest_prime_factor = i
            num = num // i
    if num > largest_prime_factor:
        largest_prime_factor = num
    return largest_prime_factor


num = 600851475143
print("Largest prime factor of", num, ":", find_largest_prime_factor(num))
