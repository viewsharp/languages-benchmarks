package main

import (
	"fmt"
	"runtime"
	"strings"
	"time"
)

const sumEvenNumbersCode = `
func sumEvenNumbers(bottom int64, top int64) int64 {
    var result int64 = 0
    for x := bottom; x < top+1; x++ {
        if x%2 == 0 {
            result += x
        }
    }
    return result
}
`

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
	repeats := 100

	minExecutionTime := time.Duration(1<<63 - 1)
	for i := 0; i < repeats; i++ {
		startAt := time.Now()
		result := sumEvenNumbers(2, 20_000_000)

		executionTime := time.Now().Sub(startAt)
		if executionTime < minExecutionTime {
			minExecutionTime = executionTime
		}

		_ = result
	}

	fmt.Printf("Go: %s  \n", runtime.Version())
	fmt.Println("Test case: sumEvenNumbers(2, 20_000_000)  ")
	fmt.Println()
	fmt.Println("```go")
	fmt.Println(strings.Trim(sumEvenNumbersCode, "\n"))
	fmt.Println("```")
	fmt.Printf("Repeats: %d  \n", repeats)
	fmt.Printf("Best execution time: %s  \n", minExecutionTime)
}
