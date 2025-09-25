import math
import time
import pandas as pd

start1 = time.time()

def normal_sieve(x):

    input = x

    primelist = set(range(2, input))

    for i in range(2, input):
        if i in primelist:
            for j in range(i*i, input, i):
                primelist.discard(j)

    return primelist

to_find = list(normal_sieve(1000000))

end1 = time.time()

#------------------------------------------------------------------------------------------------------

start2 = time.time()

# Prime Number Theorem
n = 10001
estimate = int(n * (math.log(n) + math.log(math.log(n)))) + 10

def sieve_with_PNT(x):

    limit = x

    while True:
        primelist = set(range(2, limit))

        for i in range(2, limit):
            if i in primelist:
                for j in range(i*i, limit, i):
                    primelist.discard(j)

        sorted_primes = sorted(primelist)

        if len(sorted_primes) >= 10001:
            return sorted_primes[10000]
            break

        limit += 4999

PNT_sieve = sieve_with_PNT(estimate)

end2 = time.time()

#------------------------------------------------------------------------------------------------------

# No hash function, thus no sets, PNT still being used, more abstract

start3 = time.time()

def optimized_sieve(limit):

    is_prime = [True] * limit
    is_prime[0:2] = [False, False]

    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, limit, i):
                is_prime[j] = False

    primes = [i for i, val in enumerate(is_prime) if val]
    return primes

primes = optimized_sieve(estimate)

end3 = time.time()



df = pd.DataFrame({
    "Method": ["Basic sieve", "PNT estimate sieve", "Optimized sieve"],
    "Result": [to_find[10000], PNT_sieve, primes[10000]],
    "Time (seconds)": [end1 - start1, end2 - start2, end3 - start3]
})

print(df)