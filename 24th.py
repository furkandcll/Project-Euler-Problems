lexicographic = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

remainder = 999_999
result = []
turn = 10

while turn >= 1:
    temp = factorial(turn - 1)
    index = remainder // temp
    remainder = remainder % temp
    result.append(str(lexicographic[index]))
    lexicographic.pop(index)
    turn -= 1

for letter in range(len(result)):
    print(result[letter], end="")