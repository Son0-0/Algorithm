import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**8)

size = int(input())
_map = [list(map(int, input().split())) for _ in range(size)]
visited = [[-1 for _ in range(size)] for _ in range(size)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def dfs(row, col):
    if visited[row][col] == -1:
        visited[row][col] = 0

        for i in range(4):
            nr, nc = row + dx[i], col + dy[i]
            if 0 <= nr < size and 0 <= nc < size and _map[row][col] < _map[nr][nc]:
                visited[row][col] = max(visited[row][col], dfs(nr, nc))

    return visited[row][col] + 1


def solution():
    result = 0

    for row in range(size):
        for col in range(size):
            result = max(result, dfs(row, col))

    print(result)


solution()