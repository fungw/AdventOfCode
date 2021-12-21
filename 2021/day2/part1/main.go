package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
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

	verticalDepth := 0
	horizontalDistance := 0
	const (
		down    = "down"
		forward = "forward"
		up      = "up"
	)
	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		status := strings.Split(scanner.Text(), " ")
		movement, err := strconv.Atoi(status[1])

		if err != nil {
			log.Fatal(err)
		}

		if strings.Contains(status[0], down) {
			verticalDepth += movement
		} else if strings.Contains(status[0], forward) {
			horizontalDistance += movement
		} else if strings.Contains(status[0], up) {
			verticalDepth -= movement
		}
	}

	return horizontalDistance * verticalDepth
}
