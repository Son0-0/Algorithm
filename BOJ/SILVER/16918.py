import sys
from collections import deque

input = sys.stdin.readline

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

r, c, n = map(int, input().split())

_map = [list(map(str, input().rstrip())) for _ in range(r)]


def bomb_position():
    temp = deque()
    for i in range(r):
        for j in range(c):
            if _map[i][j] == 'O':
                temp.append((i, j))
    return temp


def install():
    for i in range(r):
        for j in range(c):
            if _map[i][j] == '.':
                _map[i][j] = 'O'


def explosion(bomb):
    while bomb:
        x, y = bomb.popleft()
        _map[x][y] = '.'
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if _map[nx][ny] == 'O':
                    _map[nx][ny] = '.'


def solution():
    global n

    # 다음 1초 동안 봄버맨은 아무것도 하지 않는다.
    n -= 1

    while n != 0:
        # 폭탄 위치 파악
        bomb = bomb_position()

        # 폭탄 설치
        install()

        n -= 1
        if n == 0:
            break

        # 폭발
        explosion(bomb)
        n -= 1

    for m in _map:
        print(*m, sep='')

    return 0


solution()
