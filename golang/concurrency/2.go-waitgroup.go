package main

import (
	"fmt"
	"sync"
	"time"
)

func f(i int, wg *sync.WaitGroup) {
	fmt.Println(i)
	wg.Done()
}

func main() {
	start := time.Now()
	var wg sync.WaitGroup
	// Waitgroup Add function
	wg.Add(5)

	for i := 0; i < 5; i++ {
		// Passing the wg parameter
		go f(i, &wg)
	}

	end := time.Since(start)
	// Waitgroup wait function
	wg.Wait()
	fmt.Println("It took : ", end)
}
