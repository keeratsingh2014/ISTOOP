import pygame
import button
import player
import map
from sys import exit


class Main():
    def __init__(self, title, fps, dimensions):
        self.dimensions = dimensions
        self.fps = fps
        self.title = title
        self.is_running = False
        self.screen = None
        self.clock = None
        self.output = ""
        self.prompt = ""

    def initialise(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.dimensions))
        pygame.display.set_caption(self.title)
        self.clock = pygame.time.Clock()
        self.is_running = True
        self.font = pygame.font.SysFont("alefregular", 20)

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
                print(event.unicode)
                
                if 65 <= ord(event.unicode) <= 90 or 97 <= ord(event.unicode) <= 122:
                    self.prompt += event.unicode
                elif event.key == pygame.K_BACKSPACE:
                    self.prompt = self.prompt[:-1]
                elif (event.key == pygame.K_KP_ENTER) or (event.key == pygame.K_RETURN):
                    self.control()
                    self.prompt = ""
                elif event.key == pygame.K_SPACE:
                    self.prompt += " " if self.prompt[-1]!= " " else ""

    def update(self):
        self.screen.blit(self.BG, (0,0))
        #pygame.draw.rect(self.screen, (181, 23, 158), pygame.Rect(20, 20, 350, 350))
        self.screen.blit(self.map, (20, 20)) # map
        pygame.draw.rect(self.screen, (114, 9, 183), pygame.Rect(20, 390, 715, 140)) # menu/bag
        pygame.draw.rect(self.screen, (181, 23, 158), pygame.Rect(390, 20, 345, 310)) # prompt space
        pygame.draw.rect(self.screen, (247, 37, 133), pygame.Rect(390, 330, 345, 40)) # input box
        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect((user.player_location()[0] + 40, user.player_location()[1] + 40), (10, 10)))
        #self.inventory_buttons()
        self.typing()
        self.render_text(self.output)
        pygame.display.update()

    def typing(self):
        text = self.font.render(self.prompt, True, (0,0,0))
        rect = text.get_rect()
        rect.left, rect.centery =  400, 350 
        self.screen.blit(text, rect)
    
    def control(self):
        if (self.prompt.split()[0] == "move") and (self.prompt.split()[1] == "up"):
            user.player_movement(1, -50)
        if (self.prompt.split()[0] == "move") and (self.prompt.split()[1] == "down"):
            user.player_movement(1, 50)
        if (self.prompt.split()[0] == "move") and (self.prompt.split()[1] == "right"):
            user.player_movement(0, 50)
        if (self.prompt.split()[0] == "move") and (self.prompt.split()[1] == "left"):
            user.player_movement(0, -50)
        if self.prompt == "look":
            self.output = map.world.locations[tuple(user.player_location())]["desc"]
        
        
        self.map = map.world.check(tuple(user.player_location()))
        self.map = "images/mapschematic.png" if self.map == "" else self.map
        self.map = pygame.image.load(self.map).convert_alpha()
        self.map = pygame.transform.scale(self.map, (350, 350))
        
    
    def render(self):
        self.button1 = pygame.image.load("images/JustBg.png").convert_alpha()
        self.button2 = pygame.image.load("Images/JustBg.png").convert_alpha()
        self.button3 = pygame.image.load("images/JustBg.png").convert_alpha()
        self.BG = pygame.image.load("images/BG.png").convert_alpha()
        self.map = pygame.image.load("images/mapschematic.png").convert_alpha()
        self.map = pygame.transform.scale(self.map, (350, 350))
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
            text = self.font.render(i, True, (0,0,0))
            rect = text.get_rect()
            rect.topleft = (400, 30 + 20 * textArray.index(i))
            self.screen.blit(text, rect)
        return textArray

game = Main("Mygame", 60, (755, 550))
user = player.Player("Bob", [150, 300], {"HP":1, "DMG":1}, map.world)
game.run()

