import sys

input = sys.stdin.readline

size = int(input())
slist = [0] + [int(input()) for _ in range(size)]


def solution():
    dp = [0 for _ in range(size + 1)] # 전칸 전전칸만 선언해서 공간을 줄일 수 있다.
    dp[1] = slist[1]
    if 1 < size:
        dp[2] = slist[1] + slist[2]

    for idx in range(3, size + 1):
        dp[idx] = max(dp[idx - 3] + slist[idx - 1] +
                      slist[idx], dp[idx - 2] + slist[idx])

    print(dp[size])


solution()