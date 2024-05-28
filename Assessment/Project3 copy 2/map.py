mainWorldLocations = {
    (0, 360): {"name": "", "desc": "aaaaa", "interactables": "", "map": "images/location.png"},
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
        return mainWorldLocations[location]["map"]


world = Map("shsuh", mainWorldLocations)
