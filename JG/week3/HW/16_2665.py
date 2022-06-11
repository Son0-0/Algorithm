import sys
import heapq

input = sys.stdin.readline

size = int(input())
_map = [[room for room in list(map(int, input().rstrip()))]
        for _ in range(size)]
visited = [[0 for _ in range(size)] for _ in range(size)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def bfs(x, y):
    queue = []
    heapq.heappush(queue, (0, x, y))

    while queue:
        cnt, cur_x, cur_y = heapq.heappop(queue)
        if cur_x == size - 1 and cur_y == size - 1:
            return cnt
        if visited[cur_x][cur_y] == 0:
            visited[cur_x][cur_y] = 1
            for i in range(4):
                nx, ny = cur_x + dx[i], cur_y + dy[i]
                if 0 <= nx < size and 0 <= ny < size:
                    if _map[nx][ny] == 1:
                        heapq.heappush(queue, (cnt, nx, ny))
                    if _map[nx][ny] == 0:
                        heapq.heappush(queue, (cnt + 1, nx, ny))


def solution():
    print(bfs(0, 0))


solution()
