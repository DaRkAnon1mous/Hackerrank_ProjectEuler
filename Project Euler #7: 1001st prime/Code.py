def sieve_of_eratosthenes(limit):
    primes = []
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for num in range(2, int(limit**0.5) + 1):
        if is_prime[num]:
            primes.append(num)
            for multiple in range(num * num, limit + 1, num):
                is_prime[multiple] = False

    for num in range(int(limit**0.5) + 1, limit + 1):
        if is_prime[num]:
            primes.append(num)

    return primes

def nth_prime_number(n):
    limit = 110000  # Choose a sufficiently large limit to generate the nth prime
    primes = sieve_of_eratosthenes(limit)
    return primes[n - 1]

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        result = nth_prime_number(N)
        print(result)

if __name__ == "__main__":
    main()
