import sys
import pygame
import math

pygame.init()

screen_width = 400
screen_height = 400

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Car")


Blue = (0,40,220)
Black = (0,0,0)
Red = (240,20,3)
Light_blue = (204,204,255)

while True:
    screen.fill(Blue)

    #(x, y, width, height)

    pygame.draw.rect(screen,Red,(75,225,250,100)) #base of car
    pygame.draw.rect(screen,Light_blue,(100,250,40,40)) #1st window
    pygame.draw.rect(screen,Light_blue,(250,250,40,40)) #2nd window
    
    pygame.draw.circle(screen,Black,(120,360.5),35) #left wheel
    pygame.draw.circle(screen,Black,(270,360.5),35) #right wheel

    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

