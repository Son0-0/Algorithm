package main

import "fmt"

type ParkingSystem struct {
	Slot map[int]int
}

func Constructor(big int, medium int, small int) ParkingSystem {
	return ParkingSystem{
		Slot: map[int]int{1: big, 2: medium, 3: small},
	}
}

func (this *ParkingSystem) AddCar(carType int) bool {
	if 0 < this.Slot[carType] {
		this.Slot[carType]--
	} else {
		return false
	}

	return true
}

func main() {
	obj := Constructor(1, 1, 0)
	fmt.Println(obj.AddCar(1))
	fmt.Println(obj.AddCar(2))
	fmt.Println(obj.AddCar(3))
	fmt.Println(obj.AddCar(1))
}
