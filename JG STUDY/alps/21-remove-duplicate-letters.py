# 48 ms 13.8 MB
# https://leetcode.com/problems/remove-duplicate-letters/
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        count = Counter(s)
        stack = []
        
        for char in s:
            if char in stack:
                count[char] -= 1
                continue
            while len(stack) > 0 and stack[-1] > char and count[stack[-1]] > 0:
                stack.pop()
            count[char] -= 1
            stack.append(char) 
            
        return "".join(stack)
        
#         stack = ''
        
#         length = 0
        
#         result = dict()
#         for idx in range(1, len(s) + 1):
#             result[idx] = []
            
#         for c in s:
#             if c not in stack:
#                 stack += c
#                 length += 1
#             else:
#                 if c < stack[-1]:
#                     stack = stack.replace(c, '')
#                     stack += c
#             print(stack)
#             result[length].append(stack)
#             # result.append([length, stack])    
            
#         print(length, result)
#         print(sorted(result[length])[0])
        
#         return stack[::-1]