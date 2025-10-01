# def non_abundant_sums():

#     results = []

#     def divisor_finder(limit=28_123):
#         cache = {1: [1]}

#         def get_divisors(n):
#             if n in cache:
#                 return cache[n]

#             divisors = []
#             for j in range(1, n // 2 + 1):
#                 if n % j == 0:
#                     divisors.append(j)

#             cache[n] = divisors
#             return divisors

#         for i in range(1, limit):
#             divisors = get_divisors(i)
#             results.append({"Number": i, "divisors": divisors})
#         return results

#     def catagorizer():
    
#         end_results = []

#         x = divisor_finder()

#         for i in range(len(x)):

#             a = x[i]["Number"]
#             da = sum(x[i]["divisors"])

#             if da == a:
#                 end_results.append({"number": a, "type": "perfect"})
#             elif da < a:
#                 end_results.append({"number": a, "type": "deficient"})
#             elif da > a:
#                 end_results.append({"number": a, "type": "abundant"})

#         return end_results
    
#     to_catagorize = catagorizer()

#     abundant_n = []

#     for i in range(len(to_catagorize)):
#         a = to_catagorize[i]["number"]
#         b = to_catagorize[i]["type"]
#         if b == "abundant":
#             abundant_n.append({"number": a, "type": "abundant"})

#     not_abundant = []

#     for i in range(1, 28123):
#         for j in range(len(abundant_n)):
#             for k in range(j, len(abundant_n)):
#                 temp = j + k
#                 if i == temp:
#                     continue
#                 else:
#                     not_abundant.append(i)

#     return not_abundant
    

# hope = non_abundant_sums()

# print(sum(hope))

# - potentially taking forever | poor code and crude logic -

#-------------------------------------------------------------------------------

def non_abundant_sums():

    results = []

    def divisor_finder(limit=28_123):
        cache = {1: [1]}

        def get_divisors(n):
            if n in cache:
                return cache[n]

            divisors = []
            for j in range(1, int(n**0.5) + 1): # sqrt(n)
                if n % j == 0:
                    divisors.append(j)

                    if j != n // j and n // j != n:
                        divisors.append(n // j)

            cache[n] = divisors
            return divisors

        for i in range(1, limit):
            divisors = get_divisors(i)
            results.append({"Number": i, "divisors": divisors})

        return results

    def catagorizer():
    
        end_results = []

        x = divisor_finder()

        for i in range(len(x)):

            a = x[i]["Number"]
            da = sum(x[i]["divisors"])

            if da == a:
                end_results.append({"number": a, "type": "perfect"})
            elif da < a:
                end_results.append({"number": a, "type": "deficient"})
            elif da > a:
                end_results.append({"number": a, "type": "abundant"})

        return end_results
    
    to_catagorize = catagorizer()

    abundant_numbers = [x["number"] for x in to_catagorize if x["type"] == "abundant"]
    
    abundant_sums = set()
    for i in range(len(abundant_numbers)):
        for j in range(i, len(abundant_numbers)):
            abundant_sums.add(abundant_numbers[i] + abundant_numbers[j])

    not_abundant = [i for i in range(1, 28124) if i not in abundant_sums]

    return not_abundant
    

solution = non_abundant_sums()

print(sum(solution))