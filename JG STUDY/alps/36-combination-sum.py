# https://leetcode.com/problems/combination-sum
class Solution:
    def __init__(self):
        self.answer = []
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def dfs(cur, nsum, visited = []):
            if nsum == target:
                self.answer.append(visited)
                return
            elif target < nsum:
                return
            
            for idx in range(cur, len(candidates)):
                dfs(idx, nsum + candidates[idx], visited + [candidates[idx]])
                
        dfs(0, 0, [])
            
        return self.answer
