
weapon = [
    {
        "name": "stick", 
        "moves":    [
            {"name": "shsuh", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 4, "locked": False}, 
            {"name": "megashsuh", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True}, 
            {"name": "moh", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True}, 
            {"name": "ant", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True}
        ]
    }, 

    {
        "name": "cangelate", 
        "moves":    [
            {"name": "earfquake", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True}, 
            {"name": "newmagicwand", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True}, 
            {"name": "keeratgun", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True}, 
            {"name": "9/11", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True}
        ]
    },     

    {
        "name": "", 
        "moves":    [
            {"name": "shsuh", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True}, 
            {"name": "megashsuh", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True}, 
            {"name": "moh", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True}, 
            {"name": "ant", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True}
        ]
    }, 

    {
        "name": "", 
        "moves":    [
            {"name": "shsuh", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True}, 
            {"name": "megashsuh", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True}, 
            {"name": "moh", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True}, 
            {"name": "ant", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True}
        ]
    }, 

    {
        "name": "", 
        "moves":    [
            {"name": "shsuh", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True}, 
            {"name": "megashsuh", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True}, 
            {"name": "moh", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True}, 
            {"name": "ant", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True}
        ]
    }, 

    {
        "name": "", 
        "moves":    [
            {"name": "shsuh", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "locked": True}, 
            {"name": "megashsuh", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "locked": True}, 
            {"name": "moh", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "locked": True}, 
            {"name": "ant", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "locked": True}
        ]
    }, 
]
        
potion = [
    {
        "type": "Health",
    },

    {
        "type": "Accuracy",
    },

    {
        "type": "Dmg",
    },


]


class Item():
    def __init__(self):
        pass

    def get_weapon(self, name, spec):
        return weapon[name][spec]
        

    def get_potion(self, type):
        return potion[type]
