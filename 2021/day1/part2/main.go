package main

import (
	"bufio"
	"container/list"
	"fmt"
	"log"
	"os"
	"strconv"
)

func main() {
	fmt.Println(processData())
}

func processData() int {
	file, err := os.Open("../data.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	queue := list.New()
	increaseCount := 0

	for scanner.Scan() {
		meterReadingStr := scanner.Text()
		meterReadingInt, _ := strconv.Atoi(meterReadingStr)

		queue.PushBack(meterReadingInt)
		if queue.Len() >= 4 {
			meterA := queue.Front()
			queue.Remove(meterA)
			meterB := queue.Front()
			queue.Remove(meterB)
			meterC := queue.Front()
			queue.Remove(meterC)
			meterD := queue.Front()
			queue.Remove(meterD)

			meterAInt := meterA.Value.(int)
			meterBInt := meterB.Value.(int)
			meterCInt := meterC.Value.(int)
			meterDInt := meterD.Value.(int)

			slidingWindowSumA := meterAInt + meterBInt + meterCInt
			slidingWindowSumB := meterBInt + meterCInt + meterDInt

			if slidingWindowSumA < slidingWindowSumB {
				increaseCount++
			}

			queue.PushBack(meterBInt)
			queue.PushBack(meterCInt)
			queue.PushBack(meterDInt)
		}
	}

	return increaseCount
}
