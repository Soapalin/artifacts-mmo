from enum import Enum
from artifact_connect import ARTIFACT_SERVER
import requests


class MapContentType(Enum):
    MONSTER = "monster"
    RESOURCE = "resource"
    WORKSHOP = "workshop"
    BANK = "bank"
    GRAND_EXCHANGE = "grand_exchange"
    TASKS_MASTER = "tasks_master"


class Location():
    def __init__(self, x, y, level_required=1, drops=[]):
        self.x = x
        self.y = y
        self.level_required = level_required
        self.drops = drops

    def get(self):
        return (self.x, self.y)

class Map():
    BANK = (4,1)
    GRAND_EXCHANGE = (5,1)

    class Wood():
        ASH = Location(x=7, y=1, level_required=1)

    class FishingSpot():
        GUDGEON = Location(x=4, y=2, level_required=1)
        SHRIMP = Location(x=5, y=2, level_required=10)

    class Monsters():
        CHICKEN = Location(x=0, y=1, level_required=1)

class Map():
    def __init__(self):
        self.size = 100
        self.server = ARTIFACT_SERVER

    def get_all_map_type(self, map_type=""):
        map_url = f"{ARTIFACT_SERVER}/maps?size={self.size}"

        if map_type != "":
            map_url = f"{ARTIFACT_SERVER}/maps?size={self.size}&content_type={map_type}"

        r = requests.get(map_url)
        if r.status_code == 200:
            response = r.json()["data"]
            return response
        self.MAP = []

    def get_mining_map():
        resource_map = []
        mining_map = []
        for location in resource_map:  
            if "rock" in location:
                mining_map.append(location)

        return mining_map

    def get_woodcutting_map():
        resource_map = []
        mining_map = []
        for location in resource_map:  
            if "tree" in location:
                mining_map.append(location)

        return mining_map
    
    def get_fishing_spot_map():
        resource_map = []
        mining_map = []
        for location in resource_map:  
            if "fishing_spot" in location:
                mining_map.append(location)

        return mining_map


