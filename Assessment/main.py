import pygame
import button, game
from sys import exit


class Mob():
    pass


class Player():
    def __init__(self, name, location, stats):
        self.name = name
        self.location = location
        self.stats = stats
        # self.inventory = {}
        self.sprite = None
        # self.progress = None
    
    def player_movement(self, direction, magnitude):
        self.location[direction] += magnitude
        print(self.location)

    def player_location(self):
        return self.location
    
    def player_stats(self):
        pass

    def player_inventory(self):
        pass

    
class Enemy():
    pass


class Item():
    pass

class Consumable():
    pass

class Equipment():
    pass

class Map():
    pass


class Progress():
    pass


game = Game("Mygame", 60, (755, 550))
player = Player("Bob", {"x":0, "y":0}, {"HP":1, "DMG":1})
# Intitalise Game/Player
# Loop until valid
#
game.run()