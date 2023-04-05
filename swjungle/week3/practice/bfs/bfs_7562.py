import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]


def bfs(cur_x, cur_y, target_x, target_y, size):
    visited = [[0 for _ in range(size)] for _ in range(size)]
    queue = deque()
    queue.append((cur_x, cur_y, 0))

    while queue:
        x, y, cnt = queue.popleft()
        if x == target_x and y == target_y:
            return cnt
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < size and 0 <= ny < size and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny, cnt + 1))


def solution():
    size = int(input())
    for _ in range(size):
        msize = int(input())
        _map = [[0 for _ in range(msize)] for _ in range(msize)]
        cur_x, cur_y = map(int, input().split())
        target_x, target_y = map(int, input().split())
        print(bfs(cur_x, cur_y, target_x, target_y, msize))


solution()
