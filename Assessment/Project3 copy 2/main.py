import pygame
import button
import player
import map
from sys import exit


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

    def initialise(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.dimensions))
        pygame.display.set_caption(self.title)
        self.clock = pygame.time.Clock()
        self.is_running = True
        self.font = pygame.font.SysFont("alefregular", 20)
        map.dungeon1.initialise()


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
                if len(str(event.unicode)) == 1 and (65 <= ord(event.unicode) <= 90 or 97 <= ord(event.unicode) <= 122):
                    self.input += event.unicode if (
                        self.font.render("  " + self.input + event.unicode, True, (0,0,0)).get_rect().width <= 325) else ""
                elif event.key == pygame.K_BACKSPACE:
                    self.input = self.input[:-1]
                elif (event.key == pygame.K_KP_ENTER) or (event.key == pygame.K_RETURN):
                    self.control()
                    self.lastCmd = self.input
                    self.input = ""
                elif event.key == pygame.K_SPACE:
                    self.input += " " if self.input[-1]!= " " else ""

    def update(self):
        self.screen.blit(self.BG, (0,0))
        #pygame.draw.rect(self.screen, (181, 23, 158), pygame.Rect(20, 20, 350, 350))
        self.screen.blit(self.map, (20, 20)) # map
        pygame.draw.rect(self.screen, (114, 9, 183), pygame.Rect(20, 460, 785, 140)) # menu/bag
        pygame.draw.rect(self.screen, (181, 23, 158), pygame.Rect(460, 20, 345, 380)) # prompt space
        pygame.draw.rect(self.screen, (247, 37, 133), pygame.Rect(460, 400, 345, 40)) # input box
        sprite = pygame.image.load("images/playerSprite.png").convert_alpha()
        sprite = pygame.transform.scale(sprite, (40, 40))
        self.screen.blit(sprite, (user.player_location()[0] + 20 + (self.step - sprite.get_width())/2, user.player_location()[1] + 20 + (self.step - sprite.get_width())/2))
        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect((user.player_location()[0] + 20 + (self.step - 10)/2, user.player_location()[1] + 20 + (self.step - 10)/2), (10, 10)))
        #pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect((85, 85), (10, 10)))
        #self.inventory_buttons()
        self.typing()
        self.display_output()
        if user.map != map.world:
            for i in user.map.enemies:
                if user.map.enemies[i]["stage"] == user.map.stage:
                    self.screen.blit(user.map.enemies[i]["ref"], (i[0] + 70, i[1] + 70))
                
        pygame.display.update()

    def typing(self):
        text = self.font.render(self.input, True, (0,0,0))
        rect = text.get_rect()
        rect.topleft =  (470, 406)
        self.screen.blit(text, rect)
    
    def control(self):
        self.output.append(f"  {self.input}")

        if (self.input.split()[0] == "move") and (self.input.split()[1] == "up"):
            if user.location != [140, 0]:
                user.player_movement(1, -self.step)
            elif user.location == [140, 0] and user.map.stage < user.map.maxStage:
                user.map.stage += 1
                print(user.map.stage)
                user.location = [140, 280]
        elif (self.input.split()[0] == "move") and (self.input.split()[1] == "down"):
            user.player_movement(1, self.step)
        elif (self.input.split()[0] == "move") and (self.input.split()[1] == "right"):
            user.player_movement(0, self.step)
        elif (self.input.split()[0] == "move") and (self.input.split()[1] == "left"):
            user.player_movement(0, -self.step)
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
            user.location = user.map.spawn
            user.map.stage = 1
            user.map = user.map.parent
            self.map = pygame.image.load(user.map.sprite).convert_alpha()
            self.map = pygame.transform.scale(self.map, (420, 420))
            self.step = 60        

        self.output.append("")
    
    def render(self):
        self.button1 = pygame.image.load("images/JustBg.png").convert_alpha()
        self.button2 = pygame.image.load("Images/JustBg.png").convert_alpha()
        self.button3 = pygame.image.load("images/JustBg.png").convert_alpha()
        self.BG = pygame.image.load("images/BG.png").convert_alpha()
        self.BG = pygame.transform.scale(self.BG, self.dimensions)
        self.map = pygame.image.load(user.map.sprite).convert_alpha()
        self.map = pygame.transform.scale(self.map, (420, 420))
        self.button1 = button.Button(390, 20, self.button1, 1)
        self.button2 = button.Button(505, 20, self.button2, 1)
        self.button3 = button.Button(620, 20, self.button3, 1)
        self.var1 = True
        self.var2 = False
        self.var3 = False
    
    def inventory_buttons(self):
        if self.button1.draw(self.screen, self.var1):
            self.var1 = True
            self.var2 = False
            self.var3 = False
            print("menu1")
        if self.button2.draw(self.screen, self.var2):
            self.var2 = True
            self.var1 = False
            self.var3 = False
            print("menu2")
        if self.button3.draw(self.screen, self.var3):
            self.var3 = True
            self.var1 = False
            self.var2 = False
            print("menu3")

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
                text = self.font.render(self.output[-(18 - i)], True, (255, 0, 0) if "  " in self.output[-(18 - i)] else (0,0,0))
                rect = text.get_rect()
                rect.topleft = (470, 30 + 20 * i)
                self.screen.blit(text, rect)
            except:
                pass

game = Main("Mygame", 60, (825, 620), 60)
user = player.Player("Bob", [180, 360], {"HP": 1, "DMG": 1}, map.world)
game.run()

