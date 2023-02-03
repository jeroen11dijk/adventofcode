package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"path"
	"runtime"
	"strconv"
	"strings"
)

type Pair struct {
	a, b int
}

func Abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func part(filepath string) []int {
	distance := math.MaxInt64
	stepsRequired := math.MaxInt64
	file, _ := os.Open(filepath)
	scanner := bufio.NewScanner(file)
	seen := map[Pair][]int{}
	line := 0
	for scanner.Scan() {
		moves := strings.Split(scanner.Text(), ",")
		current := Pair{0, 0}
		step := 1
		for _, move := range moves {
			side := move[0:1]
			steps, _ := strconv.Atoi(move[1:])
			for i := 0; i < steps; i++ {
				if side == "R" {
					current = Pair{current.a + 1, current.b}
				} else if side == "L" {
					current = Pair{current.a - 1, current.b}
				} else if side == "U" {
					current = Pair{current.a, current.b + 1}
				} else if side == "D" {
					current = Pair{current.a, current.b - 1}
				}
				value, ok := seen[current]
				if !ok {
					value = []int{0, 0}
					seen[current] = value
				}
				if value[line] == 0 {
					value[line] = step
					if value[0] > 0 && value[1] > 0 {
						distance = min(distance, Abs(current.a)+Abs(current.b))
						stepsRequired = min(stepsRequired, value[0]+value[1])
					}
				}
				step += 1
			}
		}
		line += 1
	}
	return []int{distance, stepsRequired}
}

func main() {
	_, filename, _, _ := runtime.Caller(0)
	filepath := path.Join(path.Dir(filename), "day3.txt")
	fmt.Println(part(filepath))
}
