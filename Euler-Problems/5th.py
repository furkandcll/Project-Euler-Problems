import math
import time

def euler5(input):
    for i in range(2, 21):
        if input % i != 0:
            return False
    return True

print("-----------------------------------------------------------------------------------------------------------------------")

start = time.time()

starting_point = 2520

while True:
    if euler5(starting_point):
        break
    starting_point += 2520

end = time.time()

print("Direct search result:", starting_point, "\n")
print("Direct search time:", end - start, "seconds")

print("-----------------------------------------------------------------------------------------------------------------------")

# LCM (Least Common Multiple) = |a * b| / GCM(a, b)
# GCM (Greatest Common Divisor)

def LCM(a, b):
    return abs(a * b) // math.gcd(a, b) 

start = time.time()

outcome = 1

for i in range(2, 21):
    outcome = LCM(outcome, i)

end = time.time()

print("LCM method's result:", outcome, "\n")
print("LCM method's time:", end - start, "seconds")

print("-----------------------------------------------------------------------------------------------------------------------")

start = time.time()

primes = [2, 3, 5, 7, 11, 13, 17, 19]
final = 1

for p in primes:
    calc = int(math.log(20, p))
    final *= p ** calc

end = time.time()

print("Logarithm method's result:", final, "\n")
print("Logarithm time:", end - start, "seconds")

print("-----------------------------------------------------------------------------------------------------------------------")
