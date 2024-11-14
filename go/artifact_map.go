package main

import "fmt"

const (
	Monster       string = "monster"
	Resource      string = "resource"
	Workshop      string = "workshop"
	Bank          string = "bank"
	GrandExchange string = "grand_exchange"
	TasksMaster   string = "tasks_master"
)

type Location struct {
	name          string
	x             int
	y             int
	levelRequired int
	content       string
}

func (l *Location) Get() (int, int) {
	return l.x, l.y
}

func (l *Location) String() string {
	return fmt.Sprintf("%s (%d, %d)", l.name, l.x, l.y)
}

type ArtifactMap struct {
	URL                 string
	miningLocation      []Location
	fishingLocation     []Location
	woodcuttingLocation []Location
	monsterLocation     []Location
	bankLocation        []Location
	grandExchange       []Location
	tasksMaster         []Location
}

func (m *ArtifactMap) Init() {
	fmt.Printf("ArtifactMap | Init() | URL: %s\n", m.URL)
}
