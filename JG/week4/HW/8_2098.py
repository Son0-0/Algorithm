import sys

input = sys.stdin.readline

INF = 10**9

W = [[-1, -1, -1, -1, -1]]
for _ in range(int(input())):
    temp = [-1] + list(map(int, input().split()))
    for idx in range(len(temp)):
        if temp[idx] == 0:
            temp[idx] = INF
    W.append(temp)

for row in range(1, len(W)):
    for col in range(len(W)):
        if row == col:
            W[row][col] = 0


def count(A, n):
    count = 0
    for i in range(n):
        if ((A & (1 << i)) != 0):
            count += 1
    return count


def isIn(i, A):
    if ((A & (1 << (i - 2))) != 0):
        return True
    else:
        return False


def diff(A, j):
    t = 1 << (j - 2)
    return (A & (~t))


def minimum(W, D, i, A):
    minValue = INF
    minJ = 1
    n = len(W) - 1
    for j in range(2, n + 1):
        if (isIn(j, A)):
            m = W[i][j] + D[j][diff(A, j)]
            if (minValue > m):
                minValue = m
                minJ = j
    return minValue, minJ


def travel(W):
    n = len(W) - 1
    size = 2 ** (n - 1)
    D = [[0] * size for _ in range(n + 1)]
    P = [[0] * size for _ in range(n + 1)]
    for i in range(2, n + 1):
        D[i][0] = W[i][1]
    for k in range(1, n - 1):
        for A in range(1, size):
            if (count(A, n) == k):
                for i in range(2, n + 1):
                    if (not isIn(i, A)):
                        D[i][A], P[i][A] = minimum(W, D, i, A)
    A = size - 1
    D[1][A], P[1][A] = minimum(W, D, 1, A)
    return D, P


def solution():
    D, P = travel(W)

    print(D[1][2**(len(W)-2)-1])


solution()