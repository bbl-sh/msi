package main

import (
	"fmt"
	"time"
)

func main() {
	ch1 := make(chan int, 2)
	ch2 := make(chan int, 2)

	go goOne(ch1)
	go goTwo(ch2)
	// Using select statement
	select {
	case val1 := <-ch1:
		fmt.Println(val1)
	case val2 := <-ch2:
		fmt.Println(val2)
		// default:
		// 	fmt.Println("default case run")
	}
	time.Sleep(2 * time.Second)
}

func goOne(ch chan int) {
	ch <- 1
}

func goTwo(ch chan int) {
	ch <- 2
}
