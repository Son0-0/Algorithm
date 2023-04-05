import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**8)

size = int(input())
_map = [[num for num in list(map(int, input().split()))] for _ in range(size)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, h, mmap):
    mmap[x][y] = -1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < size and 0 <= ny < size:
            if h < mmap[nx][ny]:
                dfs(nx, ny, h, mmap)


def solution():
    max_v = -sys.maxsize - 1
    min_v = sys.maxsize

    for m in _map:
        max_v = max(max_v, max(m))
        min_v = min(min_v, min(m))

    count = 0
    for num in range(min_v - 1, max_v):
        temp = [[num for num in mmap] for mmap in _map]
        cnt = 0
        for row in range(size):
            for col in range(size):
                if num < temp[row][col]:
                    dfs(row, col, num, temp)
                    cnt += 1

        if count < cnt:
            count = cnt

    print(count)


solution()