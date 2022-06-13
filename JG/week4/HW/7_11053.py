# O(n^2)

import sys

input = sys.stdin.readline

def solution():
    N = int(input())  # 수열 A의 크기
    num = list(map(int, input().split()))  # 수열 A
    dp = [1 for _ in range(N)]

    for i in range(N):
        for j in range(i):
            if num[j] < num[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(max(dp))


solution()