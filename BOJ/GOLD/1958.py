import sys

input = sys.stdin.readline

a = input().strip()
b = input().strip()
c = input().strip()


def solution():
    la, lb, lc = len(a), len(b), len(c)
    dp = [[[0 for _ in range(lc + 1)] for _ in range(lb + 1)]
          for _ in range(la + 1)]
    answer = 0

    for i in range(1, la + 1):
        for j in range(1, lb + 1):
            for k in range(1, lc + 1):
                if a[i - 1] == b[j - 1] and b[j - 1] == c[k - 1]:
                    dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
                else:
                    dp[i][j][k] = max(dp[i][j][k - 1], dp[i]
                                      [j - 1][k], dp[i - 1][j][k])

    for i in range(la + 1):
        for j in range(lb + 1):
            answer = max(answer, max(dp[i][j]))

    print(answer)


solution()
