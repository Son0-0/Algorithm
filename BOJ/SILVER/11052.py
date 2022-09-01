import sys
import math

input = sys.stdin.readline


def solution():

    N = int(input())
    price = [0] + list(map(int, input().split()))
    dp = [0 for _ in range(N + 1)]
    dp[1] = price[1]

    for i in range(2, N + 1):
        dp[i] = price[i]
        for j in range(1, i):
            dp[i] = max(dp[i], dp[i - j] + dp[j])

    print(dp[N])


solution()
