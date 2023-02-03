package main

import (
	"bufio"
	"fmt"
	"os"
	"path"
	"runtime"
	"strconv"
)

func IntToSlice(n int64, sequence []int64) []int64 {
	if n != 0 {
		i := n % 10
		sequence = append([]int64{i}, sequence...)
		return IntToSlice(n/10, sequence)
	}
	return sequence
}

func part1(filepath string) int {
	file, _ := os.Open(filepath)
	scanner := bufio.NewScanner(file)
	var lines []string
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	chars := []rune(lines[0])
	numbers := make([]int, 0)
	for i := 0; i < len(chars); i++ {
		number, _ := strconv.Atoi(string(chars[i]))
		numbers = append(numbers, number)
	}
	length := 150
	res := 0
	zerores := length
	for i := 0; i < len(numbers); i += length {
		slice := numbers[i : i+length]
		zeros, ones, twos := 0, 0, 0
		for _, num := range slice {
			if num == 0 {
				zeros += 1
			}
			if num == 1 {
				ones += 1
			}
			if num == 2 {
				twos += 1
			}
		}
		if zeros < zerores {
			zerores = zeros
			res = ones * twos
		}
	}
	return res
}

func part2(filepath string) {
	file, _ := os.Open(filepath)
	scanner := bufio.NewScanner(file)
	var lines []string
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	chars := []rune(lines[0])
	numbers := make([]int, 0)
	for i := 0; i < len(chars); i++ {
		number, _ := strconv.Atoi(string(chars[i]))
		numbers = append(numbers, number)
	}
	screen := make([][]int, 0)
	length := 150
	for i := 0; i < len(numbers); i += length {
		screen = append(screen, numbers[i:i+length])
	}
	final := make([]rune, 0)
	for i := 0; i < 150; i++ {
		for j := 0; j < 150; j++ {
			if screen[j][i] == 0 {
				final = append(final, ' ')
				break
			}
			if screen[j][i] == 1 {
				final = append(final, '#')
				break
			}
		}
	}
	for i := 0; i < len(final); i += 25 {
		fmt.Println(string(final[i : i+25]))
	}
}

func main() {
	_, filename, _, _ := runtime.Caller(0)
	filepath := path.Join(path.Dir(filename), "day8.txt")
	fmt.Println(part1(filepath))
	part2(filepath)
}
