# 871 ms 46.6 MB
# https://leetcode.com/problems/palindrome-linked-list
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        cur = head
        llist = []
        size = 0
        while cur:
            llist.append(cur.val)
            size += 1
            cur = cur.next
        
        half = size // 2
        
        if (size % 2) == 0:
            if llist[:half] == list(reversed(llist[half:])):
                return True
        else:
            if llist[:half] == list(reversed(llist[half + 1:])):
                return True
        return False