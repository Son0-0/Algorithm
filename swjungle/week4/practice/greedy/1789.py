import sys

input = sys.stdin.readline

N = int(input())


def solution():
    n = 0
    while (n * (n + 1) // 2) <= N:
        n += 1
    print(n - 1)


solution()
