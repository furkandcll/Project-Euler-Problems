def amicable():

    results = []

    def divisor_finder(limit=10_000):
        cache = {1: [1]}

        def get_divisors(n):
            if n in cache:
                return cache[n]

            divisors = []
            for j in range(1, n // 2 + 1):
                if n % j == 0:
                    divisors.append(j)

            cache[n] = divisors
            return divisors

        for i in range(1, limit):
            divisors = get_divisors(i)
            results.append({"Number": i, "divisors": divisors})
        return results

    amicables = []

    x = divisor_finder()

    for i in range(len(x)):

        a = x[i]["Number"]
        da = sum(x[i]["divisors"])

        if da < len(x) and da != a:
            db = sum(x[da - 1]["divisors"])
            if db == a:
                amicables.append({"digit1": a, "digit2": da})

    return amicables

print(len(amicable()) // 2)
