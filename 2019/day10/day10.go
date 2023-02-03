package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"path"
	"runtime"
	"sort"

	mapset "github.com/deckarep/golang-set/v2"
)

type Asteroid struct {
	x int
	y int
}

func distance(a Asteroid, b Asteroid) float64 {
	return math.Sqrt(math.Pow(float64(a.x-b.x), 2) + math.Pow(float64(a.y-b.y), 2))
}

func getAsteroids(filepath string) []Asteroid {
	file, _ := os.Open(filepath)
	scanner := bufio.NewScanner(file)
	y := 0
	asteroids := []Asteroid{}
	for scanner.Scan() {
		line := scanner.Text()
		for x, character := range line {
			if character == '#' {
				asteroids = append(asteroids, Asteroid{x, y})
			}
		}
		y++
	}
	return asteroids
}

func getVision(asteroid Asteroid, asteroids []Asteroid) mapset.Set[Asteroid] {
	res := mapset.NewSet[Asteroid]()
	for _, nbr := range asteroids {
		if asteroid != nbr {
			angle := math.Atan2(float64(nbr.y-asteroid.y), float64(nbr.x-asteroid.x)) * (180 / math.Pi)
			dist := distance(asteroid, nbr)
			seen := true
			for _, other := range asteroids {
				if asteroid != other && nbr != other {
					angle2 := math.Atan2(float64(other.y-asteroid.y), float64(other.x-asteroid.x)) * (180 / math.Pi)
					dist2 := distance(asteroid, other)
					if angle == angle2 && dist2 < dist {
						seen = false
						break
					}
				}
			}
			if seen {
				res.Add(nbr)
			}
		}
	}
	return res
}

func part1(filepath string) int {
	asteroids := getAsteroids(filepath)
	res := 0
	for _, asteroid := range asteroids {
		res = int(math.Max(float64(res), float64(len(getVision(asteroid, asteroids).ToSlice()))))
	}
	return res
}

func part2(filepath string) int {
	asteroids := getAsteroids(filepath)
	res := 0
	var best Asteroid
	var bestVision mapset.Set[Asteroid]
	for _, asteroid := range asteroids {
		vision := getVision(asteroid, asteroids)
		if len(vision.ToSlice()) > res {
			res = len(vision.ToSlice())
			best = asteroid
			bestVision = vision
		}
	}
	laserOrder := make(map[Asteroid]int)
	for _, asteroid := range bestVision.ToSlice() {
		laserOrder[asteroid] = int(math.Atan2(float64(best.y-asteroid.y), float64(best.x-asteroid.x))*(180/math.Pi)+270) % 360
	}
	keys := make([]Asteroid, 0, len(laserOrder))
	for key := range laserOrder {
		keys = append(keys, key)
	}
	sort.SliceStable(keys, func(i, j int) bool {
		return laserOrder[keys[i]] < laserOrder[keys[j]]
	})
	return keys[199].x*100 + keys[199].y
}

func main() {
	_, filename, _, _ := runtime.Caller(0)
	filepath := path.Join(path.Dir(filename), "day10.txt")
	fmt.Println(part1(filepath))
	fmt.Println(part2(filepath))
}
