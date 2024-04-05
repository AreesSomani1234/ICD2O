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
WHITE = (255,255,255)
x = ((SCREEN_WIDTH / 2) - 12.5)
y = ((SCREEN_HEIGHT / 2) - 12.5)
velocity = 3

clock = pygame.time.Clock()

while True:
    screen.fill(WHITE) 
    clock.tick(60)
# (x, y, width, height)


    y += velocity
    if y >= SCREEN_HEIGHT - 75 or y <= 0:
        velocity *= -1


    pygame.draw.rect(screen, RED, (x , y, 25, 75)) #pole


    # Update the display
    pygame.display.flip()
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()