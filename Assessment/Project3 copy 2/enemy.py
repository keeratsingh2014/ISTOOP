import random

class Enemy():
    def __init__(self, name, sprite, stats, moveset):
        self.name = name
        self.sprite = sprite
        self.stats = stats
        self.moveset = moveset
        self.maxHP = stats["HP"]

    def attack(self):
        return self.moveset[random.randint(0, len(self.moveset) - 1)]
    
    def clone(self):
        return Enemy(self.name, self.sprite, self.stats, self.moveset)

    def handle_attack(self, attack, scaling):
        if random.randint(0, 100) <= attack["accuracy"]:
            self.stats["HP"] -= round((scaling ** 1/2) * (attack["dmg"] * 1/10), 2)
            self.stats["HP"] = 0 if self.stats["HP"] < 0 else self.stats["HP"]

sampleEnemy = Enemy("Bob", "images\playerSprite.png", {"HP": 200, "DMG": 40},
            [{"name": "shsuh", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": False}, 
            {"name": "megashsuh", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True}, 
            {"name": "moh", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True}, 
            {"name": "ant", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True}])