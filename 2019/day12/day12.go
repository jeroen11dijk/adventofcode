package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"path"
	"reflect"
	"regexp"
	"runtime"
	"strconv"
)

func part1(filepath string) int {
	file, _ := os.Open(filepath)
	scanner := bufio.NewScanner(file)
	moons := make([][]int, 0)
	vel := make([][]int, 0)
	for scanner.Scan() {
		line := scanner.Text()
		re := regexp.MustCompile("-?\\d*\\.{0,1}\\d+")
		moonPos := make([]int, 0)
		for _, val := range re.FindAllString(line, -1) {
			val, _ := strconv.Atoi(val)
			moonPos = append(moonPos, val)
		}
		moons = append(moons, moonPos)
		vel = append(vel, []int{0, 0, 0})
	}
	for range make([]int, 1000) {
		// Update velocity first
		for moonIndex, moon := range moons {
			for index := 0; index < 3; index++ {
				for _, other := range moons {
					if !reflect.DeepEqual(moon, other) {
						if moon[index] < other[index] {
							vel[moonIndex][index] += 1
						}
						if moon[index] > other[index] {
							vel[moonIndex][index] -= 1
						}
					}
				}
			}
		}
		// Update positions
		for moonIndex, moon := range moons {
			for index := 0; index < 3; index++ {
				moon[index] += vel[moonIndex][index]
			}
		}
	}
	res := 0
	for moonIndex, moon := range moons {
		pot, kin := 0, 0
		for index := 0; index < 3; index++ {
			pot += int(math.Abs(float64(moon[index])))
			kin += int(math.Abs(float64(vel[moonIndex][index])))
		}
		res += pot * kin
	}
	return res
}

func getState(moons [][]int, vel [][]int) []string {
	res := []string{"", "", ""}
	for moonIndex, moon := range moons {
		for index := 0; index < 3; index++ {
			res[index] += fmt.Sprint(moon[index])
			res[index] += fmt.Sprint(vel[moonIndex][index])
		}
	}
	return res
}

// greatest common divisor (GCD) via Euclidean algorithm
func GCD(a, b int) int {
	for b != 0 {
		t := b
		b = a % b
		a = t
	}
	return a
}

// find Least Common Multiple (LCM) via GCD
func LCM(a, b int, integers ...int) int {
	result := a * b / GCD(a, b)

	for i := 0; i < len(integers); i++ {
		result = LCM(result, integers[i])
	}

	return result
}

func part2(filepath string) int {
	file, _ := os.Open(filepath)
	scanner := bufio.NewScanner(file)
	moons := make([][]int, 0)
	vel := make([][]int, 0)
	for scanner.Scan() {
		line := scanner.Text()
		re := regexp.MustCompile("-?\\d*\\.{0,1}\\d+")
		moonPos := make([]int, 0)
		for _, val := range re.FindAllString(line, -1) {
			val, _ := strconv.Atoi(val)
			moonPos = append(moonPos, val)
		}
		moons = append(moons, moonPos)
		vel = append(vel, []int{0, 0, 0})
	}
	initStates := getState(moons, vel)
	XStates, YStates, ZStates := make(map[string]int), make(map[string]int), make(map[string]int)
	XStates[initStates[0]], YStates[initStates[0]], ZStates[initStates[0]] = 0, 0, 0
	frequences := []int{0, 0, 0}
	step := 0
	for {
		// Update velocity first
		for moonIndex, moon := range moons {
			for index := 0; index < 3; index++ {
				for _, other := range moons {
					if !reflect.DeepEqual(moon, other) {
						if moon[index] < other[index] {
							vel[moonIndex][index] += 1
						}
						if moon[index] > other[index] {
							vel[moonIndex][index] -= 1
						}
					}
				}
			}
		}
		// Update positions
		for moonIndex, moon := range moons {
			for index := 0; index < 3; index++ {
				moon[index] += vel[moonIndex][index]
			}
		}
		states := getState(moons, vel)
		step += 1
		val, ok := XStates[states[0]]
		if ok && frequences[0] == 0 {
			frequences[0] = step - val
		}
		val1, ok1 := YStates[states[1]]
		if ok1 && frequences[1] == 0 {
			frequences[1] = step - val1
		}
		val2, ok2 := ZStates[states[2]]
		if ok2 {
			frequences[2] = step - val2
		}
		XStates[states[0]], YStates[states[1]], ZStates[states[2]] = step, step, step
		if frequences[0] != 0 && frequences[1] != 0 && frequences[2] != 0 {
			fmt.Println(frequences)
			break
		}
	}
	return LCM(frequences[0], frequences[1], frequences[2])
}

func main() {
	_, filename, _, _ := runtime.Caller(0)
	filepath := path.Join(path.Dir(filename), "day12.txt")
	// fmt.Println(part1(filepath))
	fmt.Println(part2(filepath))
}
