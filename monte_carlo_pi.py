import random

def monte_carlo_pi(attempts=1_000_000):
    sphere = 0
    for _ in range(attempts):
        x, y = random.random(), random.random()
        if x**2 + y**2 <= 1:
            sphere += 1
    result = (sphere/attempts) * 4
    print(result)

monte_carlo_pi()