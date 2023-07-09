import sys
from collections import deque

input = sys.stdin.readline

size = int(input())
graph = [[] for _ in range(size + 1)]

for _ in range(int(input())):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def solution():
    visited = [0 for _ in range(size + 1)]
    visited[1] = 1

    q = deque()
    q.append(1)

    while q:
        cur = q.pop()

        for node in graph[cur]:
            if visited[node] == 0:
                visited[node] = 1
                q.append(node)

    print(sum(visited) - 1)


solution()
