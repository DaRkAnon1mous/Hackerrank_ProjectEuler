import math

def smallest_multiple(N):
    result = 1

    for i in range(1, N + 1):
        result = result * i // math.gcd(result, i)

    return result

def main():
   
    T = int(input())

    for _ in range(T):
        
        N = int(input())
        
       
        result = smallest_multiple(N)
        print(result)

if __name__ == "__main__":
    main()
