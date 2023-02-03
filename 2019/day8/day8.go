package main

import (
	"bufio"
	"fmt"
	"os"
	"path"
	"runtime"
	"strconv"

	"github.com/reactivex/rxgo/v2"
)

func readFile(filepath string) []string {
	file, _ := os.Open(filepath)
	scanner := bufio.NewScanner(file)
	var lines []string
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	return lines
}

func convertStringSliceToIntSlice(lines []string) []int {
	chars := []rune(lines[0])
	numbers := make([]int, 0)
	for _, c := range chars {
		number, _ := strconv.Atoi(string(c))
		numbers = append(numbers, number)
	}
	return numbers
}

func part1(numbers []int, length int) int {
	res := 0
	zeroRes := length
	for i := 0; i < len(numbers); i += length {
		slice := numbers[i : i+length]
		zeros, ones, twos := 0, 0, 0
		for _, num := range slice {
			switch num {
			case 0:
				zeros += 1
			case 1:
				ones += 1
			case 2:
				twos += 1
			}
		}
		if zeros < zeroRes {
			zeroRes = zeros
			res = ones * twos
		}
	}
	return res
}

func part2(numbers []int, length int) {
	screen := make([][]int, 0)
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

func processSlice(slice []int, res int, zerores int) (int, int) {
	zeros, ones, twos := 0, 0, 0
	for _, num := range slice {
		switch num {
		case 0:
			zeros += 1
		case 1:
			ones += 1
		case 2:
			twos += 1
		}
	}
	if zeros < zerores {
		zerores = zeros
		res = ones * twos
	}
	return res, zerores
}

func part1RX(numbers []int, length int) int {
	res := 0
	zerores := length
	<-rxgo.Just(numbers)().BufferWithCount(150).DoOnNext(func(i interface{}) {
		bufferedNumbers := i.([]interface{})
		wtf := make([]int, len(bufferedNumbers))
		for i, n := range bufferedNumbers {
			wtf[i] = n.(int)
		}
		res, zerores = processSlice(wtf, res, zerores)
	})
	return res
}

func main() {
	_, filename, _, _ := runtime.Caller(0)
	filepath := path.Join(path.Dir(filename), "day8.txt")
	lines := readFile(filepath)
	numbers := convertStringSliceToIntSlice(lines)
	// fmt.Println(part1(numbers, 150))
	fmt.Println(part1RX(numbers, 150))

	// part2(numbers, 150)

}
