package main

import (
	"bufio"
	"fmt"
	"os"
	"path"
	"runtime"
	"strconv"
)

func part1(filepath string) int {
	res := 0
	file, _ := os.Open(filepath)
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lineStr := scanner.Text()
		num, _ := strconv.Atoi(lineStr)
		res += (num / 3) - 2
	}
	return res
}

func CalculateFuel(remainder int) int {
	ExtraFuel := (remainder / 3) - 2
	if ExtraFuel <= 0 {
		return 0
	} else {
		return ExtraFuel + CalculateFuel(ExtraFuel)
	}
}

func part2(filepath string) int {
	res := 0
	file, _ := os.Open(filepath)
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lineStr := scanner.Text()
		num, _ := strconv.Atoi(lineStr)
		res += CalculateFuel(num)
	}
	return res
}

func main() {
	_, filename, _, _ := runtime.Caller(0)
	filepath := path.Join(path.Dir(filename), "day2.txt")
	fmt.Println(part1(filepath))
	fmt.Println(part2(filepath))
}
