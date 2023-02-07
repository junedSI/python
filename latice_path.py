import math


def binomial_coefficient(n, k):
    return math.comb(n, k)


def number_of_routes(n):
    return binomial_coefficient(2 * n, n)


print("Number of routes in a 20 x 20 grid:", number_of_routes(20))
