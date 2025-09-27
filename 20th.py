def factorial(x):
    result = x
    while x > 1:
        x -= 1
        result *= x
    return result

def sum_of_digits(x):
    # converted = str(x)
    # result = 0
    # for n in range(len(converted)):
    #     temp = int(converted[n])
    #     result += temp
    # return result
    result = 0
    while x:
        result, x = result + (x % 10), x // 10
    return result

answer = sum_of_digits(factorial(100))

print(answer)