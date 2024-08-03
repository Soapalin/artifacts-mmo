import requests
import datetime
from artifact_connect import ArtefactConnect

class Player(ArtefactConnect):
    def __init__(self, name, jwt):
        self.name = name
        self.request = ArtefactConnect.__init__(self, jwt=jwt)
        self.auth_header = {'Authorization': "Bearer " + self.jwt, 'Content-Type': 'application/json', 'Accept': 'application/json'}
        self.cooldown = 0
        self.last_updated = datetime.datetime.now()

    def move(self, x, y):
        body = "{" + f"\"x\": \"{x}\",\"y\": \"{y}\""  + "}"
        # body = {'x': x, 'y': y}
        move_api = f"https://api.artifactsmmo.com/my/{self.name}/action/move"
        r = requests.post(move_api, data=body, headers=self.auth_header)
        print(r.status_code)
        if r.status_code == 200:
            # print(r.json())
            response = r.json()["data"]
            print(response["cooldown"])