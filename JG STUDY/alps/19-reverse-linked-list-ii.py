# 55 ms 14.1 MB
# https://leetcode.com/problems/reverse-linked-list-ii
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        llist = []
        while head:
            llist.append(head.val)
            head = head.next

        answer = ListNode()
        cur = answer
        
        for num in (llist[:left - 1] + llist[left - 1:right][::-1] + llist[right:]):
            cur.next = ListNode(num)
            cur = cur.next
        
        answer = answer.next
        
        return answer