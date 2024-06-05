import pygame, button, player, map, npc, time, random, time
from sys import exit

startTime = time.time()

class Main():
    def __init__(self, title, fps, dimensions, step):
        self.dimensions = dimensions
        self.fps = fps
        self.title = title
        self.step = step
        self.is_running = False
        self.screen = None
        self.clock = None
        self.output = []
        self.input = ""
        self.lastCmd = ""
        self.enemy = None
        self.npc = None
        self.menu = "ITEM"

    def initialise(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.dimensions))
        pygame.display.set_caption(self.title)
        self.clock = pygame.time.Clock()
        self.is_running = True
        self.font = pygame.font.Font("Jersey.ttf", 30)
        map.initialise_all()
        print(map.dungeon1.locations == map.dungeon2.locations)


    def run(self):
        self.initialise()
        self.render()
        
        while self.is_running:
            self.handle_events()
            self.update()
            self.clock.tick(self.fps)

        pygame.quit()
        exit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

            if event.type == pygame.KEYDOWN:
                if len(str(event.unicode)) == 1 and (65 <= ord(event.unicode) <= 90 or 97 <= ord(event.unicode) <= 122 or event.unicode.isnumeric()):
                    self.input += event.unicode if (
                        self.font.render("  " + self.input + event.unicode, True, "white").get_rect().width <= 325) else ""
                elif event.key == pygame.K_BACKSPACE:
                    self.input = self.input[:-1]
                elif (event.key == pygame.K_KP_ENTER) or (event.key == pygame.K_RETURN) and (self.input != ""):
                    self.control()
                    self.lastCmd = self.input
                    self.input = ""
                elif event.key == pygame.K_SPACE:
                    self.input += " " if (self.input != "" and self.input[-1]!= " ") else ""

    def update(self):

        self.screen.fill((99, 12, 168))
        self.screen.blit(self.map, (25, 25)) # map
        self.screen.blit(self.terminal, (470, 25)) # terminal
        pygame.draw.rect(self.screen, (181, 23, 158), pygame.Rect(25, 470, 775, 160)) # menu/bag
        pygame.draw.rect(self.screen, (247, 37, 133), pygame.Rect(39, 484, 132, 132)) # menu/bag (Put player sprite orientation here)
        pygame.draw.rect(self.screen, (247, 37, 133), pygame.Rect(185, 484, 132, 59)) # menu/bag (ITEMS)
        pygame.draw.rect(self.screen, (247, 37, 133), pygame.Rect(185, 557, 132, 59)) # menu/bag (STATS)
        pygame.draw.rect(self.screen, (247, 37, 133), pygame.Rect(724, 484, 59, 59)) # menu/bag (?)
        pygame.draw.rect(self.screen, (247, 37, 133), pygame.Rect(724, 557, 59, 59)) # menu/bag (X)

        if self.menu == "ITEM":
            pygame.draw.rect(self.screen, (247, 37, 133), pygame.Rect(331, 484, 224, 132)) # menu/bag (WEAPONS)
            pygame.draw.rect(self.screen, (224, 35, 122), pygame.Rect(555, 484, 155, 132)) # menu/bag (POTIONS)


            pygame.draw.rect(self.screen, (217, 217, 217), pygame.Rect(348, 494, 52, 52)) # menu/bag (square (deleteable))
            pygame.draw.rect(self.screen, (217, 217, 217), pygame.Rect(417, 494, 52, 52)) # menu/bag (square (deleteable))
            pygame.draw.rect(self.screen, (217, 217, 217), pygame.Rect(486, 494, 52, 52)) # menu/bag (square (deleteable))
            pygame.draw.rect(self.screen, (217, 217, 217), pygame.Rect(574, 494, 52, 52)) # menu/bag (square (deleteable))
            pygame.draw.rect(self.screen, (217, 217, 217), pygame.Rect(643, 494, 52, 52)) # menu/bag (square (deleteable))

            pygame.draw.rect(self.screen, (217, 217, 217), pygame.Rect(348, 551, 52, 52)) # menu/bag (square (deleteable))
            pygame.draw.rect(self.screen, (217, 217, 217), pygame.Rect(417, 551, 52, 52)) # menu/bag (square (deleteable))
            pygame.draw.rect(self.screen, (217, 217, 217), pygame.Rect(486, 551, 52, 52)) # menu/bag (square (deleteable))
            pygame.draw.rect(self.screen, (217, 217, 217), pygame.Rect(574, 551, 52, 52)) # menu/bag (square (deleteable))
            pygame.draw.rect(self.screen, (217, 217, 217), pygame.Rect(643, 551, 52, 52)) # menu/bag (square (deleteable))
        elif self.menu == "STAT":
            pygame.draw.rect(self.screen, (247, 37, 133), pygame.Rect(331, 484, 379, 132)) # menu/bag (STATS)
        
        self.typing()
        self.display_output()

        if user.map != map.world:
            sprite = pygame.image.load("images/playerSprite.png").convert_alpha()
            sprite = pygame.transform.scale(sprite, (120, 120))
            self.screen.blit(sprite, (user.player_location()[0] + 20 + (self.step - sprite.get_width())/2, user.player_location()[1] + 20 + (self.step - sprite.get_width())/2))
            for i in user.map.enemies:
                if i["stage"] == user.map.stage and i["ref"].stats["HP"] != 0:
                    self.screen.blit(i["sprite"], (i["location"][0] + 20 + (self.step - i["sprite"].get_width())/2, i["location"][1] + 20 + (self.step - i["sprite"].get_width())/2))
            
            for i in user.map.chests:
                if i["stage"] == user.map.stage and i["ref"].display:
                    self.screen.blit(i["sprite"], (i["location"][0] + 20 + (self.step - i["sprite"].get_width())/2, i["location"][1] + 20 + (self.step - i["sprite"].get_width())/2))
            
            for i in user.map.npcs:
                if i["stage"] == user.map.stage:
                    self.screen.blit(i["sprite"], (i["location"][0] + 20 + (self.step - i["sprite"].get_width())/2, i["location"][1] + 20 + (self.step - i["sprite"].get_width())/2))
        else:
            pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect((user.player_location()[0] + 20 + (self.step - 10)/2, user.player_location()[1] + 20 + (self.step - 10)/2), (10, 10)))

        self.menu_buttons()

        pygame.display.update()

    def typing(self):
        text = self.font.render(self.input, True, "white")
        rect = text.get_rect()
        rect.topleft =  (470, 406)
        self.screen.blit(text, rect)
        
        if (time.time() - startTime) % 1.5 > 0.75:
            pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(rect.right, rect.top + 2, 2, 24))

    def combat_info(self):
        self.render_text(f"{self.enemy.name}:    {self.enemy.stats["HP"]}/{self.enemy.maxHP} HP    {self.enemy.stats["DMG"]} STR")
        self.render_text(" ")
        self.render_text(f"{user.name}:    {user.stats["HP"]}/{user.maxHP} HP    {user.stats["DMG"]} STR")
        self.render_text(" ")
        if self.enemy.stats["HP"] == 0:
            self.render_text(f"You have successfully defeated {self.enemy.name}")
        elif user.stats["HP"] == 0:
            self.render_text("You have been killed, respawning at nearest checkpoint.")
        else:
            self.render_text("Choose an attack:")
            for i in range(4):
                self.render_text(f"{i+1}. {user.inventory["weapon"][0]["moves"][i]["name"]}")

    def control(self):
        self.output.append(f"  {self.input}")
        
        if user.state == "roam":
            if len(self.input.split()) > 1 and (self.input.split()[0] == "move"):
                direction = 1 if self.input.split()[1] == "up" or self.input.split()[1] == "down" else 0
                magnitude = self.step if self.input.split()[1] == "down" or self.input.split()[1] == "right" else -self.step
                
                if user.location == [140, 0] and self.input.split()[1] == "up":
                    if user.map.stage < user.map.maxStage:
                        user.map.stage += 1
                        print(user.map.stage)
                        user.location = [140, 280]
                    else:
                        self.leave()
                
                else:
                    if self.input.split()[1] in ["up", "down", "right", "left"]:
                        user.player_movement(direction, magnitude)
                        
                        if user.location == [140, 0]:
                            self.render_text(f"You approach a door... move up to {"continue to the next room" if user.map.stage < user.map.maxStage else "leave this area"}")

                    if user.map != map.world and user.map.check_area(user.location.copy(), "enemy") != "" and user.map.check_area(user.location.copy(), "enemy").stats["HP"] != 0:
                        self.enemy = user.map.check_area(user.location.copy(), "enemy")
                        user.state = "combat"
                        self.render_text(f"You have encountered {self.enemy.name}. Get ready to start combat.")
                        self.combat_info()
            
            elif self.input == "open chest" and user.map != map.world and user.map.check_area(user.location.copy(), "chest") != "" and user.map.check_area(user.location.copy(), "chest").display:
                loot = user.map.check_area(user.location.copy(), "chest").loot()
                self.render_text(f"You have found a chest. You received {loot} coins")
                user.givemymoney(loot)
                print(user.coins)

            elif self.input == "interact" and user.map != map.world and user.map.check_area(user.location.copy(), "npc") != "":
                user.state = "talk"
                self.npc = user.map.check_area(user.location.copy(), "npc")
                for i in user.map.check_area(user.location.copy(), "npc").introduction():
                    self.render_text(i)
                self.render_text(f"You have {f"{user.souls} souls" if isinstance(self.npc, npc.Teachers) else f"{user.coins} coins"}, spend wisely...")

            elif self.input == "look" and user.map == map.world:
                self.render_text(map.world.locations[tuple(user.player_location())]["desc"])

            elif self.input == "enter" and user.map == map.world:
                if user.map.locations[tuple(user.player_location())]["map"] != "":
                    user.map = user.map.locations[tuple(user.player_location())]["map"]
                    self.map = pygame.image.load(user.map.sprite).convert_alpha()
                    self.map = pygame.transform.scale(self.map, (420, 420))
                    user.location = [140, 280]
                    self.step = 140
            
            elif self.input == "leave" and user.map != map.world:
                self.leave()

        elif user.state == "combat":
            if self.input.isnumeric() and 1 <= int(self.input) <= 4 and not user.attack(int(self.input) - 1)["locked"]:
                enemyAttack = self.enemy.attack()
                
                if user.attack(int(self.input) - 1)["speed"] >= enemyAttack["speed"]:
                    self.render_text(f"You used: {user.attack(int(self.input) - 1)["name"]}")
                    self.enemy.handle_attack(user.attack(int(self.input) - 1), user.stats["DMG"])
                    
                    if self.enemy.stats["HP"] != 0:
                        self.render_text(f"{self.enemy.name} used: {enemyAttack["name"]}")
                        user.handle_attack(enemyAttack, self.enemy.stats["DMG"])
                        self.render_text(" ")

                else:
                    self.render_text(f"{self.enemy.name} used: {enemyAttack["name"]}")
                    user.handle_attack(enemyAttack, self.enemy.stats["DMG"])
                    
                    if user.stats["HP"] != 0:
                        self.render_text(f"You used: {user.attack(int(self.input) - 1)["name"]}")
                        self.enemy.handle_attack(user.attack(int(self.input) - 1), user.stats["DMG"])
                        self.render_text(" ")

                self.combat_info()

                if self.enemy.stats["HP"] == 0:
                    soulGain = self.enemy.souls if isinstance(self.enemy.souls, int) else random.randint(self.enemy.souls[0], self.enemy.souls[1])
                    user.givemysouls(soulGain)
                    self.render_text(f"You earned {soulGain} souls")
                    self.roam_state()
                elif user.stats["HP"] == 0:
                    self.leave()
                    self.roam_state()

            elif user.attack(int(self.input) - 1)["locked"]:
                self.render_text("That move has not been unlocked yet, for further information about moves, use of the menu below")

            else:
                self.render_text("That does not seem to be a valid command")
    
        elif user.state == "talk":
            if self.input.isnumeric() and 1 <= int(self.input) <= len(self.npc.movesInfo if isinstance(self.npc, npc.Teachers) else self.npc.items):
                self.render_text(self.npc.sell(user, int(self.input) - 1))
            elif self.input == "talk later":
                self.roam_state()


        self.output.append("")
    
    def roam_state(self):
        user.state = "roam"
        user.stats["HP"] = user.maxHP
        self.enemy = None
        self.npc = None

    def leave(self):
        for i in user.map.enemies:
            i["ref"].stats["HP"] = i["ref"].maxHP
        for i in user.map.chests:
            i["ref"].display = True
        user.location = user.map.spawn
        user.map.stage = 1
        user.map = user.map.parent
        self.map = pygame.image.load(user.map.sprite).convert_alpha()
        self.map = pygame.transform.scale(self.map, (420, 420))
        self.step = 60
    
    def render(self):
        self.buttonEXIT = pygame.image.load("images/EXITBUTTON.png").convert_alpha()
        self.buttonHELP = pygame.image.load("images/HELPBUTTON.png").convert_alpha()
        self.buttonSTATS = pygame.image.load("images/STATBUTTON.png").convert_alpha()
        self.buttonITEMS = pygame.image.load("images/ITEMBUTTON.png").convert_alpha()
        self.buttonEXIT = button.Button(724, 557, self.buttonEXIT, 1)
        self.buttonHELP = button.Button(724, 484, self.buttonHELP, 1)
        self.buttonSTATS = button.Button(185, 557, self.buttonSTATS, 1)
        self.buttonITEMS = button.Button(185, 484, self.buttonITEMS, 1)

        self.BG = pygame.image.load("images/BG.png").convert_alpha()
        self.terminal = pygame.image.load("images/TERMINAL.png").convert_alpha()
        self.BG = pygame.transform.scale(self.BG, self.dimensions)
        self.map = pygame.image.load(user.map.sprite).convert_alpha()
        self.map = pygame.transform.scale(self.map, (420, 420))
        self.var1 = True
        self.var2 = False
        self.var3 = False
    
        
    def menu_buttons(self):
        if self.buttonITEMS.draw(self.screen):
            self.menu = "ITEM"
        if self.buttonSTATS.draw(self.screen):
            self.menu = "STAT"
        if self.buttonEXIT.draw(self.screen):
            self.is_running = False
        if self.buttonHELP.draw(self.screen):
            pass
    

    def render_text(self, text):
        textArray = text.split(" ")
        currentIndex = 0
        while currentIndex != len(textArray) - 1:
            if self.font.render(f"{textArray[currentIndex]} {textArray[currentIndex + 1]}", True, (0,0,0)).get_rect().width <= 325:
                textArray[currentIndex] += f" {textArray[currentIndex + 1]}"
                textArray.pop(currentIndex + 1)
            else:
                currentIndex += 1

        for i in textArray:
            self.output.append(i)

    def display_output(self):
        for i in range(18):
            try:
                text = self.font.render(self.output[-(18 - i)], True, (255, 0, 0) if "  " == self.output[-(18 - i)][0:2] else (0,0,0))
                rect = text.get_rect()
                rect.topleft = (470, 30 + 20 * i)
                self.screen.blit(text, rect)
            except:
                pass

game = Main("Mygame", 60, (825, 650), 60)
user = player.Player("Bob", [180, 360], {"HP": 250, "DMG": 50}, map.world, 0,0,20,20)
game.run()

