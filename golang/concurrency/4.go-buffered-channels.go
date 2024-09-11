package main

import (
	"fmt"
	"sync"
)

func main() {
	var wg sync.WaitGroup
	wg.Add(2)
	ch := make(chan int, 3)
	send(ch, &wg)
	wg.Wait()
}

func send(ch chan int, wg *sync.WaitGroup) {
	ch <- 1
	ch <- 2
	ch <- 3
	// Function has to a go routine
	go receive(ch, wg)
	// Adding more data to the buffer if required
	ch <- 4
	wg.Done()
	fmt.Println("sent data to the channel ")
}

func receive(ch chan int, wg *sync.WaitGroup) {
	// Acessing the first value of the buffered channel using <-
	fmt.Println("received values are ", <-ch)
	fmt.Println("received values are ", <-ch)
	wg.Done()
}
