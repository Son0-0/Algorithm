# https://leetcode.com/problems/subsets/
class Solution:
    def __init__(self):
        self.answer = []
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(cur, visited = []):
            self.answer.append(visited)
            
            for idx in range(cur, len(nums)):
                if nums[idx] not in visited:
                    dfs(idx, visited + [nums[idx]])
            
        dfs(0, [])
        return self.answer
