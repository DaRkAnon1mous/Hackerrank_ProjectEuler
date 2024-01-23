# Enter your code here. Read input from STDIN. Print output to STDOUT
def is_sum_of_nth_powers(number, power):
    digit_powers_sum = sum(int(digit) ** power for digit in str(number))
    return digit_powers_sum == number

def find_numbers_sum_of_nth_powers(power):
    numbers_sum_of_powers = []
    upper_limit = 9**power * (power + 1)  # Upper limit based on the digits

    for num in range(10, upper_limit + 1):
        if is_sum_of_nth_powers(num, power):
            numbers_sum_of_powers.append(num)

    return numbers_sum_of_powers

# Input reading and processing
N = int(input())
numbers_sum_of_powers = find_numbers_sum_of_nth_powers(N)
result = sum(numbers_sum_of_powers)
print(result)
