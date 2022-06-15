# https://leetcode.com/problems/network-delay-time/
import sys
from collections import deque

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        q = deque()
        
        visited = [sys.maxsize for _ in range(n + 1)]
        graph = [[] for _ in range(n + 1)]
        for node in times:
            graph[node[0]].append([node[1], node[2]])
            if node[0] == k:
                q.append([k, 0])
        
        while q:
            cur, time = q.popleft()
            if time < visited[cur]:
                visited[cur] = time
                for node in graph[cur]:
                    q.append([node[0], time + node[1]])
                    
        answer = max(visited[1:])
        return answer if answer < sys.maxsize else -1