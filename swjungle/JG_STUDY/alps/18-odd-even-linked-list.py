# 51 ms 16.7 MB
# https://leetcode.com/problems/odd-even-linked-list
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        odd, even = head, head.next
        oroot, eroot = odd, even
        cur = head.next.next
        
        while cur:
            odd.next = cur
            even.next = cur.next
                
            odd = odd.next
            even = even.next
            
            if cur.next:
                cur = cur.next.next
            else:
                cur = cur.next
        
        odd.next = eroot
        
        return oroot