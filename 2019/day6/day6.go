package main

import (
	"bufio"
	"fmt"
	"os"
	"path"
	"runtime"
	"strings"

	mapset "github.com/deckarep/golang-set/v2"
)

func part1(filepath string) int {
	file, _ := os.Open(filepath)
	scanner := bufio.NewScanner(file)
	parents := make(map[string]string)
	for scanner.Scan() {
		line := strings.Split(scanner.Text(), ")")
		parent, child := line[0], line[1]
		parents[child] = parent
	}
	res := 0
	for k := range parents {
		current := k
		for true {
			val, ok := parents[current]
			if !ok {
				break
			}
			res += 1
			current = val
		}
	}
	return res
}

func part2(filepath string) int {
	file, _ := os.Open(filepath)
	scanner := bufio.NewScanner(file)
	parents := make(map[string]string)
	children := make(map[string][]string)
	for scanner.Scan() {
		line := strings.Split(scanner.Text(), ")")
		parent, child := line[0], line[1]
		parents[child] = parent
		children[parent] = append(children[parent], child)
	}
	res := 0
	start := parents["YOU"]
	goal := parents["SAN"]
	queue := make([]string, 0)
	queue = append(queue, start)
	seen := mapset.NewSet[string]()
	seen.Add(start)
	for {
		queue2 := make([]string, 0)
		for _, current := range queue {
			seen.Add(current)
			if current == goal {
				return res
			}
			if val, ok := parents[current]; ok {
				if !seen.Contains(val) {
					queue2 = append(queue2, val)
				}
			}
			if _, ok := children[current]; ok {
				for _, child := range children[current] {
					if !seen.Contains(child) {
						queue2 = append(queue2, child)
					}
				}
			}
		}
		res += 1
		queue = queue2
	}
}

func main() {
	_, filename, _, _ := runtime.Caller(0)
	filepath := path.Join(path.Dir(filename), "day6.txt")
	fmt.Println(part1(filepath))
	fmt.Println(part2(filepath))
}
