package main

import "fmt"

func RunAlgorithm(fighters, crafters, fishermen, miners, woodcutters []Player) {
	fmt.Println("RunAlgorithm | ")

	// fighter
	// fight the strongest monster it can, starting from the weakest
	// analyse monsters stats to check average lvl to fight the monsters
	// sell loot in grand_exchange, put in storage or recycle

	// if fishermen not busy, get fishermen to fish at the highest level spot and give fighter a stack
	// takes the fighters loot to sell maybe?

	// crafter
	// decides on what to craft depending on:
	// what the fighter is missing,
	// the lowest level of the equipment of the fighter
	// lowest skill of the crafter to bring up to speed

	// 	depending on what to craft, get miner and wood cutter to get the mat to craft few
	// crafter give new tools to fighter if it is better than current equipment
}
