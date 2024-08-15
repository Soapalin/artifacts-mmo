import os
from dotenv import load_dotenv
from player import Player
import time
import sys
from artifact_connect import ArtifactAlgorithm

load_dotenv()
ACCOUNT_JWT = os.getenv("JWT_KEY")
CHARACTER_NAMES = ["Hephaestus"]

hephaestus = ArtifactAlgorithm(name="Hephaestus", jwt=ACCOUNT_JWT)


# hephaestus.move(2,1) # weaponscrafting
# hephaestus.move(3,1) # gearcrafting
# hephaestus.move(1,5) #forge 
# hephaestus.move_to_closest_bank()
# hephaestus.batch_deposit_items_to_bank()
# hephaestus.deposit_gold_to_bank()

while True:
    try:
        hephaestus.gatherer(6,1)


    except KeyboardInterrupt:
        sys.exit()

