import sys

input = sys.stdin.readline


def solution():
    size = int(input())
    dp = [0 for _ in range(size + 1)]
    llist = [0]
    for _ in range(size):
        llist.append(int(input()))

    if size == 1:
        print(llist[1])
        return

    dp[1] = llist[1]
    dp[2] = llist[1] + llist[2]

    for i in range(3, size + 1):
        dp[i] = max(dp[i - 3] + llist[i - 1] + llist[i], dp[i - 2] + llist[i])

    print(dp[size])


solution()