import sys


def solution():
    MOD = 10007

    size = int(input())

    dp = [[1 for _ in range(10)]]
    for _ in range(size):
        dp.append([0 for _ in range(10)])

    for i in range(1, size + 1):
        for j in range(10):
            if j == 0:
                dp[i][0] = 1
            else:
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

    print(dp[size][9] % MOD)


solution()
