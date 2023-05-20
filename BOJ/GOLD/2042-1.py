import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
nums = [int(input()) for _ in range(N)]

tree = [0 for _ in range(2 * N + 1)]


def buildTree():
    # leaf node
    for i in range(N):
        tree[i + N] = nums[i]

    # parent node
    for i in range(N - 1, 0, -1):
        tree[i] = tree[2 * i] + tree[2 * i + 1]


def updateTree(index, newValue):
    tree[index + N] = newValue
    i = index + N

    while i > 1:
        tree[i >> 1] = tree[i] + tree[i ^ 1]
        i >>= 1


def calcTree(l, r):
    sum = 0

    l += N
    r += N

    while l < r:
        if (l & 1) > 0:
            sum += tree[l]
            l += 1
        if (r & 1) > 0:
            r -= 1
            sum += tree[r]

        l //= 2
        r //= 2

    return sum


def solution():
    buildTree()

    for _ in range(M + K):
        cmd, p, q = map(int, input().split())

        if cmd == 1:
            updateTree(p - 1, q)
        else:
            print(calcTree(p - 1, q))


solution()
