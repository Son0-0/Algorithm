import sys

input = sys.stdin.readline

h, w, x, y = map(int, input().split())
a, b = [], []
for i in range(h + x):
    temp = list(map(int, input().split()))
    if i == 0:
        a.append(temp[:w])
    b.append(temp)


def solution():

    for i in range(1, h):
        a.append([])
        for j in range(w):
            # case 1
            if x <= i < h and y <= j < w:
                val = b[i][j] - a[i-x][j-y]
            # case 3 - 1
            elif 0 <= i < h and 0 <= j < w:
                val = b[i][j]
            elif x <= i < h + x - 1 and y <= j < w + y - 1:
                val = b[i][j]

            a[i].append(val)

    for value in a:
        print(*value)

    return 0


solution()
