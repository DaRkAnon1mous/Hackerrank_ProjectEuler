t = int(input())
n = []
for _ in range(t):
    n.append(int(input()))

# Function to find the sum of all multiples of 3 or 5 below n
def sum_of_squares_difference(n):
    sum_of_squares = sum(i**2 for i in range(1, n+1))
    square_of_sum = sum(range(1, n+1))**2
    return abs(sum_of_squares - square_of_sum)

# Output the absolute difference for each test case
result = [sum_of_squares_difference(num) for num in n]
for i in result:
    print(i)
