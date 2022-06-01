# https://leetcode.com/problems/letter-combinations-of-a-phone-number
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        digits_to_str = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']
        }
        
        answer = []
        def dfs(cur, string, length):
            if length == len(digits):
                answer.append(string)
                return
            
            for dtos in digits_to_str[int(digits[cur])]:
                dfs(cur + 1, string + dtos, length + 1)
                
        if len(digits) != 0:
            dfs(0, '', 0)
        return answer
            
        