# result = 2**1000
# result = str(result)
# final = 0
# for digits in range(len(result)):
#     final += int(result[digits])
# print(final)
#--------------------------------------------------
result = 2**1000
final = sum(int(digit) for digit in str(result))
print(final)