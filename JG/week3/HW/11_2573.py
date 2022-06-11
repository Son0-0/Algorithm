import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**8)

h, w = map(int, input().split())
_map = [[num for num in list(map(int, input().split()))] for _ in range(h)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
mlist = []


def dfs(x, y, temp_map):
    global mlist
    melt = 0
    temp_map[x][y] = -1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < h and 0 <= ny < w:
            if _map[nx][ny] == 0:
                melt += 1
            if 0 < temp_map[nx][ny]:
                dfs(nx, ny, temp_map)

    mlist.append((x, y, melt))

    return temp_map


def solution():
    day = 0
    while True:
        lsum = 0
        for m in _map:
            lsum += sum(m)
        if lsum == 0:
            return print(0)

        temp = [[num for num in mm] for mm in _map]
        cnt = 0
        for row in range(h):
            for col in range(w):
                if 0 < temp[row][col]:
                    temp = dfs(row, col, temp)
                    cnt += 1
                if 2 <= cnt:
                    return print(day)

        day += 1

        for x, y, sub in mlist:
            if _map[x][y] - sub <= 0:
                _map[x][y] = 0
            else:
                _map[x][y] -= sub
        mlist.clear()


solution()