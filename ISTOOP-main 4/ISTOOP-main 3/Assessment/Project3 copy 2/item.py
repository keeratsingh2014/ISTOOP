
weapon = [
    {
        "name": "bandar", 
        "path": "images/EXITBUTTON.png",
        "moves":    [
            {"name": "shsuh", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": False, "learnCost": 2}, 
            {"name": "megashsuh", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": False, "learnCost": 4}, 
            {"name": "moh", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": False, "learnCost": 6}, 
            {"name": "ant", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": False, "learnCost": 8}
        ]
    }, 

    {
        "name": "sword", 
        "path": "images/Sword.png",
        "moves":    [
            {"name": "shsuh", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 4, "locked": False, "learnCost": 2}, 
            {"name": "megashsuh", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True, "learnCost": 4}, 
            {"name": "moh", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True, "learnCost": 6}, 
            {"name": "ant", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True, "learnCost": 8}
        ],
        "cost": 20
    }, 

    {
        "name": "hammer", 
        "path": "images/Hammer.png",
        "moves":    [
            {"name": "earfquake", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True, "learnCost": 2}, 
            {"name": "newmagicwand", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True, "learnCost": 4}, 
            {"name": "keeratgun", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True, "learnCost": 6}, 
            {"name": "9/11", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True, "learnCost": 8}
        ],
        "cost": 20
    },     

    {
        "name": "axe", 
        "path": "images/Axe.png",
        "moves":    [
            {"name": "shsuh", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True, "learnCost": 2}, 
            {"name": "megashsuh", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True, "learnCost": 4}, 
            {"name": "moh", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True, "learnCost": 6}, 
            {"name": "ant", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True, "learnCost": 8}
        ],
        "cost": 20
    }, 

    {
        "name": "chotu", 
        "path": "images/EXITBUTTON.png",
        "moves":    [
            {"name": "shsuh", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True}, 
            {"name": "megashsuh", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True}, 
            {"name": "moh", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True}, 
            {"name": "ant", "dmg": 50, "accuracy": 99, "maxpp": 5, "pp": 5, "speed": 5, "locked": True}
        ]
    }, 

    {
        "name": "joddji", 
        "path": "images/EXITBUTTON.png",
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
        "name": "potion",
        "type": "Health",
        "cost": 5
    },

    {
        "name": "potion",
        "type": "Evasiveness",
        "cost": 5
    },

    {
        "name": "potion",
        "type": "Dmg",
        "cost": 5
    },


]


def get_weapon(name, spec):
    return weapon[name][spec]

def blitweapon(index):
    return weapon[index]["path"]
    
def blitpotion(index):
    return weapon[index]["path"]
    
def get_potion(type):
    return potion[type]
