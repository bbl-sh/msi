package main

import (
	"fmt"
	"time"
)

func send(ch chan string) {
	ch <- "channel value"
}

func receive(ch chan string) {
	fmt.Println("reveiving the values ")
	val := <-ch
	fmt.Println("received value is : ", val)
}

func main() {
	ch := make(chan string)
	go send(ch)
	go receive(ch)
	time.Sleep(2 * time.Second)
}
