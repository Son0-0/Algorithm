import sys

input = sys.stdin.readline

size = int(input())
tri = [list(map(int, input().split())) for _ in range(size)]


def solution():

    dp = [[0 for _ in range(i + 1)] for i in range(size)]
    dp[0][0] = tri[0][0]

    for row in range(size - 1):
        for col in range(row + 1):
            dp[row + 1][col] = max(dp[row + 1][col],
                                   tri[row + 1][col] + dp[row][col])
            dp[row + 1][col + 1] = max(dp[row + 1][col + 1],
                                       tri[row + 1][col + 1] + dp[row][col])

    print(max(dp[size - 1]))

    return 0


solution()
