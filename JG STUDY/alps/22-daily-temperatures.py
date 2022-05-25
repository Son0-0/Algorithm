# 1250 ms 25.3 MB
# https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 1:
            return [0]
        
        size = len(temperatures)
        answer = [0 for _ in range(size)]
        stack = []
        for idx, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                i = stack.pop()
                answer[i] = idx - i
            stack.append(idx)
            
        return answer
    
