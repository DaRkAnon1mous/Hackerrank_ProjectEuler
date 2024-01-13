def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_primes_not_greater_than_n(N):
    total = 0
    for num in range(2, N + 1):
        if is_prime(num):
            total += num
    return total

T = int(input())
for _ in range(T):
    N = int(input())
    result = sum_of_primes_not_greater_than_n(N)
    print(result)
