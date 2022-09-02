import sys

input = sys.stdin.readline


def solution():

    n, m = map(int, input().split())

    s = dict()
    for _ in range(n):
        s[input().strip()] = 1

    answer = 0
    for _ in range(m):
        target = input().strip()
        if target in s:
            answer += 1

    print(answer)


solution()
