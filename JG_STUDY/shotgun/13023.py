import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(cur, length, visited=[]):
    if length == 5:
        print('1')
        exit(0)

    for node in graph[cur]:
        if node not in visited:
            dfs(node, length + 1, visited + [node])


def solution():
    for idx in range(n):
        dfs(idx, 1, [idx])

    print('0')


solution()