# https://leetcode.com/problems/valid-perfect-square/submissions/
# 367. Valid Perfect Square
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if int(num ** 0.5) ** 2 == num:
            return True
        return False
