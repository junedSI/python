def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def sum_of_primes(limit):
    return sum(n for n in range(2, limit) if is_prime(n))


n = int(input('Enter the no below you want the sum\n'))
print(sum_of_primes(n))
