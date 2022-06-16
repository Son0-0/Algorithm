# 쓰레기 코드
# 9552 ms 13.9 MB
# https://leetcode.com/problems/longest-palindromic-substring

class Solution:    
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2 or s == s[::-1]:
            return s

        result = [0, ""]

        for pointA in range(len(s)):
            for pointB in range(len(s), pointA, -1):
                if (pointB - pointA) <= result[0]:
                    continue
                
                target = s[pointA:pointB]
                if target == target[::-1]:
                    result[0], result[1] = pointB - pointA, target

        return result[1]