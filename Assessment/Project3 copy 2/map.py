mainWorldLocations = {
    (0, 300): {"name": "", "desc": "aaaaa", "interactables": "", "map": "images/locationschematic.png"},
    (50, 300): {"name": "", "desc": "", "interactables": "", "map": ""},
    (100, 300): {"name": "", "desc": "", "interactables": "", "map": ""},
    (150, 300): {"name": "start", "desc": "Welcome to the beginning", "interactables": "", "map": ""},
    (200, 300): {"name": "", "desc": "", "interactables": "", "map": ""},
    (200, 300): {"name": "", "desc": "", "interactables": "", "map": ""},
    (250, 300): {"name": "", "desc": "", "interactables": "", "map": ""},
    (300, 300): {"name": "", "desc": "", "interactables": "", "map": ""},

    (0, 250): {"name": "", "desc": "", "interactables": "", "map": ""},
    (50, 250): {"name": "", "desc": "", "interactables": "", "map": ""},
    (250, 250): {"name": "", "desc": "", "interactables": "", "map": ""},
    (300, 250): {"name": "", "desc": "", "interactables": "", "map": ""},
    
    (0, 200): {"name": "", "desc": "", "interactables": "", "map": ""},
    (50, 200): {"name": "", "desc": "", "interactables": "", "map": ""},
    (100, 200): {"name": "", "desc": "", "interactables": "", "map": ""},
    (300, 200): {"name": "", "desc": "", "interactables": "", "map": ""},
    
    (100, 150): {"name": "", "desc": "", "interactables": "", "map": ""},
    (150, 150): {"name": "", "desc": "", "interactables": "", "map": ""},
    (200, 150): {"name": "", "desc": "", "interactables": "", "map": ""},
    (250, 150): {"name": "", "desc": "", "interactables": "", "map": ""},
    (300, 150): {"name": "", "desc": "", "interactables": "", "map": ""},
    
    (150, 100): {"name": "", "desc": "", "interactables": "", "map": ""},
    (200, 100): {"name": "", "desc": "", "interactables": "", "map": ""},
    
    (150, 50): {"name": "", "desc": "", "interactables": "", "map": ""},
    
    (150, 0): {"name": "", "desc": "", "interactables": "", "map": ""},

}

class Map():
    def __init__(self, sprite, locations):
        self.sprite = sprite
        self.locations = locations
    
    def location(self, location):
        try:
            mainWorldLocations[location]
            return mainWorldLocations[location]
        except:
            return False
    
    def check(self, location):
        if location in mainWorldLocations:
            return mainWorldLocations[location]["map"]


world = Map("shsuh", mainWorldLocations)
