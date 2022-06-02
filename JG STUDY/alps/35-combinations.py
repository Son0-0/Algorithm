# https://leetcode.com/problems/combinations
class Solution:
    def __init__(self):
        self.answer = []
    
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def dfs(cur, length, visited = []):
            if length == k:
                if visited not in self.answer:
                    self.answer.append(visited)
            
            for num in range(cur, n + 1):
                if num == cur: continue
                if num not in visited:
                    dfs(num, length + 1, visited + [num])
                    
        dfs(0, 0, [])

        return self.answer