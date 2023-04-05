import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
flist = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    flist[a].append(b)
    flist[b].append(a)


def bfs(v):
    visited = [0 for _ in range(N + 1)]
    visited[v] = 0
    q = deque()
    q.append((v, 0))

    while q:
        cur, cnt = q.popleft()
        for i in flist[cur]:
            if visited[i] == 0:
                visited[i] = cnt + 1
                q.append((i, cnt + 1))

    visited[v] = 0
    return v, sum(visited)


def solution():
    result = []
    for idx in range(1, N + 1):
        a, b = bfs(idx)
        result.append((b, a))
    print(sorted(result)[0][1])


solution()