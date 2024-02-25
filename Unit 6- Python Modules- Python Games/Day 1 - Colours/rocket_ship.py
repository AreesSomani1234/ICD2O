import sys
import pygame


pygame.init()

screen_width = 400
screen_height = 400

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Rocket Ship")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BROWN = (139, 69, 19)
YELLOW = (255, 255, 0)
BLACK = (0,0,0)
RED = (240,20,3)

while True:
    screen.fill(WHITE)

    #(x, y, width, height)

    pygame.draw.rect(screen, RED, (150, 150, 100, 150))
    pygame.draw.polygon(screen, BLACK, [(150,150), (250,150), (200, 100)])
    pygame.draw.rect(screen, BLUE, (100, 200, 50, 75))
    pygame.draw.rect(screen, BLUE,(250, 200, 50, 75))
    pygame.draw.line(screen, WHITE, (200, 155), (200, 295), 3)

        # Update the display
    pygame.display.flip()
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



