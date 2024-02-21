import sys
import pygame

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sun")

#Colours
yellow = (255,255,0)
blue = (0,0,200)


while True:
    screen.fill(blue)  # Fill the screen with white color
    
    # Draw the face (circle)
    pygame.draw.circle(screen, yellow, (SCREEN_WIDTH / 2 , SCREEN_HEIGHT / 2 ), 150)

    #Suns rays
    pygame.draw.line(screen, yellow, (50,50),(350,350), 3 )
    pygame.draw.line(screen, yellow, (0,200),(400,200), 3 )
    pygame.draw.line(screen, yellow, (350,50),(50,350), 3 )
    pygame.draw.line(screen, yellow, (200,25),(200,375), 3 )
    # Update the display
    pygame.display.flip()
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()