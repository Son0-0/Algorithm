import sys

input = sys.stdin.readline


def solution():
    for _ in range(int(input())):  # tc input

        size = int(input())
        llist = []

        for _ in range(size):
            a, b = map(int, input().split())
            llist.append((a, b))
        llist.sort()

        result = [(size + 1, size + 1)]
        for p in llist:
            if p[1] < result[-1][1]:
                result.append(p)

        print(len(result) - 1)


solution()