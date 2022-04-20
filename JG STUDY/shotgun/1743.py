import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**8)

N, M, K = map(int, input().split())
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
_map = [[0 for _ in range(M)] for _ in range(N)]
for _ in range(K):
    x, y = map(int, input().split())
    _map[x-1][y-1] = 1
size = 0


def dfs(cx, cy):
    global size

    for i in range(4):
        nx, ny = cx + dx[i], cy + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if _map[nx][ny] == 1:
                _map[nx][ny] = 0
                size += 1
                dfs(nx, ny)


def solution():
    global size

    answer = 0
    for row in range(N):
        for col in range(M):
            if _map[row][col] == 1:
                _map[row][col] = 0
                size += 1
                dfs(row, col)
                answer = max(answer, size)
                size = 0

    print(answer)


solution()