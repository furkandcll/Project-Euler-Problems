import pandas as pd

x = int(input("Enter a number: "))

i = 0

numbers = []

while i < x:
    if i % 3 == 0 or i % 5 == 0:
        numbers.append(i)
    i += 1
    

euler1 = sum(numbers)

pandas_test = pd.Series(numbers)

print("Sum of the numbers that can be divided by either 3 or 5: ", euler1)

print("Pandas series:\n", pandas_test, sep="")

print("Mean value: ",pandas_test.mean())
print("Maximum value: ",pandas_test.max())
print("Minimum value: ", pandas_test.min())