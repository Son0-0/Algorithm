import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

n = int(input())
pnum = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
for i in range(n):
    for idx, dst in enumerate(list(map(int, input().split()))):
        if idx == 0:
            continue
        graph[i+1].append(dst)


def bfs(comb):
    q = deque([comb[0]])
    visited = set([comb[0]])

    cnt, psum = 1, 0
    while q:
        cur = q.popleft()
        psum += pnum[cur]
        for node in graph[cur]:
            if node not in visited and node in comb:
                q.append(node)
                visited.add(node)
                cnt += 1

    if cnt == len(comb):
        return psum
    return 0


def solution():
    answer = 1e9

    target = sum(pnum)

    for i in range(1, n // 2 + 1):
        for comb in list(combinations(range(1, n + 1), i)):
            s1, s2 = bfs(comb), bfs(
                [num for num in range(1, n + 1) if num not in comb])
            if target == (s1 + s2):
                answer = min(answer, abs(s1 - s2))

    if answer != 1e9:
        print(answer)
    else:
        print(-1)


solution()
