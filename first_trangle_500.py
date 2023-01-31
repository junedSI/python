import math


def count_divisors(n):
    divisors = 0
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            divisors += 2
    return divisors


def triangle_number(n):
    return n * (n + 1) // 2


def first_triangle_number_with_over_n_divisors(n):
    i = 1
    while True:
        t = triangle_number(i)
        divisors = count_divisors(t)
        if divisors > n:
            return t
        i += 1


print(first_triangle_number_with_over_n_divisors(500))
