package main

import (
	"fmt"
)

func main() {
	ch := make(chan int, 3)
	ch <- 1
	ch <- 2
	val, ok := <-ch
	fmt.Println(val, ok)
	close(ch)
	// This will throw error since we are trying to write to channel after closing
	ch <- 3
	// This will also throw error since we are closing the channel again
	close(ch)
}
