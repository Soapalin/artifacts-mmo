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
        pass





