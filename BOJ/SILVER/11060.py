import sys
from collections import deque


input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))


def solution():

    q = deque()
    dp = [1e9 for _ in range(n)]
    dp[0] = 0

    q.append((0, 0))

    while q:
        cx, cc = q.popleft()
        if num[cx] == 0:
            continue
        for i in range(1, num[cx] + 1):
            nx = cx + i
            if 0 <= nx < n and cc + 1 < dp[nx]:
                dp[nx] = cc + 1
                q.append([nx, cc + 1])

    if dp[n - 1] == 1e9:
        print(-1)
    else:
        print(dp[n - 1])


solution()
