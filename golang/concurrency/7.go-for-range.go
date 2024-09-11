package main

import (
	"fmt"
)

func main() {
	ch := make(chan int, 3)
	ch <- 1
	ch <- 2
	// Close the channel before executing the for loop
	close(ch)
	// Using the for range loop for channels
	for val := range ch {
		fmt.Println(val)
	}
}
