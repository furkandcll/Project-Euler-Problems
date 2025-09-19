grid = []
with open("grid.txt") as f:
    for line in f:
        grid.append([int(x) for x in line.split()])
the_top =  {"Numbers": None, "Product": 0}

#--------------------------------------------------------------------------------------

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

#--------------------------------------------------------------------------------------

for i in range(0,20):
    for j in range(0, 20):
        if j + 3 >= 20:
            continue
        product = grid[i][j] * grid[i][j + 1] * grid[i][j + 2] * grid[i][j + 3]
        if product > the_top["Product"]:
            the_top = {"Numbers": (grid[i][j], grid[i][j + 1], grid[i][j + 2], grid[i][j + 3]), "Product": product}

for i in range(0,20):
    for j in range(0, 20):
        if i + 3 >= 20:
            continue
        product = grid[i][j] * grid[i + 1][j] * grid[i + 2][j] * grid[i + 3][j]
        if product > the_top["Product"]:
            the_top = {"Numbers": (grid[i][j], grid[i + 1][j], grid[i + 2][j], grid[i + 3][j]), "Product": product}

for i in range(0,20):
    for j in range(0, 20):
        if i + 3 >= 20 or j + 3 >= 20:
            continue
        product = grid[i][j] * grid[i + 1][j + 1] * grid[i + 2][j + 2] * grid[i + 3][j + 3]
        if product > the_top["Product"]:
            the_top = {"Numbers": (grid[i][j], grid[i + 1][j + 1], grid[i + 2][j + 2], grid[i + 3][j + 3]), "Product": product}

for i in range(0, 20):
    for j in range(3, 20):
        if i + 3 >= 20 or j + 3 >= 20:
            continue
        product = grid[i][j] * grid[i+1][j-1] * grid[i+2][j-2] * grid[i+3][j-3]
        if product > the_top["Product"]:
            the_top = {"Numbers": (grid[i][j], grid[i+1][j-1], grid[i+2][j-2], grid[i+3][j-3]), "Product": product}

print(the_top)

#--------------------------------------------------------------------------------------

directions = [
    (0, 1),
    (1, 0),
    (1, 1),
    (1, -1)
]



for i in range(20):
    for j in range(20):
        for dx, dy in directions:
            try:
                numbers = [grid[i + k*dx][j + k*dy] for k in range(4)]
                product = 1
                for n in numbers:
                    product *= n
                if product > the_top["Product"]:
                    the_top = {"Numbers": numbers, "Product": product}
            except IndexError:
                continue

print(the_top)
