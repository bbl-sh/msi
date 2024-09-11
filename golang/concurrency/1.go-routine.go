package main

import (
	"fmt"
	"time"
)

func f(i int) {
	fmt.Println(i)
}

func main() {
	start := time.Now()

	for i := 0; i < 5; i++ {
		go f(i)
	}

	end := time.Since(start)

	fmt.Println("It took : ", end)

	go func() {
		fmt.Println("anonymous go routines")
	}()

	// For executing go routines
	time.Sleep(2 * time.Second)
}
