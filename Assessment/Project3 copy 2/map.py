mainWorldPoints = {
    (0, 360): {"name": "", "desc": "aaaaa", "interactables": "", "map": ""},
    (60, 360): {"name": "", "desc": "", "interactables": "", "map": ""},
    (120, 360): {"name": "", "desc": "", "interactables": "", "map": ""},
    (180, 360): {"name": "start", "desc": "Welcome to the beginning", "interactables": "", "map": ""},
    (240, 360): {"name": "", "desc": "aaaaaaaaaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaaaaaaa", "interactables": "", "map": ""},
    (300, 360): {"name": "", "desc": "", "interactables": "", "map": ""},
    (360, 360): {"name": "", "desc": "", "interactables": "", "map": ""},

    (0, 300): {"name": "", "desc": "", "interactables": "", "map": ""},
    (60, 300): {"name": "", "desc": "", "interactables": "", "map": ""},
    (300, 300): {"name": "", "desc": "", "interactables": "", "map": ""},
    (360, 300): {"name": "", "desc": "", "interactables": "", "map": ""},
    
    (0, 240): {"name": "", "desc": "", "interactables": "", "map": ""},
    (60, 240): {"name": "", "desc": "", "interactables": "", "map": ""},
    (120, 240): {"name": "", "desc": "", "interactables": "", "map": ""},
    (360, 240): {"name": "", "desc": "", "interactables": "", "map": ""},
    
    (120, 180): {"name": "", "desc": "", "interactables": "", "map": ""},
    (180, 180): {"name": "", "desc": "", "interactables": "", "map": ""},
    (240, 180): {"name": "", "desc": "", "interactables": "", "map": ""},
    (300, 180): {"name": "", "desc": "", "interactables": "", "map": ""},
    (360, 180): {"name": "", "desc": "", "interactables": "", "map": ""},
    
    (180, 120): {"name": "", "desc": "", "interactables": "", "map": ""},
    (240, 120): {"name": "", "desc": "", "interactables": "", "map": ""},
    
    (180, 60): {"name": "", "desc": "", "interactables": "", "map": ""},
    
    (180, 0): {"name": "", "desc": "", "interactables": "", "map": ""},
}

locationPoints = {
    (0, 280): {"enemy": "", "chest": ""},
    (140, 280): {"enemy": "", "chest": ""},
    (280, 280): {"enemy": "", "chest": ""},

    (0, 140): {"enemy": "", "chest": ""},
    (140, 140): {"enemy": "", "chest": ""},
    (280, 140): {"enemy": "", "chest": ""},
    
    (0, 0): {"enemy": "", "chest": ""},
    (140, 0): {"enemy": "", "chest": ""},
    (280, 0): {"enemy": "", "chest": ""}
}

class Map():
    def __init__(self, sprite, locations):
        self.sprite = sprite
        self.locations = locations
    
    def location(self, location):
        try:
            mainWorldPoints[location]
            return mainWorldPoints[location]
        except:
            return False

        
    def check(self, location):
        return mainWorldPoints[location]["map"]

class Location(Map):
    def __init__(self, sprite, stage, maxStage, spawn, enemies, chests, parent, locations = locationPoints.copy()):
        super().__init__(sprite, locations)
        self.stage = stage
        self.maxStage = maxStage
        self.spawn = spawn
        self.enemies = enemies
        self.chests = chests
        self.parent = parent
    
    def initialise(self):
        for i in self.enemies:
            self.locations[i]["enemy"] = self.enemies[i]

        for i in self.chests:
            self.locations[i]["chest"] = self.chests[i]

        self.parent.locations[tuple(self.spawn)]["map"] = self

world = Map("images/mapschematic.png", mainWorldPoints)
dungeon1 = Location("images/location.png", 1, 5, [0, 360], {(0, 0): {"stage": 1, "ref": "enemy1"}}, {(140, 0): {"stage": 1, "ref": "chest1"}}, world)
