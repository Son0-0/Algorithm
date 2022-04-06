import sys

input = sys.stdin.readline

_map = [list(map(int, input().split())) for _ in range(5)]
result = []
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def dfs(x, y, num):
    if len(num) == 6:
        if num not in result:
            result.append(num)
        return

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, str(num) + str(_map[nx][ny]))


def solution():

    for row in range(5):
        for col in range(5):
            dfs(row, col, str(_map[row][col]))

    print(len(result))


solution()