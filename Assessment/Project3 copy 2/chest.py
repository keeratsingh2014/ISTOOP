import random, pygame

class Chest():
    def __init__(self, sprite, coins):
        self.sprite = sprite
        self.coins = coins
        self.display = True
        
    def loot(self):
        self.display = False
        return random.randint(self.coins[0], self.coins[1])
    
    def clone(self):
        return Chest(self.sprite, self.coins)
    
chest1 = Chest("images/dungeon1chest1.png", (4, 6))
chest2 = Chest("images/dungeon1chest1.png", (20, 30))