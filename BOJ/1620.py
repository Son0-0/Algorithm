import sys

input = sys.stdin.readline

N, M = map(int, input().split())


def solution():
    pmon = dict()
    for idx in range(1, N + 1):
        pkm = input().strip()
        pmon[pkm] = idx
        pmon[str(idx)] = pkm

    answer = []
    for _ in range(M):
        target = input().strip()
        answer.append(pmon[target])

    print(*answer, sep='\n')


solution()