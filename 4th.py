import pandas as pd

def if_palindrome(x, y):
    is_it = int(x) * int(y)
    templist = []
    converted = str(is_it)

    for i in converted:
        templist.append(i)
    
    reversed = templist[::-1]

    if templist == reversed:
        return True


first_threedigit = set(range(100, 1000))

second_threedigit = set(range(100, 1000))

palindrome_product = {
    "numbers": None,
    "product": None
}

results = []

for i in first_threedigit:
    for j in second_threedigit:
        if i > j:
            continue
        if if_palindrome(i, j) == True:
            palindrome_product = {"numbers": (i, j), "product": i * j}
            results.append(palindrome_product)

print("-----------------------------------------------------------------------------------------------------------------------")

print("Basic Data-Frame:\n")
df = pd.DataFrame(results)
print(df)

print("-----------------------------------------------------------------------------------------------------------------------")

print("The 5 biggest Palindromes:\n")
sorted_df = df.sort_values(by="product", ascending=False)
print(sorted_df.head())

print("-----------------------------------------------------------------------------------------------------------------------")

print("Palindromes that are bigger than 100.000:\n")
large_palindromes = df[df["product"] > 100000]
print(large_palindromes)

print("-----------------------------------------------------------------------------------------------------------------------")

largest = max(results, key=lambda d: d["product"])
print("Largest palindrome made from the product of two-digit numbers:", largest)

print("-----------------------------------------------------------------------------------------------------------------------")

df.to_csv("palindrome_products.csv", index=False)