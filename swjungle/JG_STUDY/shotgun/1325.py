import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n, m = map(int, input().split())
graph = {}

for _ in range(m):
    a, b = map(int, input().split())
    if b in graph:
        graph[b].append(a)
    else:
        graph[b] = [a]

max_value = 0
answer = {}


def dfs(strt, x, length, visited={}):
    global max_value

    visited[x] = 1

    if max_value <= length:
        max_value = length
        if length not in answer:
            answer[length] = [strt]
        else:
            answer[length].append(strt)

    if length == n:
        return

    if x in graph:
        for node in graph[x]:
            if node not in visited:
                visited[node] = 1
                dfs(strt, node, length + 1, visited)


def solution():
    global max_value

    for node in graph:
        dfs(node, node, 1, {})

    print(*sorted(list(set(answer[max_value]))))


solution()