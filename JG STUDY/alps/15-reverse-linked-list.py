# 43 ms 16.3 MB
# https://leetcode.com/problems/reverse-linked-list
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        root = ListNode()
        llist = []

        while head:
            llist.append(ListNode(head.val))
            head = head.next

        size = len(llist) - 1
        root = llist[size]
        for idx in range(size, 0, -1):
            llist[idx].next = llist[idx - 1]

        return root