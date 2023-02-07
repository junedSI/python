def is_prime(n):
    if n <= 1:                                                      #if n is 1 then there is no need of sum return 0 terminate.
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def sum_of_primes(limit):
    return sum(n for n in range(2, limit) if is_prime(n))           #passing in is prime to check it is prime or not


n = int(input('till which position you want sum\n'))
print(sum_of_primes(n))
