package main

import (
	"fmt"
	"math"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	input, err := os.ReadFile("day_01_test.txt")
	if err != nil {
		panic("could not read file: \"day_01_test.txt\"")
	}

	distance := SumOfPairsDistance(string(input))
	fmt.Printf("Distance: %v", distance)

	similarities := GetSimilarities(string(input))
	fmt.Printf("Similarities: %v", similarities)
}

func SumOfPairsDistance(input string) int {
	sum := 0
	lhs, rhs := splitVertically(input)

	sort.Ints(lhs)
	sort.Ints(rhs)

	for i := 0; i < len(lhs) && i < len(rhs); i++ {
		sum += int(math.Abs(float64(lhs[i] - rhs[i])))
	}
	return sum
}

func GetSimilarities(input string) int {
	similarity := 0
	lhs, rhs := splitVertically(input)

	for _, l := range lhs {
		occurrences := 0
		for _, r := range rhs {
			if r == l {
				occurrences++
			}
		}
		similarity += l * occurrences
	}
	return similarity
}

func splitVertically(input string) ([]int, []int) {
	var lhs, rhs []int

	for _, line := range strings.Split(input, "\n") {
		if line == "" {
			break
		}

		parts := strings.Fields(line) // Split by whitespace
		if len(parts) < 2 {
			continue
		}

		l, err1 := strconv.Atoi(parts[0])
		r, err2 := strconv.Atoi(parts[1])
		if err1 != nil || err2 != nil {
			continue // Skip invalid lines
		}

		lhs = append(lhs, l)
		rhs = append(rhs, r)
	}

	return lhs, rhs
}
