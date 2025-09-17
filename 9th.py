def pythagorian_finder(value):

    for i in range(1, value):
        for j in range(i + 1, value - 1):
                a = i
                b = j
                c = value - a - b
                if a**2 + b**2 == c**2:
                    return a, b, c
                
print(pythagorian_finder(1000))