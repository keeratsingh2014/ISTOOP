import random, pygame

class Chest():
    def __init__(self, sprite, coins):
        self.sprite = sprite
        self.coins = coins
        self.display = True
        
    def loot(self):
        self.display = False
        return self.coins
    
    def clone(self):
        return Chest(self.sprite, self.coins)
    
chest1 = Chest("images/dungeon1chest1.png", random.randint(4, 6))
chest2 = Chest("images/dungeon1chest1.png", random.randint(20, 30))