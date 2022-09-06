import sys

input = sys.stdin.readline


def solution():

    for _ in range(int(input())):
        size = int(input())
        dp = []
        for _ in range(2):
            dp.append(list(map(int, input().split())))

        if size == 1:
            print(max(dp[0][0], dp[1][0]))
            continue

        dp[0][1] = dp[1][0] + dp[0][1]
        dp[1][1] = dp[0][0] + dp[1][1]

        for i in range(2, size):
            dp[0][i] = max(dp[1][i - 1], dp[1][i - 2]) + dp[0][i]
            dp[1][i] = max(dp[0][i - 1], dp[0][i - 2]) + dp[1][i]

        print(max(dp[0][size - 1], dp[1][size - 1]))

    return 0


solution()
