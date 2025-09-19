grid = []
with open("grid.txt") as f:
    for line in f:
        grid.append([int(x) for x in line.split()])

results = []

pairs = {"Numbers": None, "Product": None}

for i in range(0,20):
    for j in range(0, 20):
        if j + 3 >= 20:
            continue
        pairs = {"Numbers": (grid[i][j], grid[i][j + 1], grid[i][j + 2], grid[i][j + 3]), "Product": grid[i][j] * grid[i][j + 1] * grid[i][j + 2] * grid[i][j + 3]}
        results.append(pairs)
    

for i in range(0,20):
    for j in range(0, 20):
        if i + 3 >= 20:
            continue
        pairs = {"Numbers": (grid[i][j], grid[i + 1][j], grid[i + 2][j], grid[i + 3][j]), "Product": grid[i][j] * grid[i + 1][j] * grid[i + 2][j] * grid[i + 3][j]}
        results.append(pairs)

for i in range(0,20):
    for j in range(0, 20):
        if i + 3 >= 20 or j + 3 >= 20:
            continue
        pairs = {"Numbers": (grid[i][j], grid[i + 1][j + 1], grid[i + 2][j + 2], grid[i + 3][j + 3]), "Product": grid[i][j] * grid[i + 1][j + 1] * grid[i + 2][j + 2] * grid[i + 3][j + 3]}
        results.append(pairs)

for i in range(0, 20):
    for j in range(3, 20):
        if i + 3 >= 20 or j + 3 >= 20:
            continue
        pairs = {"Numbers": (grid[i][j], grid[i+1][j-1], grid[i+2][j-2], grid[i+3][j-3]), "Product": grid[i][j] * grid[i+1][j-1] * grid[i+2][j-2] * grid[i+3][j-3]}
        results.append(pairs)

greatest = max(results, key=lambda x: x["Product"])

print(greatest)