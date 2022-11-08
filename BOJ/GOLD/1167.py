import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = dict()
    
for _ in range(n):
    ipt = list(map(int, input().split()))
    node = ipt[0]
    graph[node] = dict()
    
    ipt.pop()
    
    for i in range(1, len(ipt), 2):
        graph[node][ipt[i]] = ipt[i + 1]

answer = -1

def bfs(node):
    global answer, n
    
    q = deque()
    q.append([node, 0])
    
    v = set()
    v.add(node)
    
    mv, ml = 0, -1
    
    while q:
        cur, d = q.popleft()
        for j in graph[cur]:
            if j not in v:
                dis = d + graph[cur][j]
                v.add(j)
                if mv < dis:
                    mv = dis
                    ml = j
                q.append([j, dis])
        
    answer = max(answer, mv)
        
    return ml

def solution():
    
    target = bfs(1)
    _ = bfs(target)
    
    print(answer)
        
solution()