package main

import "fmt"

type SnapshotArray struct {
	arr [][][]int
	id  int
}

func Constructor(length int) SnapshotArray {
	target := make([][][]int, length)

	for i := 0; i < length; i++ {
		target[i] = append(target[i], []int{0, 0})
	}

	return SnapshotArray{
		arr: target,
		id:  0,
	}
}

func (this *SnapshotArray) Set(index int, val int) {
	this.arr[index] = append(this.arr[index], []int{this.id, val})
}

func (this *SnapshotArray) Snap() int {
	this.id++
	return this.id - 1
}

func (this *SnapshotArray) Get(index int, snap_id int) int {
	past := this.arr[index]

	left, right := 0, len(past)-1

	for left <= right {
		mid := (left + right) / 2

		if past[mid][0] <= snap_id {
			left = mid + 1
		} else {
			right = mid - 1
		}
	}

	return past[right][1]
}

func main() {
	obj := Constructor(3)
	obj.Set(0, 5)
	fmt.Println(obj.Snap())
	obj.Set(0, 6)
	fmt.Println(obj.Get(0, 0))
}

/*
 * Your SnapshotArray object will be instantiated and called as such:
 * obj := Constructor(length);
 * obj.Set(index,val);
 * param_2 := obj.Snap();
 * param_3 := obj.Get(index,snap_id);
 */
