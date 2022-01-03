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
	fmt.Println(scanner.Scan())

	for scanner.Scan() {
		s := fmt.Sprintf("%b", scanner.Text()[0])
		fmt.Println(s)
	}

	return 0
}
