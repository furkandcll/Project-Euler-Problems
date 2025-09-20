import time
import pandas as pd

def factorization(number):
    factors = []
    upper_limit = int(number ** 0.5)
    for i in range(1, upper_limit + 1):
        if number % i == 0:
            factors.append(i)
            factors.append(number // i)
    return len(factors)

start1 = time.time()

def triangle_number():
    triangle_number = 1
    for i in range(2, 20000):
        triangle_number += i
        if factorization(triangle_number) >= 500:
            break
    return triangle_number

x1 = triangle_number()

end1 = time.time()

#--------------------------------------------------------------------------------------

start2 = time.time()

def optimized_triangle_number():
    for n in range(1, 20000):
        triangle = (n * (n + 1)) // 2
        if n % 2 == 0:
            comp1 = n // 2
            comp2 = n + 1
            if factorization(comp1) * factorization(comp2) >= 500:
                return triangle
        else:
            comp1 = n
            comp2 = (n + 1) // 2
            if factorization(comp1) * factorization(comp2) >= 500:
                return triangle

end2 = time.time()

x2 = optimized_triangle_number()

df = pd.DataFrame({
    "Method": [None, "Method - 1", "Method - 2"],
    "Result": [None, x1, x2],
    "Time (seconds)": [None, end1 - start1, end2 - start2]
})

print(df)