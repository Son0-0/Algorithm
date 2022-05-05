# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:

        llist = []

        for i in s.lower():
            if 97 <= ord(i) <= 122 or 48 <= ord(i) <= 57:
                llist.append(i)

        size = len(llist)
        half = size // 2

        if size == 1:
            return True

        if size % 2 == 0:
            if llist[:half] == list(reversed(llist[half:])):
                return True
        else:
            if llist[:half] == list(reversed(llist[half + 1:])):
                return True

        return False