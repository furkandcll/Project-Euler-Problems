x = int(input("Enter a number: "))

i = 0

numbers = []

while i < x:
    if i % 3 == 0 or i % 5 == 0:
        numbers.append(i)
    i += 1
    

euler1 = sum(numbers)

print(euler1)