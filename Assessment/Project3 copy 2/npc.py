class Npc():
    def __init__(self, sprite, name, items):
        self.name = name
        self.items = items
        self.sprite = sprite
    
    def introduction(self):
        return f"Welcome to my store! I am {self.name}"
    
