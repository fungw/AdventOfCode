package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

type stack []int

func main() {
	fmt.Println(processData())
}

func (s stack) Push(v int) stack {
	return append(s, v)
}

func (s stack) Pop() (stack, int) {
	l := len(s)
	return s[:l-1], s[l-1]
}

func processData() int {
	file, err := os.Open("../data.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	meterReadingStack := make(stack, 0)
	increaseCount := 0

	for scanner.Scan() {
		meterReadingStr := scanner.Text()
		meterReadingInt, _ := strconv.Atoi(meterReadingStr)

		meterReadingStack = meterReadingStack.Push(meterReadingInt)
		if len(meterReadingStack) >= 2 {
			meterReadingStack, meterA := meterReadingStack.Pop()
			meterReadingStack, meterB := meterReadingStack.Pop()
			if meterA > meterB {
				increaseCount++
			}
		}
	}

	return increaseCount
}
