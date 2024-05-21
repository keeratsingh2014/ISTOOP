mainWorldLocations = [
    {"place": "shush", "point": (10,10), "desc": "shushhh", "interactables": []},
    {"place": "bob", "point": (), "desc": "", "interactables": []},
    {"place": "bob", "point": (), "desc": "", "interactables": []},
    {"place": "bob", "point": (), "desc": "", "interactables": []},
    {"place": "bob", "point": (), "desc": "", "interactables": []},
    {"place": "bob", "point": (), "desc": "", "interactables": []},
    {"place": "bob", "point": (), "desc": "", "interactables": []},
    {"place": "bob", "point": (), "desc": "", "interactables": []},
    {"place": "bob", "point": (), "desc": "", "interactables": []},
    {"place": "bob", "point": (), "desc": "", "interactables": []},
    {"place": "bob", "point": (), "desc": "", "interactables": []},
    {"place": "bob", "point": (), "desc": "", "interactables": []},
    {"place": "bob", "point": (), "desc": "", "interactables": []},
    {"place": "bob", "point": (), "desc": "", "interactables": []},
    {"place": "bob", "point": (), "desc": "", "interactables": []},
    {"place": "bob", "point": (), "desc": "", "interactables": []},
    {"place": "bob", "point": (), "desc": "", "interactables": []},
    {"place": "bob", "point": (), "desc": "", "interactables": []},
    {"place": "bob", "point": (), "desc": "", "interactables": []},
    {"place": "bob", "point": (), "desc": "", "interactables": []},
    {"place": "bob", "point": (), "desc": "", "interactables": []},
    {"place": "bob", "point": (), "desc": "", "interactables": []},
    {"place": "bob", "point": (), "desc": "", "interactables": []},
    {"place": "bob", "point": (), "desc": "", "interactables": []},
]


class Map():
    def __init__(self, sprite, locations):
        self.sprite = sprite
        self.locations = locations
    
    def location(self, location):
        if location in [i["point"] for i in self.locations]:
            return "good job or smthn"
        else:
            return "screw you"

world = Map("shsuh", mainWorldLocations)
