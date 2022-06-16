# dfs로 안풀림

import sys
from collections import deque

input = sys.stdin.readline
# sys.setrecursionlimit(10**8)

n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

# max_value = 0
# cur_area = 0


# def dfs(cx, cy):
#     global cur_area
#     cur_area += 1

#     for i in range(4):
#         nx, ny = cx + dx[i], cy + dy[i]
#         if 0 <= nx < n and 0 <= ny < m:
#             if paper[nx][ny] == 1:
#                 paper[nx][ny] = 0
#                 dfs(nx, ny)

def bfs(x, y):
    area = 1
    q = deque()
    q.append([x, y])

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if paper[nx][ny] == 1:
                    paper[nx][ny] = 0
                    q.append([nx, ny])
                    area += 1

    return area


def solution():

    answer = 0
    cnt = 0
    for row in range(n):
        for col in range(m):
            if paper[row][col] == 1:
                paper[row][col] = 0
                answer = max(answer, bfs(row, col))
                cnt += 1

    print(f"{cnt}\n{answer}")


solution()