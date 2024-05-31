class Npc():
    def __init__(self, sprite, name, items):
        self.name = name
        self.items = items
        self.sprite = sprite
    
    def introduction(self):
        return f"Welcome to my store! I am {self.name}"

class Teachers(Npc):
    def __init__(self, sprite, name, items):
        super().__init__(sprite, name, items)
    
    def sell(self, weapon):
        pass

class Shopkeepers(Npc):
    def __init__(self, sprite, name, items):
        super().__init__(sprite, name, items)
    
    def sell(self):
        pass
# there are two types of npcs: Teachers and shopkeers,
# recall that teachers exchange soul currency (given by defeating enemies) for moves and shoopkeepers exchange coins for weapons and items
# Each shopkeeper can sell an infinite amt of potions and a one time weapon
# Teachers teach 3 moves to a specific weapon 
# Npc interactions are not automatic, the terminal prompts the user to interact withn them.