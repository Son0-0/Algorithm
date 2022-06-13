import sys

input = sys.stdin.readline


def solution():
    N = int(input())
    llist = []

    for _ in range(N):
        a, b = map(int, input().split())
        llist.append((a, b))
    llist.sort()
    llist.sort(key=lambda x: x[1])

    result = [(0, 0)]
    for s, e in llist:
        if result[-1][1] <= s:
            result.append((s, e))
    print(len(result) - 1)


solution()