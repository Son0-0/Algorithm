import sys

input = sys.stdin.readline

N, M = map(int, input().split())
llist = [int(input()) for _ in range(M)]
MAX = 10001


def solution():
    dp = [[MAX] * (int((2 * N)**0.5) + 2) for _ in range(N + 1)]
    dp[1][0] = 0

    for i in range(2, N + 1):
        if i in llist:
            continue
        for j in range(1, int((2*i)**0.5) + 1):
            dp[i][j] = min(dp[i - j][j - 1], dp[i - j]
                           [j], dp[i - j][j + 1]) + 1

    result = min(dp[N])
    print(-1) if result == MAX else print(result)


solution()
