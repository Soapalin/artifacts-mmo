import requests
import datetime

class Player():
    def __init__(self, name, jwt):
        self.name = name
        self.jwt = jwt 
        self.auth_header = {'Authorization': "Bearer " + self.jwt, 'Content-Type': 'application/json', 'Accept': 'application/json'}
        self.cooldown = 0
        self.server = "https://api.artifactsmmo.com" 
        self.last_updated = datetime.datetime.now()

    def move(self, x, y):
        body = "{" + f"\"x\": \"{x}\",\"y\": \"{y}\""  + "}"
        move_api = f"{self.server}/my/{self.name}/action/move"
        r = requests.post(move_api, data=body, headers=self.auth_header)
        print(r.status_code)
        if r.status_code == 200:
            response = r.json()["data"]
            print(response)
            self.updateCooldown(response["cooldown"]["remaining_seconds"])
            return r.json()["data"]
        else:
            return r.json()
            

    def updateCooldown(self, cooldown):
        self.last_updated = datetime.datetime.now()
        self.cooldown = cooldown


    def fight(self):
        body = f""
        fight_api = f"{self.server}/my/{self.name}/action/fight"