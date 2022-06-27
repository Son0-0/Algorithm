# https://www.acmicpc.net/problem/3109
import sys

input = sys.stdin.readline

r, c = map(int, input().split())
_map = [list(map(str, input().strip())) for _ in range(r)]
visited = [[0 for _ in range(c)] for _ in range(r)]
dx, dy = [-1, 0, 1], [1, 1, 1]
cnt = 0


def dfs(cx, cy):
    if cy == (c - 1):
        return True

    for idx in range(3):
        nx, ny = cx + dx[idx], cy + dy[idx]
        if 0 <= nx < r and 0 <= ny < c:
            if visited[nx][ny] == 0 and _map[nx][ny] == '.':
                visited[nx][ny] = 1
                tf = dfs(nx, ny)
                if tf == True:
                    return True
    return False


def solution():
    global cnt

    for idx in range(r):
        if _map[idx][0] == '.':
            tf = dfs(idx, 0)
            if tf == True:
                cnt += 1

    print(cnt)


solution()
