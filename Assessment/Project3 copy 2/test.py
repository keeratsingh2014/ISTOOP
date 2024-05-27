import pygame
from sys import exit

pygame.init()

X = 800
Y = 500

screen = pygame.display.set_mode((X, Y))
clock = pygame.time.Clock()
pygame.display.set_caption('Show Text')
font = pygame.font.Font('freesansbold.ttf', 15)

def draw_text(text, font, text_col, xy):
    img = font.render(text, False, text_col)
    screen.blit(img, (xy))




def main_menu():
    lines = [""]
    while True:
        screen.fill("black")


        draw_text(lines[0], font, "white", (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    lines[0] = lines[0][:-1]
                elif event.key == pygame.K_RETURN:
                    lines.insert(0, "")
                    print(lines)
                else:
                    lines[0] += event.unicode
            

            pygame.display.update()
            clock.tick(60)

main_menu()
