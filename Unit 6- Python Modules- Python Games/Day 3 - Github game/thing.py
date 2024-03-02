import pygame
import sys
 
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 700
 
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mini Project")
 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BROWN = (139, 69, 19)
GREY = (128, 128, 128)
YELLOW = (255, 255, 0)
 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
 
    screen.fill(BLACK)
    # Moon base
    pygame.draw.rect(screen, GREEN, (0, SCREEN_HEIGHT - 100, SCREEN_WIDTH, 100))
    # Star
    pygame.draw.polygon(screen, YELLOW, [(400, 50), (500, 50), (415, 110), (450, 10), (485, 110)])
    pygame.draw.polygon(screen, YELLOW, [(400, 150), (500, 150), (415, 210), (450, 100), (485, 210)])
    #Sun
    pygame.draw.circle(screen, YELLOW, (100, 100), 50)
 
    #Planets
    pygame.draw.circle(screen, BLUE, (320, 150), 50)
    pygame.draw.circle(screen, GREEN, (960, 350), 70)
 
    #Buildings
    window_color = (200, 200, 200)  # Window color (light gray)
    pygame.draw.rect(screen, RED, (450, 400, 250, 300))
    pygame.draw.rect(screen, window_color, (470, 420, 80, 100))  # First window
    pygame.draw.rect(screen, window_color, (610, 420, 80, 100))  # Second window
    pygame.draw.rect(screen, window_color, (470, 540, 80, 100))  # Third window
    pygame.draw.rect(screen, window_color, (610, 540, 80, 100))  # Fourth window
 
 
    #Pole
    pygame.draw.rect(screen, RED, (105, 450, 80, 100))  
    pygame.draw.line(screen, GREY, (105, 550), (105, 600 - 150), 5)
 
    pygame.display.flip()
 
pygame.quit()