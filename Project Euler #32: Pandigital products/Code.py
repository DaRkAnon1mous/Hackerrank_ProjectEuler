# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

def is_pandigital(a, b, product, n):
    concatenated_str = str(a) + str(b) + str(product)
    return ''.join(sorted(concatenated_str)) == ''.join(map(str, range(1, n + 1)))

def find_pandigital_products_sum(N):
    pandigital_products = set()

    # The maximum number of digits in multiplicand and multiplier combined is N//2 each
    limit = 10**(N//2)

    for a in range(1, limit):
        for b in range(a, limit):
            product = a * b
            if product > 10**(N - len(str(a)) - len(str(b))):
                break

            if is_pandigital(a, b, product, N):
                pandigital_products.add(product)

    return sum(pandigital_products)

# Input
N = int(input().strip())

# Output
result = find_pandigital_products_sum(N)
print(result)
