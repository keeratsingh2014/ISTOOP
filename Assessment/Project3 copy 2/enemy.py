import random, item

class Enemy():
    def __init__(self, name, sprite, stats, weapon):
        self.name = name
        self.sprite = sprite
        self.stats = stats
        self.weapon = weapon

    def attack(self):
        return self.weapon["moves"][random.randint(0, 3)]
    
    def clone(self):
        return Enemy(self.name, self.sprite, self.stats, self.weapon)

    def handle_attack(self, attack, scaling):
        if random.randint(0, 100) <= attack["accuracy"]:
            self.stats["HP"] -= round((scaling ** 1/2) * (attack["dmg"] * 1/2), 2)