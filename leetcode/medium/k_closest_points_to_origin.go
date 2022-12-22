package main

import (
	"fmt"
	"math"
	"sort"
)

func contains(arr []float64, target float64) bool {
	for _, num := range arr {
		if num == target {
			return true
		}
	}

	return false
}

func kClosest(points [][]int, k int) [][]int {
	temp := []float64{}
	pmap := make(map[float64][][]int)

	for _, point := range points {
		t := math.Pow(float64(point[0]), 2) + math.Pow(float64(point[1]), 2)
		if !contains(temp, t) {
			temp = append(temp, t)
		}
		pmap[t] = append(pmap[t], point)
	}

	sort.Float64s(temp)

	result := [][]int{}

	cur, total := 0, 0
	for total < k {
		for _, element := range pmap[temp[cur]] {
			if total < k {
				result = append(result, element)
				total += 1
			} else {
				return result
			}
		}
		cur += 1
	}

	return result
}

func main() {
	fmt.Println(kClosest([][]int{{1, 3}, {-2, 2}}, 1))
	fmt.Println(kClosest([][]int{{-2, 2}, {2, -2}, {1, 3}}, 2))
	fmt.Println(kClosest([][]int{{0, 1}, {1, 0}}, 2))
	fmt.Println(kClosest([][]int{{3, 3}, {5, -1}, {-2, 4}}, 2))
}
