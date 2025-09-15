import math

# def all_primes_until_x(x):

#     input = x

#     primelist = set(range(2, input))

#     for i in range(2, input):
#         if i in primelist:
#             for j in range(i*i, input, i):
#                 primelist.discard(j)

#     return primelist

# to_find = list(all_primes_until_x(1000000))

# print(to_find[10_000])

#------------------------------------------------------------------------------------------------------

# Prime Number Theorem
n = 10001
estimate = int(n * (math.log(n) + math.log(math.log(n)))) + 10

def ten_thousand_first_prime(x):

    limit = x

    while True:
        primelist = set(range(2, limit))

        for i in range(2, limit):
            if i in primelist:
                for j in range(i*i, limit, i):
                    primelist.discard(j)

        sorted_primes = sorted(primelist)

        if len(sorted_primes) >= 10001:
            print(sorted_primes[10000])
            break

        limit += 4999

ten_thousand_first_prime(estimate)