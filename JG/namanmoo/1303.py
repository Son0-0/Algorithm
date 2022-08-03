import sys

r, c = map(int, input().split())
_map = [list(map(str, input().strip())) for _ in range(c)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
cnt = 1


def dfs(x, y, cur):
    global cnt

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < c and 0 <= ny < r:
            if _map[nx][ny] == cur:
                _map[nx][ny] = 'A'
                cnt += 1
                dfs(nx, ny, cur)


def solution():
    global cnt

    answer = {
        'W': 0,
        'B': 0
    }

    for x in range(c):
        for y in range(r):
            if _map[x][y] != 'A':
                cur = _map[x][y]
                _map[x][y] = 'A'
                dfs(x, y, cur)
                answer[cur] += cnt**2
                cnt = 1

    for key, value in answer.items():
        print(value)

    return 0


solution()