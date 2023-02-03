package main

import (
	"fmt"
	"strconv"
)

func part() (int, int) {
	start := 356261
	end := 846303
	res1 := 0
	res2 := 0
	for i := start; i <= end; i++ {
		res1 += part1(i)
		res2 += part2(i)
	}
	return res1, res2
}

func part1(i int) int {
	var last int32
	last = 0
	repeat := false
	for _, c := range strconv.Itoa(i) {
		if c < last {
			return 0
		}
		if c == last {
			repeat = true
		}
		last = c
	}
	if repeat {
		return 1
	}
	return 0
}

func part2(i int) int {
	var last int32
	last = 0
	repeat := false
	repeatN := 0
	for _, c := range strconv.Itoa(i) {
		if c < last {
			return 0
		}
		if c == last {
			repeatN += 1
		} else {
			if repeatN == 1 {
				repeat = true
			}
			repeatN = 0
		}
		last = c
	}
	if repeat || repeatN == 1 {
		return 1
	}
	return 0
}

func main() {
	fmt.Println(part())
}
