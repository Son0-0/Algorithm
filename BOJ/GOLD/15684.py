import sys

input = sys.stdin.readline

n, m, h = map(int, input().split())
_map = [[0 for _ in range(n)] for _ in range(h)]
for _ in range(m):
    a, b = map(int, input().split())
    _map[a - 1][b - 1] = 1

answer = 4


def is_valid():
    for i in range(n):
        pos = i
        for j in range(h):
            if _map[j][pos] == 1:
                pos += 1
            elif 0 < pos and _map[j][pos - 1] == 1:
                pos -= 1

        if pos != i:
            return False
    return True


def dfs(cx, cy, cnt):
    global answer

    if answer <= cnt or 3 < cnt:
        return

    if is_valid():
        answer = min(answer, cnt)
        return

    for i in range(cx, h):
        temp = 0
        if i == cx:
            temp = cy
        for j in range(temp, n - 1):
            if _map[i][j] == 0:
                _map[i][j] = 1
                dfs(i, j + 2, cnt + 1)
                _map[i][j] = 0


def solution():

    dfs(0, 0, 0)

    if answer == 4:
        print(-1)
    else:
        print(answer)


solution()
