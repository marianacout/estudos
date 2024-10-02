package main

import "fmt"

func main() {

	slice := make([]string, 5)
	slice[0] = "Olá"
	slice[1] = "Mundo"
	fmt.Println(slice[0], slice[1])
	fmt.Println(slice[0])
	fmt.Println(slice[1])
	fmt.Println(slice[2])
	slice[2] = "Mari"
	fmt.Println(slice[2])
	fmt.Println(slice)

	fmt.Println(len(slice))
}
