/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func deleteDuplicates(head *ListNode) *ListNode {
	if head == nil {
		return head
	}

	prev := head

	for cur := head.Next; cur != nil; cur = cur.Next {
		if prev.Val == cur.Val {
			prev.Next = cur.Next
		} else {
			prev = cur
		}
	}

	return head
}