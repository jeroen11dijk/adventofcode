package main

import (
	"path"
	"runtime"
	"testing"

	"github.com/stretchr/testify/assert"
)

func Test_readFile(t *testing.T) {
	_, filename, _, _ := runtime.Caller(0)
	filepath := path.Join(path.Dir(filename), "day8_test.txt")
	lines := readFile(filepath)
	assert.Equal(t, []string{"0222112222120000"}, lines, "The two words should be the same.")
}

func Test_convertStringSliceToIntSlice(t *testing.T) {
	numbers := convertStringSliceToIntSlice([]string{"123456789012"})
	assert.Equal(t, []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2}, numbers, "The two words should be the same.")
}

func Test_part1(t *testing.T) {
	_, filename, _, _ := runtime.Caller(0)
	filepath := path.Join(path.Dir(filename), "day8.txt")
	lines := readFile(filepath)
	numbers := convertStringSliceToIntSlice(lines)
	assert.Equal(t, 1596, part1(numbers, 150), "The two words should be the same.")
}
