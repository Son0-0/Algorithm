import sys

input = sys.stdin.readline

size = int(input())
llist = []
for _ in range(size):
    llist.append(int(input()))
llist.sort()


def solution():
    max_value = 0
    for idx in range(size):
        max_value = max(max_value, llist[idx] * (size - idx))

    print(max_value)


solution()