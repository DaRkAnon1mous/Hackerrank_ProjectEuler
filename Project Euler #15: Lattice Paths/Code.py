# Enter your code here. Read input from STDIN. Print output to STDOUT
MOD = 1000000007

def count_routes(n, m):
    # Create a 2D array to store the number of routes at each position
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Initialize base cases
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                dp[i][j] = 1

    # Calculate the number of routes for each position
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % MOD

    return dp[n][m]

def main():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        result = count_routes(N, M)
        print(result)

if __name__ == "__main__":
    main()
