import sys

input = sys.stdin.readline

n = int(input())
k = int(input())
answer = 0


def binary_search(left, right):
    global answer

    if right < left:
        return

    mid = (left + right) // 2
    count = 0

    for i in range(1, n + 1):
        count += min(mid // i, n)

    if k <= count:
        answer = mid
        binary_search(left, mid - 1)
    else:
        binary_search(mid + 1, right)


def solution():

    binary_search(0, k)
    print(answer)


solution()
