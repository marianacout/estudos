package main

import "fmt"

func main() {

	numPrimos := [6]int{2, 3, 5, 7, 11, 13}
	fmt.Println(numPrimos)
	fmt.Println(numPrimos[0])
	fmt.Println(numPrimos[1])
	fmt.Println(numPrimos[0:4])
	fmt.Println(numPrimos[:1])
	fmt.Println(numPrimos[2:])
}
