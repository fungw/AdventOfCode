package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

const REPORT_LENGTH = 12

var REPORT_TRACKER = [REPORT_LENGTH]binary{
	{
		zeroes: 0,
		ones:   0,
	},
}

type binary struct {
	zeroes int
	ones   int
}

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

	for scanner.Scan() {
		var inputLine = scanner.Text()
		for i := 0; i < len(inputLine); i++ {
			var inputValue = inputLine[i]
			if inputValue == 49 {
				fmt.Print(1)
			} else if inputValue == 48 {
				fmt.Print(0)
			}
		}
		fmt.Println()
	}

	return 0
}
