# Enter your code here. Read input from STDIN. Print output to STDOUT
def sum_of_digits_of_power_of_two(n):
    power_result = 2 ** n
    digit_sum = sum(int(digit) for digit in str(power_result))
    return digit_sum

if __name__ == "__main__":
    # Input the number of test cases
    t = int(input().strip())

    # Process each test case
    for _ in range(t):
        # Input N for each test case
        n = int(input().strip())

        # Calculate and print the sum of digits for 2^N
        result = sum_of_digits_of_power_of_two(n)
        print(result)
