# https://leetcode.com/problems/cheapest-flights-within-k-stops/
import sys
from collections import deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        q = deque()
        graph = [[] for _ in range(n)]
        for rc, st, time in flights:
            graph[rc].append([st, time])
            if rc == src:
                q.append([src, 0, 1])
    
        answer = sys.maxsize
        visited = [sys.maxsize for _ in range(n)]
        while q:
            cur, time, cnt = q.popleft()
            if cur == dst and cnt <= k + 2:
                answer = min(answer, time)
            if time < visited[cur]:
                visited[cur] = time
                for node in graph[cur]:
                    q.append([node[0], time + node[1], cnt + 1])
                
        return answer if answer < sys.maxsize else -1