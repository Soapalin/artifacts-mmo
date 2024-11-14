package main

const (
	ARTIFACT_SERVER = "api"
)

func main() {
	// characters := []string{
	// 	"Rinsyi",
	// 	"Hephaestos",
	// 	"Suiren",
	// 	// Player #4
	// 	// Player #5
	// }
	artifactMap := ArtifactMap{URL: "url/test"}
	artifactMap.Init()

	rinsyi := Player{
		Name: "Rinsyi",
		Role: Fighter,
	}
	rinsyi.Init()

	crafter := Player{
		Name: "Hephaestos",
		Role: Crafter,
	}
	crafter.Init()

	miner := Player{
		Name: "Suiren",
		Role: Miner,
	}
	miner.Init()

	woodcutter := Player{
		Name: "Houyi",
		Role: Woodcutter,
	}
	woodcutter.Init()

	fisherman := Player{
		Name: "Fisherthem",
		Role: Fisherman,
	}
	fisherman.Init()

	RunAlgorithm([]Player{rinsyi}, []Player{crafter}, []Player{fisherman}, []Player{miner}, []Player{woodcutter})

}
