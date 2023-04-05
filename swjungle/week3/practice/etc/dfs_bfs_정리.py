# ref: https://devyuseon.github.io/algorithm/dfs-and-bfs/

import sys
from collections import deque

input = sys.stdin.readline

graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3]
}


def recursive_dfs(v, visited=[]):
    visited.append(v)
    for w in graph[v]:
        if not w in visited:
            visited = recursive_dfs(w, visited)
    return visited


def bfs(start, visited=[]):
    visited = [start]
    queue = deque()
    queue.append(start)

    while queue:
        v = queue.popleft()
        for w in graph[v]:
            if not w in visited:
                visited.append(w)
                queue.append(w)

    return visited


def solution():
    print("recursive_dfs: ", recursive_dfs(1))
    print("bfs: ", bfs(1))


solution()
