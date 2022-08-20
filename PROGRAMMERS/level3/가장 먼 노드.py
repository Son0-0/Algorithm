from collections import deque


def solution(n, edge):

    graph = [[] for _ in range(n + 1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    visited = [0 for _ in range(n + 1)]
    visited[1] = -1

    q = deque()
    q.append([1, 0])

    while q:
        cur, cnt = q.popleft()
        for node in graph[cur]:
            if visited[node] == 0:
                visited[node] = cnt + 1
                q.append([node, cnt + 1])

    return visited.count(max(visited))


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))

# def solution(n, edge):

#   graph = [[] for _ in range(n + 1)]
#   for a, b in edge:
#     graph[a].append(b)
#     graph[b].append(a)

#   node_list = [20001 for _ in range(n + 1)]

#   def dfs(cur, count, visited = []):
#     for node in graph[cur]:
#       if not node in visited:
#         node_list[node] = min(node_list[node], count + 1)
#         dfs(node, count + 1, visited + [node])

#   dfs(1, 0, [1])

#   return node_list.count()
