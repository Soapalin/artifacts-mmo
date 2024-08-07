import requests
import datetime
import time

class Player():
    def __init__(self, name, jwt):
        self.name = name
        self.jwt = jwt 
        self.auth_header = {'Authorization': "Bearer " + self.jwt, 'Content-Type': 'application/json', 'Accept': 'application/json'}
        self.cooldown = 0
        self.server = "https://api.artifactsmmo.com" 
        self.last_updated = datetime.datetime.now()
        self.init_char_status()

    def init_char_status(self):
        status, response = self.fetch_character_status()
        if status == 200:
            self.level = response["level"]
            self.xp = response["xp"]
            self.max_xp = response["max_xp"]
            self.total_xp = response["total_xp"]
            self.gold = response["gold"]
            self.speed = response["speed"]
            self.mining_level = response["mining_level"]
            self.mining_xp = response["mining_xp"]
            self.mining_max_xp = response["mining_max_xp"]
            self.woodcutting_level = response["woodcutting_level"]
            self.woodcutting_xp = response["woodcutting_xp"]
            self.woodcutting_max_xp = response["woodcutting_max_xp"]
            self.fishing_level = response["fishing_level"]
            self.fishing_xp = response["fishing_xp"]
            self.fishing_max_xp = response["fishing_max_xp"]
            self.weaponcrafting_level = response["weaponcrafting_level"]
            self.weaponcrafting_xp = response["weaponcrafting_xp"]
            self.weaponcrafting_max_xp = response["weaponcrafting_max_xp"]
            self.gearcrafting_level = response["gearcrafting_level"]
            self.gearcrafting_xp = response["gearcrafting_xp"]
            self.gearcrafting_max_xp = response["gearcrafting_max_xp"]
            self.jewelrycrafting_level = response["jewelrycrafting_level"]
            self.jewelrycrafting_xp = response["jewelrycrafting_xp"]
            self.jewelrycrafting_max_xp = response["jewelrycrafting_max_xp"]
            self.cooking_level = response["cooking_level"]
            self.cooking_xp = response["cooking_xp"]
            self.cooking_max_xp = response["cooking_max_xp"]
            self.hp = response["hp"]
            self.haste = response["haste"]
            self.critical_strike = response["critical_strike"]
            self.stamina = response["stamina"]
            self.attack_fire = response["attack_fire"]
            self.attack_earth = response["attack_earth"]
            self.attack_water = response["attack_water"]
            self.attack_air = response["attack_air"]
            self.dmg_fire = response["dmg_fire"]
            self.dmg_earth = response["dmg_earth"]
            self.dmg_water = response["dmg_water"]
            self.dmg_air = response["dmg_air"]
            self.res_fire = response["res_fire"]
            self.res_earth = response["res_earth"]
            self.res_water = response["res_water"]
            self.res_air = response["res_air"]
            self.x = response["x"]
            self.y = response["y"]
            self.cooldown = response["cooldown"]
            print(self.cooldown)
            self.waitCooldown()
            self.cooldown_expiration = response["cooldown_expiration"]
            self.weapon_slot = response["weapon_slot"]
            self.shield_slot = response["shield_slot"]
            self.helmet_slot = response["helmet_slot"]
            self.body_armor_slot = response["body_armor_slot"]
            self.leg_armor_slot = response["leg_armor_slot"]
            self.boots_slot = response["boots_slot"]
            self.ring1_slot = response["ring1_slot"]
            self.ring2_slot = response["ring2_slot"]
            self.amulet_slot = response["amulet_slot"]
            self.artifact1_slot = response["artifact1_slot"]
            self.artifact2_slot = response["artifact2_slot"]
            self.artifact3_slot = response["artifact3_slot"]
            self.consumable1_slot = response["consumable1_slot"]
            self.consumable1_slot_quantity = response["consumable1_slot_quantity"]
            self.consumable2_slot = response["consumable2_slot"]
            self.consumable2_slot_quantity = response["consumable2_slot_quantity"]
            self.task = response["task"]
            self.task_type = response["task_type"]
            self.task_progress = response["task_progress"]
            self.task_total = response["task_total"]
            self.inventory_max_items = response["inventory_max_items"]
            self.inventory = response["inventory"]
        else:
            raise Exception(f"fetch_character_status: {status} - {response}")

    def move(self, x, y):
        body = "{" + f"\"x\": \"{x}\",\"y\": \"{y}\""  + "}"
        move_api = f"{self.server}/my/{self.name}/action/move"
        r = requests.post(move_api, data=body, headers=self.auth_header)
        print(f"move() | {r.status_code}")
        if r.status_code == 200:
            response = r.json()["data"]
            print(response)
            self.updateCooldown(response["cooldown"]["remaining_seconds"])
            self.waitCooldown()
            return r.json()["data"]
        else:
            return r.json()
            

    def updateCooldown(self, cooldown):
        self.last_updated = datetime.datetime.now()
        self.cooldown = cooldown

    def waitCooldown(self):
        print(f"waitCooldown | {self.cooldown}s")
        time.sleep(self.cooldown)


    def fetch_character_status(self):
        char_status = f"{self.server}/characters/{self.name}"
        r = requests.get(char_status, headers=self.auth_header)
        print(f"fetch_character_status | {r.status_code}")
        if r.status_code == 200:
            response = r.json()["data"]
            return r.status_code, response
        else:
            return r.status_code, r.json()
    

    def batch_deposit_items_to_bank(self):
        for item in self.inventory:
            if item["code"] != "":
                status, response = self.deposit_item_to_bank(item["code"], item["quantity"])
                if status == 491:
                    cooldown = response["error"]["message"].rstrip(" seconds left.")
                    cooldown = cooldown.lstrip("Character in cooldown: ")
                    cooldown = int(cooldown)
                    time.sleep(cooldown+1)
                    status, response = self.deposit_item_to_bank(item["code"], item["quantity"])



    def deposit_item_to_bank(self, item_code, quantity):
        deposit_api = f"{self.server}/my/{self.name}/action/bank/deposit"
        body = "{" + f"\"code\": \"{item_code}\",\"quantity\": {quantity}"  + "}"
        r = requests.post(deposit_api, data=body, headers=self.auth_header)
        if r.status_code == 200:
            print(f"Deposit Item To Bank: {item_code}, {quantity}")
            response = r.json()["data"]
            self.updateCooldown(response["cooldown"]["remaining_seconds"] + 1)
            self.waitCooldown()
            return r.status_code, response
        else:
            print(f"Fail to deposit to bank: {r.json()}")
            return r.status_code, r.json()


    def deposit_gold_to_bank(self, amount=None):
        deposit_gold_api = f"{self.server}/my/{self.name}/action/bank/deposit/gold"
        if amount is None: #deposit all
            status, response = self.fetch_character_status()
            if status == 200:
                self.gold = response["gold"]
                if self.gold > 0:
                    body = "{" + f"\"quantity\": {self.gold}"  + "}"
                    r = requests.post(deposit_gold_api, data=body, headers=self.auth_header)
                    print(f"deposit_gold_to_bank | {r.status_code}")
                    if r.status_code == 200:
                        response = r.json()["data"]
                        self.updateCooldown(response["cooldown"]["remaining_seconds"] + 1)
                        self.waitCooldown()
                        return r.status_code, response
                    else:
                        return r.status_code, r.json()
                else:
                    print(f"deposit_gold_to_bank | no gold to deposit")
        else: 
            body = "{" + f"\"quantity\": {amount}"  + "}"
            r = requests.post(deposit_gold_api, data=body, headers=self.auth_header)
            print(f"deposit_gold_to_bank | {r.status_code}")
            if r.status_code == 200:
                response = r.json()["data"]
                self.updateCooldown(response["cooldown"]["remaining_seconds"] + 1)
                self.waitCooldown()
                return r.status_code, response
            else:
                return r.status_code, r.json()



    def fight(self):
        fight_api = f"{self.server}/my/{self.name}/action/fight"
        r = requests.post(fight_api, headers=self.auth_header)
        print(f"fight() | {r.status_code}")
        if r.status_code == 200:
            response = r.json()["data"]
            self.updateCooldown(response["cooldown"]["remaining_seconds"] + 1)
            self.waitCooldown()
            return r.status_code, response
        elif r.status_code == 499:
                response = r.json()
                cooldown = response["error"]["message"].rstrip(" seconds left.")
                cooldown = cooldown.lstrip("Character in cooldown: ")
                cooldown = int(cooldown.split(".")[0])
                time.sleep(cooldown+1)
                return r.status_code, response
        else:
            return r.status_code, r.json()
        
    def gathering(self):
        gathering_api = f"{self.server}/my/{self.name}/action/gathering"
        r = requests.post(gathering_api, headers=self.auth_header)
        print(f"gathering() | {r.status_code}")
        if r.status_code == 200:
            response = r.json()["data"]
            self.updateCooldown(response["cooldown"]["remaining_seconds"] + 1)
            self.waitCooldown()
            return r.status_code, response
        elif r.status_code == 499:
                response = r.json()
                cooldown = response["error"]["message"].rstrip(" seconds left.")
                cooldown = cooldown.lstrip("Character in cooldown: ")
                cooldown = int(cooldown.split(".")[0])
                time.sleep(cooldown+1)
                return r.status_code, response
        else:
            return r.status_code, r.json()
        
    def move_to_closest_bank(self):
        print("move_to_closest_bank | ")
        self.move(4,1)
        

    def fishing(self):
        fishing_api = f"{self.server}/my/{self.name}/action/fishing"
        r = requests.post(fishing_api, headers=self.auth_header)
        print(f"fishing() | {r.status_code}")
        if r.status_code == 200:
            response = r.json()["data"]
            self.updateCooldown(response["cooldown"]["remaining_seconds"] + 1)
            self.waitCooldown()
            return r.status_code, response
        elif r.status_code == 499:
                response = r.json()
                cooldown = response["error"]["message"].rstrip(" seconds left.")
                cooldown = cooldown.lstrip("Character in cooldown: ")
                cooldown = int(cooldown.split(".")[0])
                time.sleep(cooldown+1)
                return r.status_code, response
        else:
            return r.status_code, r.json()
