# Enter your code here. Read input from STDIN. Print output to STDOUT
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

def find_sum_of_digits_in_factorial(t, test_cases):
    results = []
    for n in test_cases:
        factorial_result = factorial(n)
        digit_sum = sum_of_digits(factorial_result)
        results.append(digit_sum)
    return results

if __name__ == "__main__":
    # Input
    T = int(input())
    test_cases = []
    for _ in range(T):
        N = int(input())
        test_cases.append(N)

    # Calculate and Output
    results = find_sum_of_digits_in_factorial(T, test_cases)
    for result in results:
        print(result)
