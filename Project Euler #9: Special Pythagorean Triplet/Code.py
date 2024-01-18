def find_pythagorean_triplet_product(n):
    max_product = -1
    for a in range(1, n // 3 + 1):
        b = (n * n - 2 * n * a) // (2 * n - 2 * a)
        c = n - a - b
        if a < b < c and a*a + b*b == c*c:
            max_product = max(max_product, a * b * c)
    return max_product

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        result = find_pythagorean_triplet_product(n)
        print(result)

if __name__ == "__main__":
    main()

