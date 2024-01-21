package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func swapPairs(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}

	result := &ListNode{
		Val:  0,
		Next: head,
	}

	cur := result

	for cur.Next != nil && cur.Next.Next != nil {
		first, second := cur.Next, cur.Next.Next

		cur.Next = second
		first.Next = second.Next
		second.Next = first
		cur = cur.Next.Next
	}

	return result.Next
}

func main() {
	four := ListNode{
		Val:  4,
		Next: nil,
	}

	three := ListNode{
		Val:  3,
		Next: &four,
	}

	two := ListNode{
		Val:  2,
		Next: &three,
	}

	result := swapPairs(&ListNode{
		Val:  1,
		Next: &two,
	})

	for cur := result; cur != nil; cur = cur.Next {
		fmt.Println(cur.Val)
	}
}
