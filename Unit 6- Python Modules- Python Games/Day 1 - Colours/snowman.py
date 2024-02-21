import sys
import pygame
import math
pygame.init()

screen_width = 400
screen_height = 400

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snowman")


white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,163,240)

while True:
    screen.fill(blue)

    #Body of snowman (cirlces)
    pygame.draw.circle(screen, white, (200,340), 60)
    pygame.draw.circle(screen, white, (200,250), 50)
    pygame.draw.circle(screen, white,(200,170), 40)

    #Eyes and buttons (circles)
    pygame.draw.circle(screen, black,(200,325), 10)
    pygame.draw.circle(screen, black,(200,275), 10)
    pygame.draw.circle(screen, black,(200,240), 10)

    pygame.draw.circle(screen, red,(190,160), 5)
    pygame.draw.circle(screen, red,(210,160), 5)

    #Mouth
    pygame.draw.line(screen, red, (180,180),(220,180), 2)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
