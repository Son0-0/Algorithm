package main

import (
	"container/heap"
	"fmt"
)

// num range (1, 1000)
// implement minheap

type MinHeap []int

func (mh MinHeap) Len() int { return len(mh) }

func (mh MinHeap) Less(i, j int) bool {
	return mh[i] < mh[j]
}

func (mh MinHeap) Swap(i, j int) {
	mh[i], mh[j] = mh[j], mh[i]
}

func (mh *MinHeap) Push(x interface{}) {
	*mh = append(*mh, x.(int))
}

func (mh *MinHeap) Pop() interface{} {
	old := *mh
	n := len(old)
	item := old[n-1]
	*mh = old[0 : n-1]
	return item
}

type SmallestInfiniteSet struct {
	set    *MinHeap
	exists map[int]bool
}

func Constructor() SmallestInfiniteSet {
	mh := make(MinHeap, 0)
	heap.Init(&mh)

	exists := make(map[int]bool)

	for i := 1; i <= 1000; i++ {
		exists[i] = true
		heap.Push(&mh, i)
	}

	set := SmallestInfiniteSet{
		set:    &mh,
		exists: exists,
	}

	return set
}

func (this *SmallestInfiniteSet) PopSmallest() int {
	retVal := heap.Pop(this.set).(int)

	delete(this.exists, retVal)

	return retVal
}

func (this *SmallestInfiniteSet) AddBack(num int) {
	if _, e := this.exists[num]; e {
		return
	}

	this.exists[num] = true
	heap.Push(this.set, num)
}

func main() {
	set := Constructor()

	set.AddBack(2)
	fmt.Println(set.PopSmallest()) // 1
	fmt.Println(set.PopSmallest()) // 2
	fmt.Println(set.PopSmallest()) // 3
	set.AddBack(1)
	fmt.Println(set.PopSmallest()) // 1
	fmt.Println(set.PopSmallest()) // 4
	fmt.Println(set.PopSmallest()) // 5
}
