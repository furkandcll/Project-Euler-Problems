with open("13th.txt", "r", encoding="utf-8") as f:
    numbers = [int(line.strip()) for line in f]

total = sum(numbers)
first_10 = str(total)[:10]

print(first_10)