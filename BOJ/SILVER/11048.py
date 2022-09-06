import sys


def solution():

    n, m = map(int, input().split())
    jmap = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0 for _ in range(m)] for _ in range(n)]
    dp[0][0] = jmap[0][0]

    dx, dy = [-1, -1, 0], [0, -1, -1]
    for i in range(n):
        for j in range(m):
            for k in range(3):
                nx, ny = i + dx[k], j + dy[k]
                if 0 <= nx < n and 0 <= ny < m:
                    dp[i][j] = max(dp[i][j], dp[nx][ny] + jmap[i][j])

    print(dp[n - 1][m - 1])


solution()
