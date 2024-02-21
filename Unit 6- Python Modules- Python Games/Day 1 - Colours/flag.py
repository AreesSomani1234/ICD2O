import sys
import pygame


pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flag")


GRAY = (96,96,96)
RED = (200,0,0)
BLUE = (10, 4, 150)
GREEN = (0,200,8)

while True:
    screen.fill(BLUE) 

# (x, y, width, height)
    
    pygame.draw.rect(screen, GRAY, (100, 150, 15, 400)) #pole
    pygame.draw.rect(screen, RED, (115, 150, 100, 75))  #flag

    pygame.draw.polygon(screen, GREEN, [(145,200),(165,180),(185,200)])

    # Update the display
    pygame.display.flip()
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()