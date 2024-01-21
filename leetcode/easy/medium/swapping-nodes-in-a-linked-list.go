package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func swapNodes(head *ListNode, k int) *ListNode {
	i := 0
	first, second := head, head

	for i < k-1 {
		first = first.Next
		i++
	}

	for i := first.Next; i != nil; i = i.Next {
		second = second.Next
	}

	first.Val, second.Val = second.Val, first.Val

	return head
}

func main() {
	five := ListNode{
		Val:  5,
		Next: nil,
	}

	four := ListNode{
		Val:  4,
		Next: &five,
	}

	three := ListNode{
		Val:  3,
		Next: &four,
	}

	two := ListNode{
		Val:  2,
		Next: &three,
	}

	one := ListNode{
		Val:  1,
		Next: &two,
	}

	swapNodes(&one, 2)

	cur := &one
	for cur != nil {
		fmt.Println(cur.Val)
		cur = cur.Next
	}
}
