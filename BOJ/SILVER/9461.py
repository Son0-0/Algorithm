import sys

input = sys.stdin.readline


def solution():
    temp = [0 for _ in range(91)]

    dp = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
    dp += temp

    for _ in range(int(input())):
        n = int(input())
        if dp[n] != 0:
            print(dp[n])
        else:
            for idx in range(11, n + 1):
                dp[idx] = dp[idx - 2] + dp[idx - 3]
            print(dp[n])


solution()
