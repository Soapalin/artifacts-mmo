from enum import Enum 
from player import Player 
class CharacterType(Enum):
    FIGHTER = 0 
    GATHERER = 1
    CRAFTER = 2 

class ArtifactAlgorithm(Player):
    def __init__(self, name, jwt):
        self.server = "https://api.artifactsmmo.com"
        self.player = Player(name, jwt)
        print(self.server)

        # Locations
        self.bank = [4, 1]

    def fighter(self, x, y, loop_size=60):
        """
        Figher type of character will fight most of the time and explore the map
        """
        self.player.move(x,y) 
        for i in range(loop_size):
            status_code, response = self.player.fight()
            if status_code != 200:
                print(f"Failed to fight: {response}")
                if status_code == 497:
                    print(f"Inventory full. Batch deposit all items to bank.")
                    self.player.move_to_closest_bank()
                    self.player.batch_deposit_items_to_bank()
                    self.player.deposit_gold_to_bank()
                    self.player.move(x,y)
            else:
                print(f"Fought and waited for cooldown: {response['cooldown']['remaining_seconds'] + 1}s")
    
    def gatherer(self, x, y, loop_size=60):
        """
        Gatherer type of character will gather any types of resources
        """
        pass


    def miner():
        """
        Miner type of character will gather mining resources
        """
        pass

    def crafter():
        """
        Crafter tpe of characgter will spent most of their time craft. 
        """
        pass




