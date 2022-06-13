import sys

input = sys.stdin.readline

n = int(input())
wlist = [0] + [int(input()) for _ in range(n)]


def solution():
    dp = [0 for _ in range(n + 1)]
    dp[1] = wlist[1]
    if 1 < n:
        dp[2] = wlist[1] + wlist[2]

    for idx in range(3, n + 1):
        dp[idx] = max(dp[idx - 3] + wlist[idx - 1] +
                      wlist[idx], dp[idx - 2] + wlist[idx], dp[idx - 1])

    print(dp[n])


solution()