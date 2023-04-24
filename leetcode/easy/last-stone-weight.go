package main

import (
	"container/heap"
	"fmt"
)

type Item struct {
	value    int
	priority int
	index    int
}

type PriorityQueue []*Item

func (pq PriorityQueue) Len() int { return len(pq) }

func (pq PriorityQueue) Less(i, j int) bool {
	return pq[i].priority > pq[j].priority
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

func lastStoneWeight(stones []int) int {

	pq := make(PriorityQueue, len(stones))

	for i, stone := range stones {
		pq[i] = &Item{
			value:    stone,
			priority: stone,
			index:    i,
		}
	}

	heap.Init(&pq)

	for {
		if pq.Len() < 2 {
			break
		}

		y := heap.Pop(&pq).(*Item)
		x := heap.Pop(&pq).(*Item)

		if x.value == y.value {
			continue
		} else {
			heap.Push(&pq, &Item{
				value:    y.value - x.value,
				priority: y.value - x.value,
			})
		}
	}

	if pq.Len() == 0 {
		return 0
	}
	return heap.Pop(&pq).(*Item).value
}

func main() {
	fmt.Println(lastStoneWeight([]int{2, 7, 4, 1, 8, 1}))
	fmt.Println(lastStoneWeight([]int{1}))
	fmt.Println(lastStoneWeight([]int{2, 2}))
}
