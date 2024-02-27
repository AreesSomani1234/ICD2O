import sys
import pygame
import math
pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("City")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BROWN = (139, 69, 19)
YELLOW = (255, 255, 0)
BLACK = (0,0,0)
RED = (240,20,3)
LIGHT_BLUE = (204,204,255)
DARK_BLUE = (0,0,153)
GRAY = (96,96,96)
ORANGE = (255,153,51)
GREEN = (0,200,8)

while True:
    screen.fill(LIGHT_BLUE)
    # (x, y, width, height)
    #small building
    pygame.draw.rect(screen, GRAY, (0,300,75,300))
    pygame.draw.polygon(screen, GRAY,[(0,300),(75,300),(37.5,200)])
    pygame.draw.rect(screen, BLACK, (25,325,25,25))
    pygame.draw.rect(screen, BLACK, (25,375,25,25))
    pygame.draw.rect(screen, BLACK, (25,425,25,25))

    #big building
    pygame.draw.rect(screen, GRAY, (200,250,125,250))
    pygame.draw.ellipse(screen, GRAY, (200,150,125,250))
    pygame.draw.line(screen, RED, (262.5,150),(262.5,50),3)
    pygame.draw.rect(screen, DARK_BLUE, (218.5,250,25,75))
    pygame.draw.rect(screen, DARK_BLUE, (218.5,350,25,75))
    pygame.draw.rect(screen, DARK_BLUE, (280,250,25,75))
    pygame.draw.rect(screen, DARK_BLUE, (280,350,25,75))


    #Sun
    pygame.draw.circle(screen, YELLOW, (100,50), 50)

    #plane
    pygame.draw.ellipse(screen, WHITE, (350,60,100,40))
    pygame.draw.polygon(screen, BROWN, [(390,60),(410,60),(400,30)])
    pygame.draw.polygon(screen, BROWN, [(390,100),(410,100),(400,130)])
    pygame.draw.circle(screen,LIGHT_BLUE,(400,80),5)
    pygame.draw.circle(screen,LIGHT_BLUE,(385,80),5)
    pygame.draw.circle(screen,LIGHT_BLUE,(415,80),5)
    pygame.draw.circle(screen,LIGHT_BLUE,(430,80),5)
    pygame.draw.circle(screen,LIGHT_BLUE,(370,70),9)


    #flag
    pygame.draw.rect(screen, BLACK, (400, 350, 15, 150)) #pole
    pygame.draw.rect(screen, RED, (415, 350, 50, 50))  #flag
    pygame.draw.polygon(screen, GREEN, [(440,355),(430,390),(450,390)])


    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


