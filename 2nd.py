import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

x = int(input("Enter an upper limit: "))

fibonacci = [0, 1]

while True:
    tempn = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(tempn)

    if fibonacci[-1] > x:
        break

print("Fibonacci Sequence:\n", fibonacci, sep="")

evenvalues = []

for i in fibonacci:
    if i % 2 == 0:
        evenvalues.append(i)
        i += 1

print("Sum of the even values: ", sum(evenvalues))

plt.plot(fibonacci, marker="o", linestyle="--", color="c", label="Fibonacci")
plt.xlabel("Index")
plt.ylabel("Integer Value")
plt.title("Fibonacci Sequence")
plt.legend()
plt.grid(True)
plt.show()