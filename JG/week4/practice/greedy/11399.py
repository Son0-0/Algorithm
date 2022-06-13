import sys

input = sys.stdin.readline

size = int(input())


def solution():
    llist = list(map(int, input().split()))
    llist.sort()

    result = 0
    for idx in range(size):
        result += sum(llist[0:idx + 1])

    print(result)


solution()