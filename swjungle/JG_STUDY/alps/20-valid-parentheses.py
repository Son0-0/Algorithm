# 47 ms 13.8 MB
# https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        olist = ['[', '(', '{']
        clist = [']', ')', '}']
        
        for c in s:
            if c in olist:
                stack.append(c)
            elif c in clist:
                if not stack or olist[clist.index(c)] != stack.pop():
                    return False
        
        if len(stack) == 0:
            return True
        else:
            return False