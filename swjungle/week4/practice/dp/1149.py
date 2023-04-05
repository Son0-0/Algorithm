# 3
# 26 40 83
# 49 60 57
# 13 89 99

import sys

input = sys.stdin.readline

INF = sys.maxsize

N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]

# 1. 1번 집의 색은 2번 집의 색과 같지 않아야 한다.
# 2. N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
# i번 집의 색은 i-1, i+1번 집의 색과 같지 않아야 한다.


def solution():
    dp = [[INF for _ in range(N + 1)] for _ in range(4)]

    for col in range(1, N + 1):
        for row in range(1, 4):
            if col == 1:
                dp[row][col] = house[col - 1][row - 1]
                continue
            if row == 1:
                dp[row][col] = min(dp[2][col - 1] + house[col - 1]
                                   [row - 1], dp[3][col - 1] + house[col - 1][row - 1])
            elif row == 2:
                dp[row][col] = min(dp[1][col - 1] + house[col - 1]
                                   [row - 1], dp[3][col - 1] + house[col - 1][row - 1])
            else:
                dp[row][col] = min(dp[1][col - 1] + house[col - 1]
                                   [row - 1], dp[2][col - 1] + house[col - 1][row - 1])

    result = sys.maxsize
    for d in dp:
        result = min(result, d[N])

    print(result)


solution()