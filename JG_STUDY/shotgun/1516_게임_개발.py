import sys
from collections import deque

input = sys.stdin.readline


def solution():

    n = int(input())

    graph = [[] for _ in range(n + 1)]
    indegree = [0 for _ in range(n + 1)]
    time = [0 for _ in range(n + 1)]

    for idx in range(1, n + 1):
        _input = list(map(int, input().split()))
        time[idx] = _input[0]

        for node in _input[1:-1]:
            graph[node].append(idx)
            indegree[idx] += 1

    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    answer = [0 for _ in range(n + 1)]
    while q:
        cur = q.popleft()
        answer[cur] += time[cur]
        for node in graph[cur]:
            indegree[node] -= 1
            answer[node] = max(answer[node], answer[cur])
            if indegree[node] == 0:
                q.append(node)

    print(*answer[1:], sep='\n')

    return 0


solution()