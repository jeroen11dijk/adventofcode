package main

import (
	"bufio"
	"fmt"
	"os"
	"path"
	"runtime"
	. "github.com/sbwhitecap/tqdm/iterators"
	"github.com/sbwhitecap/tqdm"
)

func rollStones(lines [][]rune, leftToRight bool) {
	if !leftToRight {
		for i := range lines {
			reverseLine(lines[i])
		}
	}

	for _, line := range lines {
		madeChange := true
		for madeChange {
			madeChange = false
			for i := 1; i < len(line); i++ {
				if line[i] == 'O' && line[i-1] == '.' {
					madeChange = true
					line[i-1], line[i] = line[i], line[i-1]
				}
			}
		}
	}

	if !leftToRight {
		for i := range lines {
			reverseLine(lines[i])
		}
	}
}

func reverseLine(line []rune) {
	for i, j := 0, len(line)-1; i < j; i, j = i+1, j-1 {
		line[i], line[j] = line[j], line[i]
	}
}

func puzzle1(filePath string) int {
	file, err := os.Open(filePath)
	if err != nil {
		fmt.Println("Error opening file:", err)
		return 0
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var grid [][]rune

	for scanner.Scan() {
		line := scanner.Text()
		for i, char := range line {
			if len(grid) <= i {
				grid = append(grid, []rune{})
			}
			grid[i] = append(grid[i], char)
		}
	}

	rollStones(grid, true)

	res := 0
	for _, line := range grid {
		reverseLine(line)
		for i, val := range line {
			if val == 'O' {
				res += i + 1
			}
		}
	}

	return res
}

func transpose(grid [][]rune) [][]rune {
	if len(grid) == 0 {
		return grid
	}
	transposed := make([][]rune, len(grid[0]))
	for i := range transposed {
		transposed[i] = make([]rune, len(grid))
		for j := range transposed[i] {
			transposed[i][j] = grid[j][i]
		}
	}
	return transposed
}

func puzzle2(filePath string) int {
	file, err := os.Open(filePath)
	if err != nil {
		fmt.Println("Error opening file:", err)
		return 0
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var grid [][]rune

	for scanner.Scan() {
		line := scanner.Text()
		for i, char := range line {
			if len(grid) <= i {
				grid = append(grid, []rune{})
			}
			grid[i] = append(grid[i], char)
		}
	}

    tqdm.With(Interval(0, 1000000000), "", func(v interface{}) (brk bool) {
        rollStones(grid, true)
        grid = transpose(grid)
        rollStones(grid, true)
        grid = transpose(grid)
        rollStones(grid, false)
        grid = transpose(grid)
        rollStones(grid, false)
        grid = transpose(grid)
        return
    })

	res := 0
	for _, line := range grid {
		reverseLine(line)
		for i, val := range line {
			if val == 'O' {
				res += i + 1
			}
		}
	}

	return res
}

func main() {
	_, filename, _, _ := runtime.Caller(0)
	filepath := path.Join(path.Dir(filename), "day14.txt")
	fmt.Println("Result:", puzzle1(filepath))
	fmt.Println("Result:", puzzle2(filepath))
}
