import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**8)

M, N = map(int, input().split())  # 지도의 세로 크기 M / 가로 크기 N
_map = [[num for num in list(map(int, input().split()))]
        for _ in range(M)]  # 지도
dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]
visited = [[-1 for _ in range(N)] for _ in range(M)]


def dfs(x, y):
    if x == M - 1 and y == N - 1:
        return 1

    if visited[x][y] != -1:
        return visited[x][y]
    else:
        visited[x][y] = 0

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if _map[nx][ny] < _map[x][y]:
                visited[x][y] += dfs(nx, ny)

    return visited[x][y]


def solution():
    print(dfs(0, 0))


solution()
