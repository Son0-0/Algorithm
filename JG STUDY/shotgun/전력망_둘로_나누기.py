def dfs(graph, start, visited = []):
    visited.append(start)
    
    for g in graph[start]:
        if g not in visited:
            dfs(graph, g, visited)
            
    return visited

def solution(n, wires):
    graph = [[] for _ in range(n + 1)]
    
    for w in wires:
        graph[w[0]].append(w[1])
        graph[w[1]].append(w[0])
    
    min_value = 101
    for x, y in wires:
        graph[x].remove(y)
        graph[y].remove(x)
        target = len(dfs(graph, x, []))
        min_value = min(min_value, abs(target - (n - target)))
        graph[x].append(y)
        graph[y].append(x)
        
    return min_value
  
print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))