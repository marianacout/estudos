package main

import "fmt"

func main() {

	numPares := []int{2, 4, 6, 8, 10, 12}
	fmt.Println(numPares)

	numPares = append(numPares, 14, 16, 18, 20)
	fmt.Println(numPares)
}
