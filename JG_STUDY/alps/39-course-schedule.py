# https://leetcode.com/problems/course-schedule/
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        q = deque()
        for idx, cnt in enumerate(indegree):
            if cnt == 0:
                q.append(idx)
        
        cnt = 0
        while q:
            cur = q.popleft()
            cnt += 1
            for idx in graph[cur]:
                indegree[idx] -= 1
                if indegree[idx] == 0:
                    q.append(idx)
                
        if cnt == numCourses:
            return True
        return False
            
