package main

import "fmt"

type SmallestInfiniteSet struct {
	begin  int
	cur    int
	exists map[int]bool
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}

func Constructor() SmallestInfiniteSet {
	exists := make(map[int]bool)

	for i := 0; i <= 1000; i++ {
		exists[i] = true
	}

	return SmallestInfiniteSet{
		begin:  1,
		cur:    1,
		exists: exists,
	}
}

func (this *SmallestInfiniteSet) PopSmallest() int {
	for i := this.begin; i <= this.cur; i++ {
		if v, e := this.exists[i]; e {
			if v == true {
				this.exists[i] = false
				this.begin = i + 1
				this.cur = max(this.cur, i+1)
				return i
			}
		}
	}

	return 0
}

func (this *SmallestInfiniteSet) AddBack(num int) {
	if v, e := this.exists[num]; e {
		if v == false {
			this.exists[num] = true
			this.begin = min(this.begin, num)
		}
	}
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
