package main

import "fmt"

// A PlayerRole is the primary role of a character in its tasks
type PlayerRole int

const (
	Fighter    PlayerRole = iota
	Crafter    PlayerRole = iota
	Miner      PlayerRole = iota
	Woodcutter PlayerRole = iota
	Fisherman  PlayerRole = iota
)

func (pr PlayerRole) String() string {
	switch pr {
	case Fighter:
		return "Fighter"
	case Crafter:
		return "Crafter"
	case Miner:
		return "Miner"
	case Woodcutter:
		return "Woodcutter"
	case Fisherman:
		return "Fisherman"
	default:
		return "Error"
	}
}

type InventorySlot struct {
	slot     int
	code     string
	quantity string
}

// Player structure
type Player struct {
	Name string
	Role PlayerRole

	x int
	y int

	cooldon             int
	cooldown_expiration string

	weapon_slot               string
	shield_slot               string
	helmet_slot               string
	body_armor_slot           string
	leg_armor_slot            string
	boots_slot                string
	ring1_slot                string
	ring2_slot                string
	amulet_slot               string
	artifact1_slot            string
	artifact2_slot            string
	artifact3_slot            string
	consumable1_slot          string
	consumable1_slot_quantity int
	consumable2_slot          string
	consumable2_slot_quantity int

	hp              int
	haste           int
	critical_strike int
	stamina         int
	attack_fire     int
	attack_earth    int
	attack_water    int
	attack_air      int
	dmg_fire        int
	dmg_earth       int
	dmg_water       int
	dmg_air         int
	res_fire        int
	res_earth       int
	res_water       int
	res_air         int

	level              int
	xp                 int
	max_xp             int
	achievements_point int
	gold               int
	// speed int
	mining_level           int
	mining_xp              int
	mining_max_xp          int
	woodcutting_level      int
	woodcutting_xp         int
	woodcutting_max_xp     int
	fishing_level          int
	fishing_xp             int
	fishing_max_xp         int
	weaponcrafting_level   int
	weaponcrafting_xp      int
	weaponcrafting_max_xp  int
	gearcrafting_level     int
	gearcrafting_xp        int
	gearcrafting_max_xp    int
	jewelrycrafting_level  int
	jewelrycrafting_xp     int
	jewelrycrafting_max_xp int
	cooking_level          int
	cooking_xp             int
	cooking_max_xp         int

	task          string
	task_type     string
	task_progress int
	task_total    int

	inventory_max_items int
	inventory           []InventorySlot

	isBusy      bool // character needed by another character, usually for crafting
	hasCooldown bool // character on cooldown
}

func (p *Player) Init() {
	fmt.Printf("Player | Name: %s | Role: %s\n", p.Name, p.Role.String())

}

func (p *Player) String() string {
	return fmt.Sprintf("%s", p.Name)
}

func (p *Player) Move(x, y int) {

}

func (p *Player) Fight() {

}

func (p *Player) Fish() {

}

func (p *Player) Mine() {

}

func (p *Player) Woodcut() {

}

func (p *Player) Craft() {

}
