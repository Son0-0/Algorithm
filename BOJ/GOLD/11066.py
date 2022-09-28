import sys

input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))


def solution():

    dp = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1

    for i in range(n - 1):
        if num[i] == num[i + 1]:
            dp[i][i + 1] = 1

    for i in range(2, n):
        for j in range(n - i):
            if num[j] == num[j + i] and dp[j + 1][j + i - 1] == 1:
                dp[j][i + j] = 1

    for _ in range(int(input())):
        s, e = map(int, input().split())
        print(dp[s - 1][e - 1])


solution()
