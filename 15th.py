import math

def path_count(n, m):
    return math.comb(n + m, n)

print(path_count(20, 20))