# Sieve of Eratosthenes for prime factorization

import math

given_n = int(input("Enter a number: "))

upper_limit = math.isqrt(given_n)

if given_n < 2:
    print("No prime factors have found.")
    exit()
elif given_n == 2:
    print("2 is the only prime factor.")
    exit()
else:
    primelist = set(range(2, upper_limit + 1))

for i in range(2, upper_limit + 1):
    if i in primelist:
        for j in range(i*i, upper_limit + 1, i):
            primelist.discard(j)

prime_factors = set()

for i in primelist:
    if given_n % i == 0:
        prime_factors.add(i)
    if given_n > 1 and all(given_n % i != 0 for i in primelist): # If the number is greater than 1 and none of the smaller primes divide it, then the number itself is a prima factor
        prime_factors.add(given_n)

print("Prime factors are:\n", sorted(prime_factors), sep="")


