import sys

input = sys.stdin.readline

n = int(input())
tri = [list(map(int, input().split())) for _ in range(n)]


def solution():
    dp = [num for num in tri]

    for h in range(1, n):
        for w in range(len(tri[h])):
            if w == 0:
                dp[h][w] += dp[h - 1][w]
            elif w == len(tri[h]) - 1:
                dp[h][w] += dp[h - 1][w - 1]
            else:
                if h == 1:
                    dp[h][w] += dp[h - 1][w - 1]
                else:
                    dp[h][w] += max(dp[h - 1][w], dp[h - 1][w - 1])

    print(max(dp[n - 1]))


solution()