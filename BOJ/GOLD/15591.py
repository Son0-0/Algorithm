import sys
from collections import deque

input = sys.stdin.readline

n, q = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])


def solution():
    answer = []

    for _ in range(q):
        k, v = map(int, input().split())
        visited = [0 for _ in range(n + 1)]
        visited[v] = 1
        queue = deque()
        queue.append((v, sys.maxsize))
        cnt = 0
        while queue:
            cx, cu = queue.popleft()
            for nx, nu in graph[cx]:
                mu = min(cu, nu)
                if k <= mu and visited[nx] == 0:
                    visited[nx] = 1
                    queue.append((nx, mu))
                    cnt += 1

        answer.append(cnt)

    print(*answer, sep='\n')

    return 0


solution()
