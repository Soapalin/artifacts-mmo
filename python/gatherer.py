import os
from dotenv import load_dotenv
from player import Player
import time
import sys
import random

load_dotenv()
ACCOUNT_JWT = os.getenv("JWT_KEY")
CHARACTER_NAMES = ["Suiren"]

suiren = Player(name="Suiren", jwt=ACCOUNT_JWT)


# suiren.move_to_closest_bank()
# suiren.batch_deposit_items_to_bank()
# suiren.deposit_gold_to_bank()

while True:
    try:
        suiren.move(2,0) # copper rocks
        for i in range(60):
            status_code, response = suiren.gathering()
            if status_code != 200:
                print(f"Failed to gather: {response}")
                if status_code == 497:
                    print(f"Inventory full. Crafting copper and deposit to bank.")
                    suiren.move(1,5) #forge
                    suiren.craft_copper()
                    suiren.move_to_closest_bank()
                    suiren.batch_deposit_items_to_bank()
                    suiren.deposit_gold_to_bank()
                    suiren.move(2,0)
            else:
                print(f"Gathered copper rocks and waited for cooldown: {response['cooldown']['remaining_seconds'] + 1}s")



        # suiren.move(6,1) # ash tree
        # for i in range(30):
        #     status_code, response = suiren.gathering()
        #     if status_code != 200:
        #         print(f"Failed to gather: {response}")
        #         if status_code == 497:
        #             print(f"Inventory full. Batch deposit all items to bank.")
        #             suiren.move_to_closest_bank()
        #             suiren.batch_deposit_items_to_bank()
        #             suiren.deposit_gold_to_bank()
        #             suiren.move(6,1)
        #     else:
        #         print(f"Gathered ash trees and waited for cooldown: {response['cooldown']['remaining_seconds'] + 1}s")


    except KeyboardInterrupt:
        sys.exit()

