import math


def num_divisors(n):
    count = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            count += 2
    return count


def triangle_number(n):
    return sum(range(1, n + 1))


n = 1
triangle = triangle_number(n)
divisors = num_divisors(triangle)
while divisors <= 500:
    n += 1
    triangle = triangle_number(n)
    divisors = num_divisors(triangle)

print("The first triangle number with over 500 divisors is", triangle)
