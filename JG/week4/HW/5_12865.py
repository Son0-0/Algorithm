import sys

input = sys.stdin.readline

N, K = map(int, input().split())


def solution():
    bag = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
    items = []

    for _ in range(N):
        w, v = map(int, input().split())
        items.append((w, v))

    for i, item in enumerate(items):
        for idx in range(1, K + 1):
            if item[0] <= idx:
                bag[i + 1][idx] = max(bag[i][idx], bag[i][idx - item[0]] + item[1])
            else:
                bag[i + 1][idx] = bag[i][idx]

    print(bag[-1][-1])


solution()