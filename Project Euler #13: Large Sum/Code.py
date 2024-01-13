# Enter your code here. Read input from STDIN. Print output to STDOUT
def main():
    # Read the number of lines (N)
    N = int(input().strip())

    # Initialize sum to 0
    total_sum = 0

    # Read N lines containing 50-digit numbers
    for _ in range(N):
        number = int(input().strip())
        total_sum += number

    # Print the first ten digits of the sum
    print(str(total_sum)[:10])

if __name__ == "__main__":
    main()
