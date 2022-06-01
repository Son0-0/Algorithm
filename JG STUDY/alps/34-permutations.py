# https://leetcode.com/problems/permutations
class Solution:
    def __init__(self):
        self.answer=[]
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        
        def dfs(length, visited=[]):
            
            if length == size and visited not in self.answer:
                self.answer.append(visited)
            
            for num in nums:
                if num not in visited:
                    dfs(length + 1, visited + [num])
        
        dfs(0, [])
            
        return self.answer
