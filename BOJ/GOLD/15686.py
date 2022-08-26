import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())

_map = [list(map(int, input().split())) for _ in range(N)]


def solution():
    answer = 1e9
    clist = []
    hlist = []

    for idx, m in enumerate(_map):
        for i, j in enumerate(m):
            if j == 2:
                clist.append([idx + 1, i + 1])
            elif j == 1:
                hlist.append([idx + 1, i + 1])

    length = len(hlist)
    for nlist in list(combinations(range(1, len(clist) + 1), M)):
        dlist = [1e9 for _ in range(length)]
        for idx, h in enumerate(hlist):
            for i, c in enumerate(clist):
                if (i + 1) in nlist:
                    dlist[idx] = min(dlist[idx], abs(
                        h[0] - c[0]) + abs(h[1] - c[1]))

        answer = min(answer, sum(dlist))

    print(answer)


solution()
