import random

class Enemy():
    def __init__(self, name, sprite, stats, souls, exp, moveset):
        self.name = name
        self.sprite = sprite
        self.stats = stats
        self.moveset = moveset
        self.souls = souls
        self.exp = exp
        self.maxHP = stats["HP"]

    def attack(self):
        return self.moveset[random.randint(0, len(self.moveset) - 1)]
    
    def clone(self):
        return Enemy(self.name, self.sprite, self.stats, self.souls, self.exp, self.moveset)

    def handle_attack(self, attack, scaling):
        if random.randint(0, 100) <= attack["accuracy"]:
            self.stats["HP"] -= round((scaling ** 1/2) * (attack["dmg"] * 1/10), 2)
            self.stats["HP"] = 0 if self.stats["HP"] < 0 else self.stats["HP"]

enemy1 = Enemy("CodeReaper", "images/dungeon1enemy1.png", {"HP": 200, "DMG": 40}, 1, (),
            [{"name": "shsuh", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": False}, 
            {"name": "megashsuh", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True}, 
            {"name": "moh", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True}, 
            {"name": "ant", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True}])

enemy2 = Enemy("CodeReaper", "images/dungeon1enemy2.png", {"HP": 300, "DMG": 55}, (3, 4), (),
            [{"name": "shsuh", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": False}, 
            {"name": "megashsuh", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True}, 
            {"name": "moh", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True}, 
            {"name": "ant", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True}])

enemy3 = Enemy("CodeReaper", "images/dungeon1enemy3.png", {"HP": 350, "DMG": 65}, (10, 12), (),
            [{"name": "shsuh", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": False}, 
            {"name": "megashsuh", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True}, 
            {"name": "moh", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True}, 
            {"name": "ant", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True}])

enemy4 = Enemy("NanoStalker", "images/dungeon2enemy1.png", {"HP": 200, "DMG": 40}, 1, (),
            [{"name": "shsuh", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": False}, 
            {"name": "megashsuh", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True}, 
            {"name": "moh", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True}, 
            {"name": "ant", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True}])

enemy5 = Enemy("NanoStalker", "images/dungeon2enemy2.png", {"HP": 300, "DMG": 55}, (3, 4), (),
            [{"name": "shsuh", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": False}, 
            {"name": "megashsuh", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True}, 
            {"name": "moh", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True}, 
            {"name": "ant", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True}])

enemy6 = Enemy("NanoStalker", "images/dungeon2enemy3.png", {"HP": 350, "DMG": 65}, (10, 12), (),
            [{"name": "shsuh", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": False}, 
            {"name": "megashsuh", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True}, 
            {"name": "moh", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True}, 
            {"name": "ant", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True}])

enemy7 = Enemy("DataMage", "images/dungeon3enemy1.png", {"HP": 200, "DMG": 40}, 1, (),
            [{"name": "shsuh", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": False}, 
            {"name": "megashsuh", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True}, 
            {"name": "moh", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True}, 
            {"name": "ant", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True}])

enemy8 = Enemy("DataMage", "images/dungeon3enemy2.png", {"HP": 300, "DMG": 55}, (3, 4), (),
            [{"name": "shsuh", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": False}, 
            {"name": "megashsuh", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True}, 
            {"name": "moh", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True}, 
            {"name": "ant", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True}])

enemy9 = Enemy("DataMage", "images/dungeon3enemy3.png", {"HP": 350, "DMG": 65}, (10, 12), (),
            [{"name": "shsuh", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": False}, 
            {"name": "megashsuh", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True}, 
            {"name": "moh", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True}, 
            {"name": "ant", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True}])


boss1 = Enemy("CodeReaper", "images/Boss1.png", {"HP": 500, "DMG": 85}, (18, 23), (),
            [{"name": "shsuh", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": False}, 
            {"name": "megashsuh", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True}, 
            {"name": "moh", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True}, 
            {"name": "ant", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True}])

boss2 = Enemy("NanoStalker", "images/Boss2.png", {"HP": 500, "DMG": 85}, (18, 23), (),
            [{"name": "shsuh", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": False}, 
            {"name": "megashsuh", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True}, 
            {"name": "moh", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True}, 
            {"name": "ant", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True}])

boss3 = Enemy("DataMage", "images/Boss3.png", {"HP": 500, "DMG": 85}, (18, 23), (),
            [{"name": "shsuh", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": False}, 
            {"name": "megashsuh", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True}, 
            {"name": "moh", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True}, 
            {"name": "ant", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True}])