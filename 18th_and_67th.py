pre_triangle = "75 95 64 17 47 82 18 35 87 10 20 4 82 47 65 19 1 23 75 3 34 88 2 77 73 7 63 67 99 65 4 28 6 16 70 92 41 41 26 56 83 40 80 70 33 41 48 72 33 47 32 37 16 94 29 53 71 44 65 25 43 91 52 97 51 14 70 11 33 28 77 73 17 78 39 68 17 57 91 71 52 38 17 14 91 43 58 50 27 29 48 63 66 4 68 89 53 67 30 73 16 69 87 40 31 4 62 98 27 23 9 70 98 73 93 38 53 60 4 23"

numbers = [int(x) for x in pre_triangle.split()]

triangle_18 = []
index = 0
row_length = 1

while index < len(numbers):
    row = numbers[index:index+row_length]
    triangle_18.append(row)
    index += row_length
    row_length += 1

with open("67_triangle.txt", "r", encoding="utf-8") as f:
    triangle_67 = [[int(x) for x in line.strip().split()] for line in f]

def maximum_path_triangle(triangle):

    reversed_triangle = triangle[::-1]
    
    triangle_copy = reversed_triangle.copy()

    for i in range(1, len(triangle_copy)):

        upper_row = triangle_copy[i]
        lower_row = triangle_copy[i-1]

        for j in range(len(upper_row)):

            upper_row[j] += max(lower_row[j], lower_row[j+1])

    return triangle_copy[-1][0]

print(maximum_path_triangle(triangle_18))

print(maximum_path_triangle(triangle_67))