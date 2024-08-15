import os
from dotenv import load_dotenv
from player import Player
import time
import sys
import random
from artifact_connect import ArtifactAlgorithm

load_dotenv()
ACCOUNT_JWT = os.getenv("JWT_KEY")
CHARACTER_NAMES = ["Suiren"]

suiren = ArtifactAlgorithm(name="Suiren", jwt=ACCOUNT_JWT)

try:
    while True:
        suiren.gatherer(2,0)

except KeyboardInterrupt:
    print("Keyboard Interrrupt")
    sys.exit()

