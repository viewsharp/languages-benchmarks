package main

import (
	"fmt"
	"time"
)

func sumEvenNumbers(bottom int64, top int64) int64 {
	var result int64 = 0
	for x := bottom; x < top+1; x++ {
		if x%2 == 0 {
			result += x
		}
	}
	return result
}

func main() {
	startAt := time.Now()
	res := sumEvenNumbers(2, 20_000_000)
	fmt.Println(time.Now().Sub(startAt))
	fmt.Println(res)
}
