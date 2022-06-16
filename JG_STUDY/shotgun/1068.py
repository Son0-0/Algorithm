import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n = int(input())
graph = [[] for _ in range(n)]
strt = 0

for idx, _ in enumerate(list(map(int, input().split()))):
    if _ != -1:
        graph[_].append(idx)
    else:
        strt = idx
target = int(input())
result = []


def dfs(cur):
    if cur == target:
        return

    flag = 0

    for node in graph[cur]:
        if node == target: continue
        flag = 1
        dfs(node)
        

    if flag == 0:
        result.append(cur)


def solution():
    for node in graph[target]:
        graph[node].clear()
    graph[target].clear()
    
    dfs(strt)
    print(len(result))


solution()