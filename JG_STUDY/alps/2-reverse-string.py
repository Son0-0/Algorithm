# 213 ms 18.4 MB
# https://leetcode.com/problems/reverse-string/

class Solution:
    def reverseString(self, s: List[str]) -> None:
        size = len(s)

        for idx in range(size // 2):
            s[idx], s[size - idx - 1] = s[size - idx - 1], s[idx]