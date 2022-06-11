# ref: https://s0ng.tistory.com/entry/DFSBFS-알고리즘-미로-탈출-파이썬python

import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())

_map = []
for _ in range(N):
    _map.append(list(map(int, input().rstrip())))


def bfs(cur_x, cur_y):
    queue = deque()
    queue.append((cur_x, cur_y))

    while queue:
        x, y = queue.popleft()

        for idx in range(4):
            px, py = x + dx[idx], y + dy[idx]
            if 0 <= px < N and 0 <= py < M:
                if _map[px][py] == 1:
                    queue.append((px, py))
                    _map[px][py] = _map[x][y] + 1

    return _map[-1][-1]


def solution():
    print(bfs(0, 0))


solution()