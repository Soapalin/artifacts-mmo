import os
from dotenv import load_dotenv
from player import Player
import time
import sys

load_dotenv()
ACCOUNT_JWT = os.getenv("JWT_KEY")
CHARACTER_NAMES = ["Rinsyi"]

rinsyi = Player(name="Rinsyi", jwt=ACCOUNT_JWT)


rinsyi.move(0,1)

while True:
    try:
        status_code, response = rinsyi.fight()
        if status_code != 200:
            print(f"Failed to fight: {response}")
            if status_code == 497:
                print(f"Inventory full. Batch deposit all items to bank.")
                # rinsyi.deposit_item_to_bank(item_code="chicken", )
                rinsyi.move(4,1)
                rinsyi.batch_deposit_items_to_bank()
                rinsyi.move(0,1)
        else:
            print(f"Fought and waiting for cooldown: {response['cooldown']['remaining_seconds'] + 1}s")
            time.sleep(response["cooldown"]["remaining_seconds"] + 1)
    except KeyboardInterrupt:
        sys.exit() 

