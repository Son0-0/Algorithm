# 94 ms 13.9 MB
# https://leetcode.com/problems/add-two-numbers
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = "", ""

        while l1:
            num1 += str(l1.val)
            l1 = l1.next
        num1 = num1[::-1]

        while l2:
            num2 += str(l2.val)
            l2 = l2.next
        num2 = num2[::-1]

        num = str(int(num1) + int(num2))
        num = num[::-1]
        size = len(num)

        answer = ListNode(num[0])
        cur = answer
        for idx in range(1, size):
            temp = ListNode(num[idx])
            cur.next = temp
            cur = cur.next

        return answer