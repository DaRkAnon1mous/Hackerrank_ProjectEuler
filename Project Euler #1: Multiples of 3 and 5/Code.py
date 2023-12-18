#!/bin/python3

t = int(input())
n = []

for _ in range(t):
    n.append(int(input()))

for num in n:
    num -= 1  # Adjust num to exclude itself from the sum if it's a multiple of 3 or 5

    sum_of_multiples_of_3 = (3 * (num // 3) * (num // 3 + 1)) // 2
    sum_of_multiples_of_5 = (5 * (num // 5) * (num // 5 + 1)) // 2
    sum_of_multiples_of_15 = (15 * (num // 15) * (num // 15 + 1)) // 2

    sum_of_multiples_of_3_or_5 = sum_of_multiples_of_3 + sum_of_multiples_of_5 - sum_of_multiples_of_15
    print(sum_of_multiples_of_3_or_5)


