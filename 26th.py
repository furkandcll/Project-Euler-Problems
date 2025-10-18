from decimal import Decimal, getcontext

getcontext().prec = 50

def decimal_ext(n):
    decimal_part = n % 1
    s = str(decimal_part)
    return s

results = []

for d in range(2, 1000):
    n = Decimal(1) / Decimal(d)
    nstr = decimal_ext(n)

    count = max_count = 1
    for i in range(len(nstr) - 1):
        if nstr[i] == nstr[i + 1]:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 1

    results.append({"denominator": d, "number": nstr, "length": max_count})

best = max(results, key=lambda x: x["length"])
print(best)
