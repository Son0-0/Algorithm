import sys

input = sys.stdin.readline


def solution():
    N, K = map(int, input().split())
    purse = []

    for _ in range(N):
        purse.append(int(input()))

    result = 0
    for coin in purse[::-1]:
        if coin <= K:
            result += K // coin
            K %= coin

    print(result)


solution()