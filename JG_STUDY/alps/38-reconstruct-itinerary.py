# https://leetcode.com/problems/reconstruct-itinerary
import sys
from collections import defaultdict

sys.setrecursionlimit(10**8)

class Solution:
    def __init__(self):
        self.answer = []
        
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        graph = defaultdict(list)
        for s, d in tickets:
            graph[s].append(d)
            graph[s].sort(reverse = True)
        
        def dfs(cur):
            if cur in graph:
                while graph[cur]:
                    dfs(graph[cur].pop())
            self.answer.append(cur)
            

        dfs("JFK")
        
        return self.answer[::-1]
