t = int(input())
n = []
for _ in range(t):
    n.append(int(input()))

for num in n:
  sum_of_multiples_of_3 = sum(i for i in range(3, num, 3))
  sum_of_multiples_of_5 = sum(i for i in range(5, num, 5))
  sum_of_multiples_of_3_or_5 = sum_of_multiples_of_3 + sum_of_multiples_of_5
  print(sum_of_multiples_of_3_or_5)

