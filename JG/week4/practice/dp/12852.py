import sys

input = sys.stdin.readline


def solution():
    N = int(input())
    dp = [[0, 0] for _ in range(N + 1)]
    odr_list = [0 for _ in range(N + 1)]

    for idx in range(2, N + 1):
        dp[idx][0] = dp[idx - 1][0] + 1
        dp[idx][1] = idx - 1

        if idx % 2 == 0:
            if dp[idx//2][0] + 1 < dp[idx][0]:
                dp[idx][1] = idx // 2
            dp[idx][0] = min(dp[idx][0], dp[idx//2][0] + 1)

        if idx % 3 == 0:
            if dp[idx//3][0] + 1 < dp[idx][0]:
                dp[idx][1] = idx // 3
            dp[idx][0] = min(dp[idx][0], dp[idx//3][0] + 1)

    print(dp[N][0])

    n = N
    print(N, end=' ')
    for _ in range(dp[n][0]):
        print(dp[n][1], end=' ')
        n = dp[n][1]


solution()
