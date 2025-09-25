import time
import pandas as pd

def collatz1(attempt):

    longest = {"The Number": None, "Sequence": 0}

    for i in range(1, attempt + 1): 

        temp_list = []
        temp = i

        while temp != 1:
            temp_list.append(temp)
            if temp % 2 == 0:
                temp = temp // 2
            else:
                temp = 3 * temp + 1

        temp_list.append(1)

        if len(temp_list) > longest["Sequence"]:
            converted = len(temp_list)
            longest = {"The Number": i, "Sequence": converted}
    return longest

start1 = time.time()

x = collatz1(1_000_000)

end1 = time.time()

#-------------------------------------------------------------------------

def collatz2(attempt):
    cache = {1: 1}
    longest = {"The Number": None, "Sequence": 0}

    def seq_length(n):
        if n in cache:
            return cache[n]
        if n % 2 == 0:
            cache[n] = 1 + seq_length(n // 2)
        else:
            cache[n] = 1 + seq_length(3 * n + 1)
        return cache[n]

    for i in range(1, attempt + 1):
        length = seq_length(i)
        if length > longest["Sequence"]:
            longest = {"The Number": i, "Sequence": length}

    return longest

start2 = time.time()

y = collatz2(1_000_000)

end2 = time.time()

df = pd.DataFrame({
    "Method": [None, "Method - 1", "Method - 2"],
    "Result": [None, x, y],
    "Time (seconds)": [None, end1 - start1, end2 - start2]
})

print(df)

#        Method                                   Result  Time (seconds)
# 0        None                                     None             NaN
# 1  Method - 1  {'The Number': 837799, 'Sequence': 525}       31.969614
# 2  Method - 2  {'The Number': 837799, 'Sequence': 525}        1.606530