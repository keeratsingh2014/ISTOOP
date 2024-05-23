mainWorldLocations = {
    (0, 300): {"name": "", "desc": "aaaaa", "interactables": ""},
    (50, 300): {"name": "", "desc": "", "interactables": ""},
    (100, 300): {"name": "", "desc": "", "interactables": ""},
    (150, 300): {"name": "start", "desc": "Welcome to the beginning", "interactables": ""},
    (200, 300): {"name": "", "desc": "", "interactables": ""},
    (250, 300): {"name": "", "desc": "", "interactables": ""},
    (300, 300): {"name": "", "desc": "", "interactables": ""},

    (0, 250): {"name": "", "desc": "", "interactables": ""},
    (50, 250): {"name": "", "desc": "", "interactables": ""},
    (250, 250): {"name": "", "desc": "", "interactables": ""},
    (300, 250): {"name": "", "desc": "", "interactables": ""},
    
    (0, 200): {"name": "", "desc": "", "interactables": ""},
    (50, 200): {"name": "", "desc": "", "interactables": ""},
    (100, 200): {"name": "", "desc": "", "interactables": ""},
    (300, 200): {"name": "", "desc": "", "interactables": ""},
    
    (100, 150): {"name": "", "desc": "", "interactables": ""},
    (150, 150): {"name": "", "desc": "", "interactables": ""},
    (200, 150): {"name": "", "desc": "", "interactables": ""},
    (250, 150): {"name": "", "desc": "", "interactables": ""},
    (300, 150): {"name": "", "desc": "", "interactables": ""},
    
    (150, 100): {"name": "", "desc": "", "interactables": ""},
    (200, 100): {"name": "", "desc": "", "interactables": ""},
    
    (150, 50): {"name": "", "desc": "", "interactables": ""},
    
    (150, 0): {"name": "", "desc": "", "interactables": ""},

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


world = Map("shsuh", mainWorldLocations)
