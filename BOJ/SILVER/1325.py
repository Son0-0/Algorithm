import sys
from collections import deque, defaultdict

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)


def bfs(cur):
    cnt = 1
    q = deque()
    visited = [0 for _ in range(n + 1)]
    visited[cur] = 1

    q.append(cur)

    while q:
        c = q.popleft()
        for node in graph[c]:
            if visited[node] == 0:
                cnt += 1
                visited[node] = 1
                q.append(node)

    return cnt


def solution():
    max_idx = 0
    max_value = defaultdict(list)

    for idx in range(1, n + 1):
        return_idx = bfs(idx)
        max_idx = max(return_idx, max_idx)
        max_value[return_idx].append(idx)

    print(*sorted(max_value[max_idx]))

    return 0


solution()
