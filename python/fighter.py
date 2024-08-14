import os
from dotenv import load_dotenv
from player import Player
import time
import sys
from artifact_connect import ArtifactAlgorithm

load_dotenv()
ACCOUNT_JWT = os.getenv("JWT_KEY")
CHARACTER_NAMES = ["Rinsyi"]

# rinsyi = Player(name="Rinsyi", jwt=ACCOUNT_JWT)

rinsyi = ArtifactAlgorithm(name="Rinsyi", jwt=ACCOUNT_JWT)


# rinsyi.move_to_closest_bank()
# rinsyi.batch_deposit_items_to_bank()
# rinsyi.deposit_gold_to_bank()

while True:
    try:
        # rinsyi.move(2,0) # copper rocks
        # for i in range(60):
        #     status_code, response = rinsyi.gathering()
        #     if status_code != 200:
        #         print(f"Failed to gather: {response}")
        #         if status_code == 497:
        #             print(f"Inventory full. Batch deposit all items to bank.")
        #             # rinsyi.deposit_item_to_bank(item_code="chicken", )
        #             rinsyi.move_to_closest_bank()
        #             rinsyi.batch_deposit_items_to_bank()
        #             rinsyi.deposit_gold_to_bank()
        #             rinsyi.move(2,0)
        #     else:
        #         print(f"Gathered copper rocks and waited for cooldown: {response['cooldown']['remaining_seconds'] + 1}s")

        # rinsyi.move(4,2) # gudgeon fishing spot
        # for i in range(30):
        #     status_code, response = rinsyi.gathering()
        #     if status_code != 200:
        #         print(f"Failed to gather: {response}")
        #         if status_code == 497:
        #             print(f"Inventory full. Batch deposit all items to bank.")
        #             # rinsyi.deposit_item_to_bank(item_code="chicken", )
        #             rinsyi.move_to_closest_bank()
        #             rinsyi.batch_deposit_items_to_bank()
        #             rinsyi.deposit_gold_to_bank()
        #             rinsyi.move(4,2)
        #     else:
        #         print(f"Fished gudgeon fishing spot and waited for cooldown: {response['cooldown']['remaining_seconds'] + 1}s")


        # rinsyi.move(5,2) # shrimp fishing spot need lvl 10
        # for i in range(30):
        #     status_code, response = rinsyi.gathering()
        #     if status_code != 200:
        #         print(f"Failed to gather: {response}")
        #         if status_code == 497:
        #             print(f"Inventory full. Batch deposit all items to bank.")
        #             # rinsyi.deposit_item_to_bank(item_code="chicken", )
        #             rinsyi.move_to_closest_bank()
        #             rinsyi.batch_deposit_items_to_bank()
        #             rinsyi.deposit_gold_to_bank()
        #             rinsyi.move(5,2)
        #     else:
        #         print(f"Fished shrimp fishing spot and waited for cooldown: {response['cooldown']['remaining_seconds'] + 1}s")

        # rinsyi.move(0,1) # chicken
        # for i in range(60):
        #     status_code, response = rinsyi.fight()
        #     if status_code != 200:
        #         print(f"Failed to fight: {response}")
        #         if status_code == 497:
        #             print(f"Inventory full. Batch deposit all items to bank.")
        #             # rinsyi.deposit_item_to_bank(item_code="chicken", )
        #             rinsyi.move_to_closest_bank()
        #             rinsyi.batch_deposit_items_to_bank()
        #             rinsyi.deposit_gold_to_bank()
        #             rinsyi.move(0,1)
        #     else:
        #         print(f"Fought and waited for cooldown: {response['cooldown']['remaining_seconds'] + 1}s")
        rinsyi.fighter(x=2, y=-2)

        # rinsyi.move(3,-2) # green slime
        # for i in range(60):
        #     status_code, response = rinsyi.fight()
        #     if status_code != 200:
        #         print(f"Failed to fight: {response}")
        #         if status_code == 497:
        #             print(f"Inventory full. Batch deposit all items to bank.")
        #             rinsyi.move_to_closest_bank()
        #             rinsyi.batch_deposit_items_to_bank()
        #             rinsyi.deposit_gold_to_bank()
        #             rinsyi.move(3,-2)
        #     else:
        #         print(f"Fought and waited for cooldown: {response['cooldown']['remaining_seconds'] + 1}s")


        # rinsyi.move(6,1) # ash tree
        # for i in range(30):
        #     status_code, response = rinsyi.gathering()
        #     if status_code != 200:
        #         print(f"Failed to gather: {response}")
        #         if status_code == 497:
        #             print(f"Inventory full. Batch deposit all items to bank.")
        #             # rinsyi.deposit_item_to_bank(item_code="chicken", )
        #             rinsyi.move_to_closest_bank()
        #             rinsyi.batch_deposit_items_to_bank()
        #             rinsyi.deposit_gold_to_bank()
        #             rinsyi.move(6,1)
        #     else:
        #         print(f"Gathered ash trees and waited for cooldown: {response['cooldown']['remaining_seconds'] + 1}s")


    except KeyboardInterrupt:
        sys.exit()

