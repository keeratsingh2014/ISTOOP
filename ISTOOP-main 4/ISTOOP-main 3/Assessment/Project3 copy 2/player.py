import random, item

class Player():
    def __init__(self, name, location, stats, map, levels, exp, souls, coins):
        self.name = name
        self.location = location
        self.stats = stats
        self.maxHP = stats["HP"]
        self.baseDmg = stats["DMG"]
        self.evasiveness = 1
        self.inventory = {"weapon": [item.weapon[0], item.weapon[1], item.weapon[2], item.weapon[3], item.weapon[4]], "potions": {"Health": 0, "Evasiveness": 0, "Dmg": 1}}
        self.map = map
        self.level = levels
        self.exp = 10
        self.sprite = None
        self.souls = souls
        self.coins = coins
        self.state = "roam"
        # self.progress = None
    
    def player_movement(self, direction, magnitude):
        try:
            self.location[direction] += magnitude
            print(self.location)
            print(self.map.locations[tuple(self.location)])

            try:
                if self.map.locations[tuple(self.location)]["chest"] != []:
                    for i in self.map.locations[tuple(self.location)]["chest"]:
                        if i["stage"] == self.map.stage and i["ref"].display:
                            self.location[direction] -= magnitude
            except:
                pass

            try:
                if self.map.locations[tuple(self.location)]["npc"] != []:
                    for i in self.map.locations[tuple(self.location)]["npc"]:
                        if i["stage"] == self.map.stage:
                            self.location[direction] -= magnitude
            except:
                pass
        except:
            self.location[direction] -= magnitude

    def player_location(self):
        return self.location
    
    def spawn(self, location):
        self.location = location

    def player_stats(self):
        self.stats["HP"] = (self.stats["HP"])(1.1)**self.level
        self.stats["DMG"] = (self.stats["DMG"])(1.1)**self.level

    def player_check_level_up(self):
        if self.exp == 100:
            self.level += 1
            self.exp = 0
    
    def player_hp(self):
        return self.stats["HP"]

    def maxhp(self):
        return self.maxHP



    def player_inventory_add(self, type, item):
        self.inventory[type].insert(0, item)
    
    def givemymoney(self, amount):
        self.coins += amount
    
    def givemysouls(self, amount):
        self.souls += amount

    def handle_attack(self, attack, scaling):
        if random.randint(0, 100)*self.evasiveness <= attack["accuracy"]:
            self.stats["HP"] -= round((scaling ** 1/2) * (attack["dmg"] * 1/10), 2)
            self.stats["HP"] = 0 if self.stats["HP"] < 0 else self.stats["HP"]

    def attack(self, index):
        return self.inventory["weapon"][0]["moves"][index]
    
    def use_potion(self, type):
        self.inventory["potions"][type] -= 1
        if type == "Health":
            self.stats["HP"] += self.maxHP * 0.25
            if self.stats["HP"] > self.maxHP:
                self.stats["HP"] = self.maxHP
        
        if type == "Dmg":
            self.stats["DMG"] += self.baseDmg * 0.1

        if type == "Evasiveness":
            self.evasiveness += 0.1



# jeron shush
