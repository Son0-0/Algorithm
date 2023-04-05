import sys

input = sys.stdin.readline

N = int(input())
list_a = sorted(list(map(int, input().split())))
list_b = sorted(list(map(int, input().split())), reverse=True)


def solution():
    result = 0
    for idx in range(N):
        result += list_a[idx] * list_b[idx]

    print(result)


solution()