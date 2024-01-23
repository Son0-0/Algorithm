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

func topKFrequent(nums []int, k int) []int {
	result := make([]int, 0)
	freq := make(map[int]int)

	for _, num := range nums {
		freq[num]++
	}

	fmt.Println(freq)

	// init priority queue
	pq := make(PriorityQueue, len(freq))
	i := 0

	for key := range freq {
		pq[i] = &Item{
			value:    key,
			priority: freq[key],
			index:    i,
		}
		i++
	}

	heap.Init(&pq)

	for k != 0 {
		cur := heap.Pop(&pq).(*Item)
		result = append(result, cur.value)
		k--
	}

	return result
}

func main() {
	fmt.Println(topKFrequent([]int{1, 1, 1, 2, 2, 3}, 2))
}
