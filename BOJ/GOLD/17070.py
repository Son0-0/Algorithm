import sys

input = sys.stdin.readline

n = int(input())
_map = [list(map(int, input().split())) for _ in range(n)]

# 가로 대각선 세로
dx, dy = [0, 1, 1], [1, 1, 0]

answer = 0


def dfs(cx, cy, cd):
    global answer
    if cx == n - 1 and cy == n - 1:
        answer += 1
        return

    if cd == 0 or cd == 1:  # 가로
        nx, ny = cx, cy + 1
        if 0 <= nx < n and 0 <= ny < n and _map[nx][ny] == 0:
            dfs(nx, ny, 0)
    if cd == 1 or cd == 2:  # 세로
        nx, ny = cx + 1, cy
        if 0 <= nx < n and 0 <= ny < n and _map[nx][ny] == 0:
            dfs(nx, ny, 2)
    if cd == 0 or cd == 1 or cd == 2:  # 대각선
        nx, ny = cx + 1, cy + 1
        if 0 <= nx < n and 0 <= ny < n and _map[nx][ny] == 0:
            if _map[nx][ny - 1] == 0 and _map[nx - 1][ny] == 0:
                dfs(nx, ny, 1)


def solution():

    dfs(0, 1, 0)  # 첫 번째 파이프 끝 부분

    print(answer)


solution()
