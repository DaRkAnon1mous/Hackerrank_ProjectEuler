# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import factorial

def nth_lexicographic_permutation(word, n):
    result = []
    n -= 1  

    for i in range(len(word), 0, -1):
        index, n = divmod(n, factorial(i - 1))
        result.append(word.pop(index))

    return ''.join(result)


T = int(input())

# Process each test case
for _ in range(T):
    
    N = int(input())

    
    word = list("abcdefghijklm")

   
    result = nth_lexicographic_permutation(word, N)
    print(result)

