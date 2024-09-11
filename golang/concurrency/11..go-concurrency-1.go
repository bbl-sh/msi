// Time out execution
package main

import (
	"fmt"
	"time"
)

func main() {
	ch1 := make(chan int, 3)

	go AssignVal(ch1)
	select {
	case val1 := <-ch1:
		fmt.Println(val1)
	// This line is to be executed after the timeout happens
	case <-time.After(1 * time.Second):
		fmt.Println("Executed after timeout")
	}
	time.Sleep(time.Second)
}

func AssignVal(ch chan int) {
	time.Sleep(3 * time.Second)
	ch <- 1
}
