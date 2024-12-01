package main

import (
	"os"
	"testing"
)

func TestSumOfPairsDistance_Sample(t *testing.T) {
	input, err := os.ReadFile("day_01_sample.txt")
	if err != nil {
		t.Fatalf(`os.ReadFile("day_01_sample.txt") = %v, want nil`, err)
	}
	distance := SumOfPairsDistance(string(input))
	if distance != 11 {
		t.Fatalf(`SumOfPairsDistance("day_01_sample.txt") = %d, want 11`, distance)
	}
}

func TestSumOfPairsDistance_Test(t *testing.T) {
	input, err := os.ReadFile("day_01_test.txt")
	if err != nil {
		t.Fatalf(`os.ReadFile("day_01_test.txt") = %v, want nil`, err)
	}
	distance := SumOfPairsDistance(string(input))
	if distance != 2756096 {
		t.Fatalf(`SumOfPairsDistance("day_01_test.txt") = %d, want 2756096`, distance)
	}
}

func TestGetSimilarities_Sample(t *testing.T) {
	input, err := os.ReadFile("day_01_sample.txt")
	if err != nil {
		t.Fatalf(`os.ReadFile("day_01_sample.txt") = %v, want nil`, err)
	}
	similarities := GetSimilarities(string(input))
	if similarities != 31 {
		t.Fatalf(`GetSimilarities("day_01_sample.txt") = %d, want 31`, similarities)
	}
}

func TestGetSimilarities_Test(t *testing.T) {
	input, err := os.ReadFile("day_01_test.txt")
	if err != nil {
		t.Fatalf(`os.ReadFile("day_01_test.txt") = %v, want nil`, err)
	}
	similarities := GetSimilarities(string(input))
	if similarities != 23117829 {
		t.Fatalf(`GetSimilarities("day_01_test.txt") = %d, want 23117829`, similarities)
	}
}
