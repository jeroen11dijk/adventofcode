package main

import (
	"bufio"
	"fmt"
	"os"
	"path"
	"regexp"
	"runtime"
	"strconv"
)

type Chemical struct {
	resource string
	number   int
}

func Max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func readFile(filepath string) []string {
	file, _ := os.Open(filepath)
	scanner := bufio.NewScanner(file)
	var lines []string
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	return lines
}

func createReactions(lines []string) map[string][]Chemical {
	reactions := make(map[string][]Chemical)
	for _, line := range lines {
		re := regexp.MustCompile("[0-9]+")
		numbers := make([]int, 0)
		for _, val := range re.FindAllString(line, -1) {
			number, _ := strconv.Atoi(val)
			numbers = append(numbers, number)
		}
		re = regexp.MustCompile("[A-Za-z]+")
		resources := make([]string, 0)
		resources = append(resources, re.FindAllString(line, -1)...)
		made := resources[len(resources)-1]
		requirements := make([]Chemical, 0)
		requirements = append(requirements, Chemical{made, numbers[len(numbers)-1]})
		resources = resources[0 : len(resources)-1]
		for i, resource := range resources {
			requirements = append(requirements, Chemical{resource, numbers[i]})
		}
		reactions[made] = requirements
	}
	return reactions
}

func cost(name string, quantity int, reactions map[string][]Chemical, refuse map[string]int) int {
	if name == "ORE" {
		return quantity
	}
	list, quantityProducted := reactions[name][1:], reactions[name][0].number
	if refuse[name] > 0 {
		if refuse[name] >= quantity {
			refuse[name] -= quantity
			return 0
		}
		quantity -= refuse[name]
		refuse[name] = 0
		return cost(name, quantity, reactions, refuse)
	}
	reactionsNeeded := (quantity-1)/quantityProducted + 1
	var oreNeeded int
	for _, r := range list {
		oreNeeded += cost(r.resource, r.number*reactionsNeeded, reactions, refuse)
	}
	if reactionsNeeded*quantityProducted-quantity > 0 {
		refuse[name] += reactionsNeeded*quantityProducted - quantity
	}
	return oreNeeded
}

func part1(reactions map[string][]Chemical) int {
	storage := make(map[string]int)
	return cost("FUEL", 1, reactions, storage)
}

func part2(reactions map[string][]Chemical) int {
	storage := make(map[string]int)
	target := 1000000000000
	lowerbound := target / cost("FUEL", 1, reactions, storage)
	upperbound := 1
	for cost("FUEL", upperbound, reactions, storage) < target {
		upperbound *= 10
	}
	for {
		mid := lowerbound + (upperbound-lowerbound)/2
		if mid == lowerbound {
			break
		}
		guess := cost("FUEL", mid, reactions, storage)
		if guess <= target {
			lowerbound = mid
		} else {
			upperbound = mid - 1
		}
	}
	return lowerbound
}

func main() {
	_, filename, _, _ := runtime.Caller(0)
	filepath := path.Join(path.Dir(filename), "day14.txt")
	lines := readFile(filepath)
	reactions := createReactions(lines)
	fmt.Println(part1(reactions))
	fmt.Println(part2(reactions))
}
