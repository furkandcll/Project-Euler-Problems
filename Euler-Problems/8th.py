import pandas as pd
import math
import time

data = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"

start1 = time.time()

products_data = []

for split in (range (0, 997)):
    temp = data[split:split+4]
    if "0" in temp:
        continue
    product = int(temp[0]) * int(temp[1]) * int(temp[2]) * int(temp[3])
    dictionary = {"Digits": temp, "Product": product}
    products_data.append(dictionary)

max_entry = max(products_data, key=lambda x: x["Product"])

end1 = time.time()

#--------------------------------------------------------------------------------------

start2 = time.time()

def search1():

    max_product = 0

    for split in (range (0, 997)):
        temp = data[split:split+4]
        if "0" in temp:
            continue
        product = int(temp[0]) * int(temp[1]) * int(temp[2]) * int(temp[3])
        if product > max_product:
            max_product = product
            max_digits = temp
    
    dictionary = {"Digits": max_digits, "Product": max_product}

    return dictionary

result1 = search1()
    
end2 = time.time()

#--------------------------------------------------------------------------------------

start3 = time.time()

def search2():

    max_product = 0

    for split in (range (0, 997)):
        temp = data[split:split+4]
        if "0" in temp:
            continue
        coverting = [int(d) for d in temp]
        product = math.prod(coverting)
        if product > max_product:
            max_product = product
            max_digits = temp
    
    dictionary = {"Digits": max_digits, "Product": max_product}

    return dictionary
    
result2 = search2()

end3 = time.time()

#--------------------------------------------------------------------------------------

start4 = time.time()

def optimized_search(givendata):

    seq_len = 4   # can be any positive integer
    max_product = 0
    max_digits = ""
    i = 0

    while i <= len(givendata) - seq_len:
        temp = givendata[i:i+4]

        if "0" in temp:
            
            zero_index = temp.index("0")
            i += zero_index + 1
            continue

        coverting = [int(d) for d in temp]
        product = math.prod(coverting)
        if product > max_product:
            max_product = product
            max_digits = temp

        i += 1

    dictionary = {"Digits": max_digits, "Product": max_product}

    return dictionary

result3 = optimized_search(data)

end4 = time.time()

df = pd.DataFrame({
    "Method": ["Method - 1", "Method - 2", "Method - 3", "Method - 4"],
    "Result": [max_entry, result1, result2, result3],
    "Time (seconds)": [end1 - start1, end2 - start2, end3 - start3, end4 - start4]
})

print("\nSince the data is small, we cannot see the difference in our data.\n")
print(df, "\n")

#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------

import random

# Define the length of the random string
length = 10**6  # 1 million digits

# Generate the random string
random_string = ''.join(random.choices('0123456789', k=length))

start1 = time.time()

products_data = []

for split in (range (0, 999997)):
    temp = random_string[split:split+4]
    if "0" in temp:
        continue
    product = int(temp[0]) * int(temp[1]) * int(temp[2]) * int(temp[3])
    dictionary = {"Digits": temp, "Product": product}
    products_data.append(dictionary)

max_entry = max(products_data, key=lambda x: x["Product"])

end1 = time.time()

#--------------------------------------------------------------------------------------

start2 = time.time()

def search1():

    max_product = 0

    for split in (range (0, 999997)):
        temp = random_string[split:split+4]
        if "0" in temp:
            continue
        product = int(temp[0]) * int(temp[1]) * int(temp[2]) * int(temp[3])
        if product > max_product:
            max_product = product
            max_digits = temp
    
    dictionary = {"Digits": max_digits, "Product": max_product}

    return dictionary

result1 = search1()
    
end2 = time.time()

#--------------------------------------------------------------------------------------

start3 = time.time()

def search2():

    max_product = 0

    for split in (range (0, 999997)):
        temp = random_string[split:split+4]
        if "0" in temp:
            continue
        coverting = [int(d) for d in temp]
        product = math.prod(coverting)
        if product > max_product:
            max_product = product
            max_digits = temp
    
    dictionary = {"Digits": max_digits, "Product": max_product}

    return dictionary
    
result2 = search2()

end3 = time.time()

#--------------------------------------------------------------------------------------

start4 = time.time()

def optimized_search(givendata):

    seq_len = 4   # can be any positive integer
    max_product = 0
    max_digits = ""
    i = 0

    while i <= len(givendata) - seq_len:
        temp = givendata[i:i+4]

        if "0" in temp:
            
            zero_index = temp.index("0")
            i += zero_index + 1
            continue

        product = 1
        for d in temp:
            product *= int(d)

        if product > max_product:
            max_product = product
            max_digits = temp

        i += 1

    dictionary = {"Digits": max_digits, "Product": max_product}

    return dictionary

result3 = optimized_search(random_string)

end4 = time.time()

df = pd.DataFrame({
    "Method": [None, "Method - 1", "Method - 2", "Method - 3", "Method - 4"],
    "Result": [None, max_entry, result1, result2, result3],
    "Time (seconds)": [None, end1 - start1, end2 - start2, end3 - start3, end4 - start4]
})

print("'math.prod' is not being used in the last function this time.\n")
print(df)
