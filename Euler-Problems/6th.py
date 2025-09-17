sum_of_the_squares = sum(i**2 for i in range(1, 101))

the_square_of_the_sum = sum(range(1, 101)) ** 2
    
result = the_square_of_the_sum - sum_of_the_squares

print(result)
