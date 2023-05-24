package main

import (
	"container/heap"
	"fmt"
	"sort"
)

type Item struct {
	priority int64
}

type PriorityQueue []*Item

func (pq PriorityQueue) Len() int { return len(pq) }

func (pq PriorityQueue) Less(i, j int) bool {
	return pq[i].priority < pq[j].priority
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

func max(a, b int64) int64 {
	if a < b {
		return b
	}
	return a
}

func maxScore(nums1 []int, nums2 []int, k int) int64 {
	var result int64

	// merge two num slice
	mergedNums := make([][]int, len(nums1))

	for i := 0; i < len(nums1); i++ {
		mergedNums[i] = []int{nums2[i], nums1[i]}
	}

	sort.Slice(mergedNums, func(i, j int) bool {
		return mergedNums[i][0] > mergedNums[j][0]
	})

	pq := make(PriorityQueue, 0)

	heap.Init(&pq)

	var sum int64

	for _, num := range mergedNums {
		if len(pq) == k {
			sum -= heap.Pop(&pq).(*Item).priority
		}

		sum += int64(num[1])
		heap.Push(&pq, &Item{
			priority: int64(num[1]),
		})

		if len(pq) == k {
			result = max(result, sum*int64(num[0]))
		}
	}

	return int64(result)
}

func main() {
	fmt.Println(maxScore([]int{1, 3, 3, 2}, []int{2, 1, 3, 4}, 3))
	fmt.Println(maxScore([]int{2, 1, 14, 12}, []int{11, 7, 13, 6}, 3))
}
