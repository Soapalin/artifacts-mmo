from enum import Enum 
from player import Player 
class CharacterType(Enum):
    FIGHTER = 0 
    GATHERER = 1
    CRAFTER = 2 

class ArtifactAlgorithm(Player):
    def __init__(self, jwt):
        self.jwt = jwt 
        self.server = "https://api.artifactsmmo.com"
        print(self.server)

    def fighter():
        """
        Figher type of character will fight most of the time and explore the map
        """
        pass
    
    def gatherer():
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




