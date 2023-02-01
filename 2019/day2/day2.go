package main

import (
	"bufio"
	"fmt"
	"os"
	"path"
	"runtime"
	"strconv"
	"strings"
)

func runIntcode(intCode []int, noun int, verb int) int {
	intCode[1] = noun
	intCode[2] = verb
	index := 0
	for true {
		if intCode[index] == 99 {
			return intCode[0]
		} else if intCode[index] == 1 {
			intCode[intCode[index+3]] = intCode[intCode[index+1]] + intCode[intCode[index+2]]
		} else if intCode[index] == 2 {
			intCode[intCode[index+3]] = intCode[intCode[index+1]] * intCode[intCode[index+2]]
		}
		index += 4
	}
	return 0
}

func part1(filepath string) int {
	file, _ := os.Open(filepath)
	scanner := bufio.NewScanner(file)
	var lines []string
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	strs := strings.Split(lines[0], ",")
	intCode := make([]int, len(strs))
	for i := range intCode {
		intCode[i], _ = strconv.Atoi(strs[i])
	}
	return runIntcode(intCode, 12, 2)
}

func part2(filepath string) int {
	file, _ := os.Open(filepath)
	scanner := bufio.NewScanner(file)
	var lines []string
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	strs := strings.Split(lines[0], ",")
	intCode := make([]int, len(strs))
	for i := range intCode {
		intCode[i], _ = strconv.Atoi(strs[i])
	}
	tmp := make([]int, len(intCode))
	for noun := 0; noun < 100; noun++ {
		for verb := 0; verb < 100; verb++ {
			copy(tmp, intCode)
			res := runIntcode(tmp, noun, verb)
			if res == 19690720 {
				return 100*noun + verb
			}
		}
	}
	return 0
}

func main() {
	_, filename, _, _ := runtime.Caller(0)
	filepath := path.Join(path.Dir(filename), "day6.txt")
	fmt.Println(part1(filepath))
	fmt.Println(part2(filepath))
}
