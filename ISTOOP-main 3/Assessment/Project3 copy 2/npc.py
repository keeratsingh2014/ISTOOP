import item

class Npc():
    def __init__(self, sprite, name, items):
        self.name = name
        self.items = items
        self.sprite = sprite
    
    def introduction(self):
        return f"Welcome to my store! I am {self.name}."

class Teachers(Npc):
    def __init__(self, sprite, name, items):
        super().__init__(sprite, name, items)
    
    def introduction(self):
        self.movesInfo = []
        for i in self.items["moves"]:
            if i["locked"]:
                self.movesInfo.append(i)
        returnValue = [f"{super().introduction()} {f"You can learn {self.items["name"].capitalize()}'s moves from here, select a move to learn:" if self.movesInfo != [] else ""}"]
        for i in self.movesInfo:
            returnValue.append(f"{self.movesInfo.index(i) + 1}. {i["name"].upper()} for {i["learnCost"]} souls")
        return returnValue
    
    def sell(self, player, index):
        if player.souls >= self.movesInfo[index]["learnCost"] and self.movesInfo[index]["locked"]:
            player.givemysouls(-self.movesInfo[index]["learnCost"])
            self.movesInfo[index]["locked"] = False
            return f"You have successfully learnt {self.movesInfo[index]["name"].upper()}"
        elif not self.movesInfo[index]["locked"]:
            return f"You have successfully learnt {self.movesInfo[index]["name"].upper()}"        
        else:
            return f"You do not have enough souls to learn {self.movesInfo[index]["name"].upper()}"

class Shopkeepers(Npc):
    def __init__(self, sprite, name, items):
        super().__init__(sprite, name, items)
    
    def introduction(self):
        returnValue = [f"{super().introduction()} You can buy:"]
        for i in self.items:
            returnValue.append(f"{self.items.index(i) + 1}. {i["name"].upper()} for {i["cost"]} coins")
        return returnValue
    
    def sell(self, player, index):
        if player.coins >= self.items[index]["cost"]:
            player.givemymoney(-self.items[index]["cost"])
            returnValue = f"You have successfully purchased {self.items[index]["name"].upper()}"
            if self.items[index] in item.weapon:
                self.items.pop(index)
            return returnValue
        else:
            return f"You do not have enough coins to purchase {self.items[index]["name"].upper()}"

teacher1 = Teachers("images\playerSprite.png", "Steve", item.weapon[1])
shop1 = Shopkeepers("images\dungeon3enemy3.png", "John", [item.weapon[1]])

# there are two types of npcs: Teachers and shopkeers,
# recall that teachers exchange soul currency (given by defeating enemies) for moves and shoopkeepers exchange coins for weapons and items
# Each shopkeeper can sell an infinite amt of potions and a one time weapon
# Teachers teach 3 moves to a specific weapon 
# Npc interactions are not automatic, the terminal prompts the user to interact withn them.