"""
Command: prime_numbers
Return a list of all the prime numbers inferior or equal to n
"""


def prime_numbers(n):
    from math import isqrt
    if n <= 2:
        return []
    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, isqrt(n)+1):
        if is_prime[i]:
            for x in range(i*i, n, i):
                is_prime[x] = False

    return [i for i in range(n) if is_prime[i]]


"""
Command: sum_prime_numbers
Return a sum of all the prime numbers inferior or equal to n
"""


def sum_prime_numbers(n):
    return sum(prime_numbers(n))
