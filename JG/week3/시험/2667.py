import sys

input = sys.stdin.readline

size = int(input())
_map = [list(map(int, input().strip())) for _ in range(size)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
result = []


def dfs(x, y, cnt):
    _map[x][y] = -1

    for idx in range(4):
        nx, ny = x + dx[idx], y + dy[idx]
        if 0 <= nx < size and 0 <= ny < size and _map[nx][ny] == 1:
            cnt = dfs(nx, ny, cnt + 1)

    return cnt


def solution():
    cnt = 0

    for row in range(size):
        for col in range(size):
            if _map[row][col] == 1:
                result.append(dfs(row, col, 1))

    print(len(result))
    print(*sorted(result), sep="\n")


solution()