class Player():
    def __init__(self, name, location, stats):
        self.name = name
        self.location = location
        self.stats = stats
        # self.inventory = {}
        self.map = None
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

# jeron shush