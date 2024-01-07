#!/bin/python3
import math
def largest_prime_factor(n):
    while n % 2 == 0:
        max_prime = 2
        n //= 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            max_prime = i
            n //= i
    if n > 2:
        max_prime = n
    return max_prime
# Input and output
T = int(input())
N = []
for _ in range(T):
    N.append(int(input()))
result = [largest_prime_factor(n) for n in N]
for i in result:
    print(i)




