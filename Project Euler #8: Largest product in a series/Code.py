def max_product(num, k):
    max_product = 0
    for i in range(len(num) - k + 1):
        product = 1
        for j in range(i, i + k):
            product *= int(num[j])
        if product > max_product:
            max_product = product
    return max_product

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    number = input().strip()
    result = max_product(number, k)
    print(result)
