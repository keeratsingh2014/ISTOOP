import pygame, button, player, map, npc, time, random, time, enemy
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
        self.enemy = None
        self.npc = None
        self.menu = "ITEM"
        self.text_index = 0
        self.text_delay = 50
        self.last_update_time = pygame.time.get_ticks()
        self.lines = 0

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
                        self.font.render("   " + self.input + event.unicode, True, "white").get_rect().width <= 325) else ""
                elif event.key == pygame.K_BACKSPACE:
                    self.input = self.input[:-1]
                elif (event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN) and self.input != "" and self.lines == 0:
                    self.control()
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


            for i in range(len(user.inventory["weapon"])):
                self.temp = pygame.image.load(user.inventory["weapon"][i-1]["path"]).convert_alpha()
                self.screen.blit(self.temp, self.location[i-1])
            
            self.shadow = pygame.image.load("images/shadow.png")
            self.shadow.set_alpha(50)


            health = pygame.image.load("images/health.png").convert_alpha()
            health = pygame.transform.scale(health, (52, 52))

            speed = pygame.image.load("images/speed.png").convert_alpha()
            speed = pygame.transform.scale(speed, (52, 52))

            strength = pygame.image.load("images/strength.png").convert_alpha()
            strength = pygame.transform.scale(strength, (52, 52))

            self.screen.blit(health, (643, 495))
            self.screen.blit(speed, (574, 552))
            self.screen.blit(strength, (643, 552))
            
            if user.inventory["potions"]["Health"] == 0:
                self.screen.blit(self.shadow, (643, 495))
            if user.inventory["potions"]["Evasiveness"] == 0:
                self.screen.blit(self.shadow, (574, 552))
            if user.inventory["potions"]["Dmg"] == 0:
                self.screen.blit(self.shadow, (643, 552))
            


        elif self.menu == "STAT":
            pygame.draw.rect(self.screen, (247, 37, 133), pygame.Rect(331, 484, 379, 132)) # menu/bag (STATS BG)

            self.screen.blit(self.Lvl, (348, 516))
            self.screen.blit(self.ATK, (443, 516))
            self.screen.blit(self.XPBAR, (538, 564))
            self.screen.blit(self.HPBAR, (538, 514))
            pygame.draw.rect(self.screen, (217, 217, 217), pygame.Rect(578, 514, (user.player_hp() / user.maxhp())*120, 40)) # menu/bag (STATS HP bar)
            pygame.draw.rect(self.screen, (210, 245, 136), pygame.Rect(578, 564, 120, 40)) # menu/bag (STATS XP bar)

            
        
        self.typing()
        self.display_output()

        if user.map != map.world:
            sprite = pygame.image.load("images/playerSprite.png").convert_alpha()
            sprite = pygame.transform.scale(sprite, (120, 120))
            self.screen.blit(sprite, (user.player_location()[0] + 25 + (self.step - sprite.get_width())/2, user.player_location()[1] + 25 + (self.step - sprite.get_width())/2))
            for i in user.map.enemies:
                if i["stage"] == user.map.stage and i["ref"].stats["HP"] != 0:
                    self.screen.blit(i["sprite"], (i["location"][0] + 25 + (self.step - i["sprite"].get_width())/2, i["location"][1] + 25 + (self.step - i["sprite"].get_width())/2))
            
            for i in user.map.chests:
                if i["stage"] == user.map.stage and i["ref"].display:
                    self.screen.blit(i["sprite"], (i["location"][0] + 25 + (self.step - i["sprite"].get_width())/2, i["location"][1] + 25 + (self.step - i["sprite"].get_width())/2))
            
            for i in user.map.npcs:
                if i["stage"] == user.map.stage and i["sprite"] != None:
                    self.screen.blit(i["sprite"], (i["location"][0] + 25 + (self.step - i["sprite"].get_width())/2, i["location"][1] + 25 + (self.step - i["sprite"].get_width())/2))
        else:
            pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect((user.player_location()[0] + 25 + (self.step - 10)/2, user.player_location()[1] + 25 + (self.step - 10)/2), (10, 10)))

        self.menu_buttons()

        pygame.display.update()

    def typing(self):
        text = self.font.render(f" {self.input}", True, "white")
        rect = text.get_rect()
        rect.topleft = (470, 406)
        self.screen.blit(text, rect)
        
        if (time.time() - startTime) % 1.5 > 0.75:
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(rect.right, rect.top + 6, 2, 24))

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
            self.render_text("What would you like to do?")
            self.render_text("1. Attack")
            self.render_text("2. Potions")

    def control(self):
        self.output.append(f" {self.input}")
        
        if user.state == "roam":
            if len(self.input.split()) > 1 and (self.input.split()[0] == "move"):
                direction = 1 if self.input.split()[1] == "up" or self.input.split()[1] == "down" else 0
                magnitude = self.step if self.input.split()[1] == "down" or self.input.split()[1] == "right" else -self.step
                
                if user.location == [140, 0] and self.input.split()[1] == "up":
                    if user.map.stage < user.map.maxStage:
                        user.map.stage += 1
                        print(user.map.stage)
                        user.location = [140, 280]
                        if isinstance(user.map, map.Village):
                            self.map = pygame.image.load(user.map.sprite[user.map.stage - 1]).convert_alpha()
                            self.map = pygame.transform.scale(self.map, (420, 420))
                    else:
                        self.leave()
                
                elif user.location == [280, 140] and self.input.split()[1] == "right" and user.map.stage < user.map.maxStage and isinstance(user.map, map.Location):
                    user.map.stage += 2
                    print(user.map.stage)
                    user.location = [140, 280]
                    self.map = pygame.image.load(user.map.sprite[user.map.stage - 1]).convert_alpha()
                    self.map = pygame.transform.scale(self.map, (420, 420))

                elif user.location == [140, 280] and self.input.split()[1] == "down" and user.map.stage > 1 and isinstance(user.map, map.Location):
                    user.location = [140, 0] if user.map.stage == 2 else [280, 140]
                    user.map.stage = 1
                    self.map = pygame.image.load(user.map.sprite[user.map.stage - 1]).convert_alpha()
                    self.map = pygame.transform.scale(self.map, (420, 420))
                
                elif not (isinstance(user.map, map.Village) and user.map.stage == 3):
                    if self.input.split()[1] in ["up", "down", "right", "left"]:
                        if not (user.location == [60, 300] and self.input.split()[1] == "up") and not (
                        user.location == [0, 240] and self.input.split()[1] == "right" and enemy.boss1.stats["HP"] != 0) and not (
                        user.location == [360, 240] and self.input.split()[1] == "up" and enemy.boss2.stats["HP"] != 0) and not (
                        user.location == [180, 120] and self.input.split()[1] == "up" and enemy.boss3.stats["HP"] != 0):
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
                    if isinstance(user.map, map.Village):
                        self.map = pygame.image.load(user.map.sprite[user.map.stage - 1]).convert_alpha()
                    else:
                        self.map = pygame.image.load(user.map.sprite).convert_alpha()
                    self.map = pygame.transform.scale(self.map, (420, 420))
                    user.location = [140, 280]
                    self.step = 140
            
            elif self.input == "leave" and user.map != map.world:
                self.leave()

        elif user.state == "combat":
            if self.input == "1" or self.input.lower() == "attack":
                user.state = "attack"
                user.attacks = []
                for i in user.inventory["weapon"][0]["moves"]:
                    if not i["locked"]:
                        user.attacks.append(i)
                
                self.render_text("Choose an attack:")
                for i in range(len(user.attacks)):
                    self.render_text(f"{i+1}. {user.attacks[i]["name"]}")
                
            elif self.input == "2" or self.input.lower() == "potions":
                user.potions = []
                for i in user.inventory["potions"]:
                    if user.inventory["potions"][i] != 0:
                        user.potions.append(i)
                if len(user.potions) > 0:
                    user.state = "potions"
                    self.render_text("Choose a potion:")
                    for i in range(len(user.potions)):
                        self.render_text(f"{i+1}. {user.potions[i]}")
                else:
                    self.render_text("You do not have any potions")

            else:
                self.render_text("That does not seem to be a valid command")
                self.render_text("Enter any key to continue")
                user.state = "invalid cmd"

        elif user.state == "potions":
            if self.input.isnumeric() and 1 <= int(self.input) <= len(user.potions):
                user.use_potion(user.potions[int(self.input)-1])
            
                user.state = "combat"
                self.combat_info()

            else:
                self.render_text("That does not seem to be a valid command")
                self.render_text("Enter any key to continue")
                user.state = "invalid cmd"

        elif user.state == "attack":
            if self.input.isnumeric() and 1 <= int(self.input) <= len(user.attacks):
                user.state = "combat"
                enemyAttack = self.enemy.attack()
                    
                if user.attacks[int(self.input)-1]["speed"] >= enemyAttack["speed"]:
                    self.render_text(f"You used: {user.attacks[int(self.input)-1]["name"]}")
                    self.enemy.handle_attack(user.attacks[int(self.input)-1], user.stats["DMG"])
                    
                    if self.enemy.stats["HP"] != 0:
                        self.render_text(f"{self.enemy.name} used: {enemyAttack["name"]}")
                        user.handle_attack(enemyAttack, self.enemy.stats["DMG"])
                        self.render_text(" ")

                else:
                    self.render_text(f"{self.enemy.name} used: {enemyAttack["name"]}")
                    user.handle_attack(enemyAttack, self.enemy.stats["DMG"])
                    
                    if user.stats["HP"] != 0:
                        self.render_text(f"You used: {user.attacks[int(self.input)-1]["name"]}")
                        self.enemy.handle_attack(user.attacks[int(self.input)-1], user.stats["DMG"])
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

            else:
                self.render_text("That does not seem to be a valid command")
                self.render_text("Enter any key to continue")
                user.state = "invalid cmd"
    
        elif user.state == "talk":
            if self.input.isnumeric() and 1 <= int(self.input) <= len(self.npc.movesInfo if isinstance(self.npc, npc.Teachers) else self.npc.items):
                self.render_text(self.npc.sell(user, int(self.input) - 1))
                print([i["name"] for i in user.inventory["weapon"]])
                print(user.inventory["potions"])
            elif self.input == "talk later":
                self.roam_state()

        elif user.state == "invalid cmd":
            user.state = "talk" if user.map.check_area(user.location.copy(), "npc") != "" else "combat"
            self.combat_info()

        
        self.output.append("")
    
    def roam_state(self):
        user.state = "roam"
        user.stats["HP"] = user.maxHP
        user.evasiveness = 1
        user.stats["DMG"] = user.baseDmg
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
        self.location = [(417, 494), (486, 494), (348, 551), (417, 551), (486, 552)]

        self.BG = pygame.image.load("images/BG.png").convert_alpha()
        self.terminal = pygame.image.load("images/TERMINAL.png").convert_alpha()

        self.Lvl = pygame.image.load("images/LVLbutton.png").convert_alpha()
        self.ATK = pygame.image.load("images/ATKbutton.png").convert_alpha()
        self.HPBAR = pygame.image.load("images/HPbar.png").convert_alpha()
        self.XPBAR = pygame.image.load("images/XPbar.png").convert_alpha()

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
            if self.font.render(f"  {textArray[currentIndex]} {textArray[currentIndex + 1]}", True, (0,0,0)).get_rect().width <= 325:
                textArray[currentIndex] += f" {textArray[currentIndex + 1]}"
                textArray.pop(currentIndex + 1)
            else:
                currentIndex += 1

        for i in textArray:
            self.output.append(i)
        self.lines += len(textArray)

    
    def display_output(self):
        current_time = pygame.time.get_ticks()
        for i in range(14):
            try:
                if i == 13 and self.lines != 0:
                    if current_time - self.last_update_time > self.text_delay:
                        self.last_update_time = current_time
                        self.text_index += 1
                        print(self.text_index)
                    text = self.font.render(f" {self.output[-(14 - i + self.lines)][:self.text_index]}", True, (154, 17, 134) if " " == self.output[-(14 - i + self.lines)][0:1] else (255, 255, 255))
                    if self.text_index == len(self.output[-(14 - i + self.lines)]):
                        self.text_index = 0
                        self.lines -= 1
                else:    
                    text = self.font.render(f" {self.output[-(14 - i + self.lines)]}", True, (154, 17, 134) if " " == self.output[-(14 - i + self.lines)][0:1] else (255, 255, 255))
                rect = text.get_rect()
                rect.topleft = (470, 21 + 27 * i)
                self.screen.blit(text, rect)
            except:
                pass

game = Main("Mygame", 60, (825, 650), 60)
user = player.Player("Bob", [180, 360], {"HP": 250, "DMG": 50}, map.world, 0,0,20,20)
game.run()

