package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func mergeNodes(head *ListNode) *ListNode {
	cur := head.Next

	for cur != nil {
		for cur.Next.Val != 0 {
			cur.Val += cur.Next.Val
			cur.Next = cur.Next.Next
		}

		cur.Next = cur.Next.Next
		cur = cur.Next
	}

	return head.Next
}

func main() {

	zero := ListNode{
		Val:  0,
		Next: nil,
	}

	one := ListNode{
		Val:  1,
		Next: &zero,
	}

	three := ListNode{
		Val:  3,
		Next: &one,
	}

	root := ListNode{
		Val:  0,
		Next: &three,
	}

	target := mergeNodes(&root)

	for target != nil {
		fmt.Println(target.Val)
		target = target.Next
	}
}
