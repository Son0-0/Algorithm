import sys

input = sys.stdin.readline
from collections import deque

N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N + 1):
    graph[i].sort()


def solution():
    visited = [0 for _ in range(N + 1)]

    q = deque()
    q.append(R)
    visited[R] = 1

    cnt = 2
    while q:
        cur = q.popleft()

        for node in graph[cur]:
            if visited[node] == 0:
                visited[node] = cnt
                cnt += 1
                q.append(node)

    print(*visited[1:], sep="\n")

    return


solution()
