import pygame
from sys import exit


class Game():
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
        pygame.draw.rect(self.screen, (114, 9, 183), pygame.Rect(20, 390, 715, 140))
        pygame.draw.rect(self.screen, (181, 23, 158), pygame.Rect(390, 20, 345, 350))
        pygame.draw.rect(self.screen, (247, 37, 133), pygame.Rect(390, 20, 345, 40))
        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect((Player.player_location(player)["x"], Player.player_location(player)["y"]), (50, 50)))

        self.inventory_buttons()
        pygame.display.update()
        self.control()

    def control(self):

        user_input = input("Enter: ")
        if (user_input.split()[0] == "move") and (user_input.split()[1] == "up"):
            Player.player_movement(player, "y", 20)
        if (user_input.split()[0] == "move") and (user_input.split()[1] == "down"):
            Player.player_movement(player, "y", -20)
        if (user_input.split()[0] == "move") and (user_input.split()[1] == "right"):
            Player.player_movement(player, "x", 20)
        if (user_input.split()[0] == "move") and (user_input.split()[1] == "left"):
            Player.player_movement(player, "x", -20)


    
    def render(self):
        self.button1 = pygame.image.load("images/JustBg.png").convert_alpha()
        self.button2 = pygame.image.load("Images/JustBg.png").convert_alpha()
        self.button3 = pygame.image.load("images/JustBg.png").convert_alpha()
        self.BG = pygame.image.load("images/BG.png").convert_alpha()
        self.button1 = Button(390, 20, self.button1, 1)
        self.button2 = Button(505, 20, self.button2, 1)
        self.button3 = Button(620, 20, self.button3, 1)
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

    

    

            


class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface, selected):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.image.set_alpha(180)
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        
        surface.blit(self.image, (self.rect.x, self.rect.y))

        if selected == True:
            self.image.set_alpha(180)
        else:
            self.image.set_alpha(256)

        return action


class Player():
    def __init__(self, name, location, stats):
        self.name = name
        self.location = location
        self.stats = stats
        # self.inventory = {}
        self.sprite = None
        # self.progress = None
    
    def player_movement(self, direction, magnitude):
        self.location[direction] += magnitude
        print(self.location)

    def player_location(self):
        return self.location
    
    def player_stats(self):
        pass

    def player_inventory(self):
        pass

    

game = Game("Mygame", 60, (755, 550))
player = Player("Bob", {"x":0, "y":0}, {"HP":1, "DMG":1})
# Intitalise Game/Player
# Loop until valid
#
game.run()
