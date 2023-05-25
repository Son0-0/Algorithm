package main

import (
	"container/heap"
	"fmt"
	"math"
)

type Item struct {
	priority int64
}

type PriorityQueue []*Item

func (pq PriorityQueue) Len() int { return len(pq) }

func (pq PriorityQueue) Less(i, j int) bool {
	return pq[i].priority > pq[j].priority
}

func (pq PriorityQueue) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
}

func (pq *PriorityQueue) Push(x interface{}) {
	item := x.(*Item)
	*pq = append(*pq, item)
}

func (pq *PriorityQueue) Pop() interface{} {
	old := *pq
	n := len(old)
	item := old[n-1]
	old[n-1] = nil // avoid memory leak
	*pq = old[0 : n-1]
	return item
}

func pickGifts(gifts []int, k int) int64 {
	var result int64

	pq := make(PriorityQueue, 0)

	for _, gift := range gifts {
		heap.Push(&pq, &Item{
			priority: int64(gift),
		})
		result += int64(gift)
	}

	heap.Init(&pq)

	for k != 0 {
		cur := heap.Pop(&pq).(*Item).priority

		if 1 < cur {
			target := int64(math.Sqrt(float64(cur)))
			result -= cur - target
			heap.Push(&pq, &Item{
				priority: target,
			})
		} else {
			heap.Push(&pq, &Item{
				priority: cur,
			})
		}

		k--
	}

	return result
}

func main() {
	fmt.Println(pickGifts([]int{25, 64, 9, 4, 100}, 4))
	fmt.Println(pickGifts([]int{1, 1, 1, 1}, 4))
	fmt.Println(pickGifts([]int{71, 43, 70, 27, 71, 37, 57, 12}, 39))
}
