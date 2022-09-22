import sys

input = sys.stdin.readline

a = input().strip()
b = input().strip()


def solution():
    la, lb = len(a), len(b)
    dp = [[0 for _ in range(lb + 1)] for _ in range(la + 1)]
    answer = 0

    for i in range(1, la + 1):
        for j in range(1, lb + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                answer = max(answer, dp[i][j])

    print(answer)


solution()
