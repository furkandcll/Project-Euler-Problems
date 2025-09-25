n = 2_000_000

def optimized_sieve(limit):

    is_prime = [True] * limit
    is_prime[0:2] = [False, False]

    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, limit, i):
                is_prime[j] = False

    primes = [i for i, val in enumerate(is_prime) if val]
    return primes

primes = optimized_sieve(n)

print(sum(primes))