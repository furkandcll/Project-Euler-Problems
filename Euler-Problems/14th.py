def collatz(attempt):

    longest = {"The Number": None, "Sequence": []}

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

        if len(temp_list) > len(longest["Sequence"]):
            longest = {"The Number": i, "Sequence": temp_list}
    return longest

x = collatz(1000000)

print(x)