import random
import sys
import pygame
import os


# Initialize Pygame
pygame.mixer.init()
pygame.init()
beep = pygame.mixer.Sound('beep (1).wav')
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

font = pygame.font.SysFont(None, 48)

# Set up the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")
score_a = 0
score_b = 0


paddle_w = 20
paddle_h = 80
paddle1_x = 15
paddle1_y = SCREEN_HEIGHT // 2 - paddle_h //2

paddle2_x = SCREEN_WIDTH - 15 - paddle_w
paddle2_y = SCREEN_HEIGHT // 2 - paddle_h //2
player_speed = 5

#Ball
ballx = SCREEN_WIDTH // 2
bally = SCREEN_HEIGHT // 2
ball_speed_x = 5
ball_speed_y = 5
ball_radius = 10


clock = pygame.time.Clock()

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)  # Set the frame rate to 60 frames per second

    keys = pygame.key.get_pressed()

    #Player 1 movement
    if keys[pygame.K_w]:
        paddle1_y -= player_speed
        paddle1_y = max(paddle1_y, 0)  # Ensure player does not move off the top edge
    if keys[pygame.K_s]:
        paddle1_y += player_speed
        paddle1_y = min(paddle1_y, SCREEN_HEIGHT - paddle_h)  # Ensure player does not move off the bottom edge

    #Player 2 movement
    if keys[pygame.K_UP]:
        paddle2_y -= player_speed
        paddle2_y = max(paddle2_y, 0)  # Ensure player does not move off the top edge
    if keys[pygame.K_DOWN]:
        paddle2_y += player_speed
        paddle2_y = min(paddle2_y, SCREEN_HEIGHT - paddle_h) 

    #Ball 
    ballx += ball_speed_x
    bally += ball_speed_y



    
    #Ball movement
    if bally <= 0 or bally >= SCREEN_HEIGHT:
        ball_speed_y *= -1

    if ballx <= 0 or ballx >= SCREEN_WIDTH:
        ballx = SCREEN_WIDTH // 2
        bally = SCREEN_HEIGHT // 2

    #Ball rectangle
    pygame.draw.circle(screen, BLACK, (ballx, bally), ball_radius)
    pygame.draw.rect(screen, BLACK,(paddle2_x, paddle2_y, paddle_w, paddle_h))
    pygame.draw.rect(screen, BLACK,(paddle1_x, paddle1_y, paddle_w, paddle_h))

    ball = pygame.Rect(ballx-ball_radius,bally-ball_radius, 2*ball_radius, 2*ball_radius)
    n1 = pygame.Rect(paddle1_x, paddle1_y, paddle_w, paddle_h)
    n2 = pygame.Rect(paddle2_x, paddle2_y, paddle_w, paddle_h)

    if (ball.colliderect(n2)) or ball.colliderect(n1):
        ball_speed_x =-ball_speed_x
        pygame.mixer.Sound.play(beep)



    #scoring
        
    if ballx >= SCREEN_WIDTH-5:
        score_a += 1
    if ballx <= 5:
        score_b += 1


    #Scoring display
    text = font.render(f"{score_a} - {score_b}", True, BLACK)
    center_text = (SCREEN_HEIGHT // 1.6, SCREEN_WIDTH // 20)
    screen.blit(text, (center_text))

    if (score_a == 10) or (score_b == 10):
        text = font.render(f"Game Over", True, BLACK)
        center_text = (SCREEN_WIDTH // 3, SCREEN_HEIGHT // 2)
        screen.blit(text, (center_text))
        
        break
        
    
    pygame.display.flip()
    


pygame.quit()
sys.exit()

