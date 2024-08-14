import os
from dotenv import load_dotenv
from player import Player
import time
import sys

load_dotenv()
ACCOUNT_JWT = os.getenv("JWT_KEY")
CHARACTER_NAMES = ["Hephaestus"]

hephaestus = Player(name="Hephaestus", jwt=ACCOUNT_JWT)


# hephaestus.move(2,1) # weaponscrafting
# hephaestus.move(3,1) # gearcrafting
# hephaestus.move(1,5) #forge 
# hephaestus.move_to_closest_bank()
# hephaestus.batch_deposit_items_to_bank()
# hephaestus.deposit_gold_to_bank()

while True:
    try:
        # hephaestus.move(2,0) # copper rocks
        # for i in range(60):
        #     status_code, response = hephaestus.gathering()
        #     if status_code != 200:
        #         print(f"Failed to gather: {response}")
        #         if status_code == 497:
        #             print(f"Inventory full. Batch deposit all items to bank.")
        #             hephaestus.move_to_closest_bank()
        #             hephaestus.batch_deposit_items_to_bank()
        #             hephaestus.deposit_gold_to_bank()
        #             hephaestus.move(2,0)
        #     else:
        #         print(f"Gathered copper rocks and waited for cooldown: {response['cooldown']['remaining_seconds'] + 1}s")



        hephaestus.move(6,1) # ash tree
        for i in range(30):
            status_code, response = hephaestus.gathering()
            if status_code != 200:
                print(f"Failed to gather: {response}")
                if status_code == 497:
                    print(f"Inventory full. Batch deposit all items to bank.")
                    hephaestus.move_to_closest_bank()
                    hephaestus.batch_deposit_items_to_bank()
                    hephaestus.deposit_gold_to_bank()
                    hephaestus.move(6,1)
            else:
                print(f"Gathered ash trees and waited for cooldown: {response['cooldown']['remaining_seconds'] + 1}s")


        hephaestus.move(1,5) #forge 
        


    except KeyboardInterrupt:
        sys.exit()

