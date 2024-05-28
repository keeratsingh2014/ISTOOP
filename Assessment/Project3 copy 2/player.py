
class Player():
    def __init__(self, name, location, stats, map):
        self.name = name
        self.location = location
        self.stats = stats
        self.inventory = {"weapon": [], "strength": [], "accuracy": [], "health": []}
        self.map = map
        self.sprite = None
        # self.progress = None
    
    def player_movement(self, direction, magnitude):
        try:
            self.location[direction] += magnitude
            print(self.location)
            print(self.map.locations[tuple(self.location)])
        except:
            self.location[direction] -= magnitude

    def player_location(self):
        return self.location
    
    def spawn(self, location):
        self.location = location

    def player_stats(self):
        pass

    def player_inventory_add(self, type, item):
        self.inventory[type].insert(0, item)
    



# jeron shush
