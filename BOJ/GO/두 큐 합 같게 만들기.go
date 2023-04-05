package main

import "fmt"

type Queue struct {
	list []int
	sum  int
}

func main() {
	answer := solution([]int{3, 2, 7, 2}, []int{4, 6, 5, 1})
	fmt.Println(answer)

	answer = solution([]int{1, 2, 1, 2}, []int{1, 10, 1, 2})
	fmt.Println(answer)

	answer = solution([]int{1, 1}, []int{1, 5})
	fmt.Println(answer)
}

func solution(queue1 []int, queue2 []int) int {
	answer := 0

	size := len(queue1)
	var q1, q2 Queue

	for i := 0; i < size; i++ {
		q1.list = append(q1.list, queue1[i])
		q1.sum += queue1[i]

		q2.list = append(q2.list, queue2[i])
		q2.sum += queue2[i]
	}

	for i := 0; i <= size*2+1; i++ {
		if q1.sum == q2.sum {
			return answer
		} else {
			if q1.sum < q2.sum {
				if len(q2.list) != 0 {
					q1.sum += q2.list[0]
					q2.sum -= q2.list[0]
					q1.append(q2.pop())
				} else {
					break
				}
			} else {
				if len(q1.list) != 0 {
					q2.sum += q1.list[0]
					q1.sum -= q1.list[0]
					q2.append(q1.pop())
				} else {
					break
				}
			}
		}
		answer++
	}

	if q1.sum == q2.sum {
		return answer
	}
	return -1
}

func (q *Queue) pop() int {
	value := q.list[0]
	q.list = q.list[1:]
	return value
}

func (q *Queue) append(num int) {
	q.list = append(q.list, num)
}
