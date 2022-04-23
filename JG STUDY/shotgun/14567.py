import enum
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())


def solution():

    graph = [[] for _ in range(n + 1)]
    indegree = [0 for _ in range(n + 1)]
    answer = [0 for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1

    q = deque()

    for idx, cnt in enumerate(indegree):
        if idx == 0:
            continue
        if cnt == 0:
            answer[idx] = 1
            q.append([idx, 1])

    while q:
        cur, cnt = q.popleft()
        for node in graph[cur]:
            indegree[node] -= 1
            answer[node] = cnt + 1
            if indegree[node] == 0:
                q.append([node, cnt + 1])

    print(*answer[1:])


solution()