import os
from dotenv import load_dotenv
from player import Player

load_dotenv()
ACCOUNT_JWT = os.getenv("JWT_KEY")
CHARACTER_NAMES = ["Rinsyi"]

rinsyi = Player(name="Rinsyi", jwt=ACCOUNT_JWT)
rinsyi.move(0,1)
# rinsyi.move(0,0)

