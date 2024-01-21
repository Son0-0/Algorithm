package main

import (
	"container/heap"
	"fmt"
)

type Item struct {
	priority int
	index    int
}

type PriorityQueue []*Item

type KthLargest struct {
	nums PriorityQueue
	k    int
}

func (pq PriorityQueue) Len() int { return len(pq) }

func (pq PriorityQueue) Less(i, j int) bool {
	return pq[i].priority < pq[j].priority
}

func (pq PriorityQueue) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
	pq[i].index = i
	pq[j].index = j
}

func (pq *PriorityQueue) Push(x interface{}) {
	n := len(*pq)
	item := x.(*Item)
	item.index = n
	*pq = append(*pq, item)
}

func (pq *PriorityQueue) Pop() interface{} {
	old := *pq
	n := len(old)
	item := old[n-1]
	old[n-1] = nil  // avoid memory leak
	item.index = -1 // for safety
	*pq = old[0 : n-1]
	return item
}

func Constructor(k int, nums []int) KthLargest {
	pq := make(PriorityQueue, len(nums))

	for i, num := range nums {
		pq[i] = &Item{
			priority: num,
			index:    i,
		}
	}

	heap.Init(&pq)

	for k < len(pq) {
		heap.Pop(&pq)
	}

	return KthLargest{
		nums: pq,
		k:    k,
	}
}

func (this *KthLargest) Add(val int) int {
	heap.Push(&this.nums, &Item{
		priority: val,
	})

	for this.k < len(this.nums) {
		heap.Pop(&this.nums)
	}

	return (this.nums)[0].priority
}

func main() {
	obj := Constructor(1, []int{})
	fmt.Println(obj.Add(-3))
	fmt.Println(obj.Add(-2))
	fmt.Println(obj.Add(-4))
	fmt.Println(obj.Add(0))
	fmt.Println(obj.Add(4))

	// obj := Constructor(3, []int{4, 5, 8, 2})
	// fmt.Println(obj.Add(3))
	// fmt.Println(obj.Add(5))
	// fmt.Println(obj.Add(10))
	// fmt.Println(obj.Add(9))
	// fmt.Println(obj.Add(4))
}
