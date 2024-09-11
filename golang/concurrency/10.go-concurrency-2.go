// Concurrency practices: Spawning Go-routine closures in a loop
package main

import (
	"fmt"
	"sync"
)

func main() {
	var wg sync.WaitGroup
	wg.Add(10)
	for i := 0; i < 10; i++ {
		// Passing the i value as parameter in go anonymous function
		go func(i int) {
			fmt.Println(i)
			wg.Done()
		}(i)

	}
	wg.Wait()
	fmt.Println("Done ")
}
