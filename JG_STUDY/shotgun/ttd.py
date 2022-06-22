# n: 노드 수
# s: 시작 지점
# a: a 도착 지점 / b: b 도착 지점
import sys

def solution(n, s, a, b, fares):
    answer = 0
    
    graph = [[] for _ in range(n + 1)]
    for fare in fares:
        graph[fare[0]].append([fare[1], fare[2]])
        graph[fare[1]].append([fare[0], fare[2]])
    
    min_fee_a = sys.maxsize
    min_route_b = [sys.maxsize for _ in range(n + 1)]
    def dfs(strt, cur, fee, dst, visited = [], fee_list = []):
        nonlocal min_fee_a, min_route_b
        
        if dst == b and cur == dst:
            min_route_b[strt] = min(min_route_b[strt], fee)
            return
        
        if dst == a and cur == dst:
            for idx, n in enumerate(visited):
                if min_route_b[idx] == sys.maxsize:
                    dfs(n, n, 0, b, [n], [0])
                min_fee_a = min(min_fee_a, fee + min_route_b[n])
            return 
        
        for node in graph[cur]:
            if node[0] not in visited:
                dfs(strt, node[0], fee + node[1], dst, visited + [node[0]], fee_list + [fee + node[1]])
    
    dfs(None, s, 0, a, [s], [0])
    
    return min_fee_a
  
a = solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]])
print(a)