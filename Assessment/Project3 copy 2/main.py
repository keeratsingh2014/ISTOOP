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

    def initialise(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.dimensions))
        pygame.display.set_caption(self.title)
        self.clock = pygame.time.Clock()
        self.is_running = True

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

    def update(self):
        self.screen.blit(self.BG, (0,0))
        pygame.draw.rect(self.screen, (181, 23, 158), pygame.Rect(20, 20, 350, 350))
        self.screen.blit(self.map, (20, 20))
        pygame.draw.rect(self.screen, (114, 9, 183), pygame.Rect(20, 390, 715, 140))
        pygame.draw.rect(self.screen, (181, 23, 158), pygame.Rect(390, 20, 345, 350))
        pygame.draw.rect(self.screen, (247, 37, 133), pygame.Rect(390, 20, 345, 40))
        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect((user.player_location()[0] + 40, user.player_location()[1] + 40), (10, 10)))
        self.inventory_buttons()
        pygame.display.update()
        self.control()

    def control(self):

        user_input = input("Enter: ")
        if (user_input.split()[0] == "move") and (user_input.split()[1] == "up"):
            user.player_movement(1, -50)
        if (user_input.split()[0] == "move") and (user_input.split()[1] == "down"):
            user.player_movement(1, 50)
        if (user_input.split()[0] == "move") and (user_input.split()[1] == "right"):
            user.player_movement(0, 50)
        if (user_input.split()[0] == "move") and (user_input.split()[1] == "left"):
            user.player_movement(0, -50)
        if user_input == "look":
            map.world.locations(user.player_location())
        


    
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

    
game = Main("Mygame", 60, (755, 550))
user = player.Player("Bob", [0, 0], {"HP":1, "DMG":1})
game.run()

