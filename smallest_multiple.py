def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def main():
    primes = [i for i in range(2, 21) if is_prime(i)]
    res = 1
    for p in primes:
        k = p
        while k * p <= 20:
            k *= p
        res *= k
    print(res)


if __name__ == '__main__':
    main()
