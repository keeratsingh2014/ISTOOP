mainWorldLocations = {
    (0,0): {"name": "", "desc": "", "interactables": ""},
    (0,0): {"name": "", "desc": "", "interactables": ""},
    (0,0): {"name": "", "desc": "", "interactables": ""},
    (0,0): {"name": "", "desc": "", "interactables": ""},
    (0,0): {"name": "", "desc": "", "interactables": ""},
    (0,0): {"name": "", "desc": "", "interactables": ""},
    (0,0): {"name": "", "desc": "", "interactables": ""},
    (0,0): {"name": "", "desc": "", "interactables": ""},
    (0,0): {"name": "", "desc": "", "interactables": ""},
    (0,0): {"name": "", "desc": "", "interactables": ""},
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
            pass


world = Map("shsuh", mainWorldLocations)
