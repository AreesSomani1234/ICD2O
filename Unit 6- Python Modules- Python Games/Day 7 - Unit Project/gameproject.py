#Importing
import random
import sys
import pygame
import os
import math

#Initialize Pygame
pygame.init()

#Pygame Sound
pygame.mixer.init()
fire = pygame.mixer.Sound('fire.wav')
small_bang = pygame.mixer.Sound('bangSmall.wav')

#Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BROWN = (139, 69, 19)
GREY = (128, 128, 128)
YELLOW = (255, 255, 0)

#Screen Setup
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Pygame Caption
pygame.display.set_caption("Super Pong")

#Beginning Score
left_score = 0
right_score = 0

#Paddle Sizes
paddle_left_location_x = 40
paddle_left_location_y = SCREEN_HEIGHT // 2

paddle_right_location_x = SCREEN_WIDTH - 40
paddle_right_location_y = SCREEN_HEIGHT // 2

paddle_radius = 20
paddle_speed = 10

#bullet
bullet_length = 45
bullet_width = 10

left_bullet = pygame.Rect(paddle_left_location_x + paddle_radius, paddle_left_location_y  , bullet_length, bullet_width)
left_bullet_motion = False

right_bullet = pygame.Rect(paddle_right_location_x - bullet_length + paddle_radius, paddle_right_location_y  , bullet_length,  bullet_width)
right_bullet_motion = False

bullet_speed = 5
bullet_count_left = 0
bullet_count_right = 0

#clock
clock = pygame.time.Clock()


#Main Loop
running = True
while running:
    screen.fill(WHITE)
    #clock
    clock.tick(60)

    #Paddles
    pygame.draw.circle(screen, BLACK, (paddle_left_location_x, paddle_left_location_y), paddle_radius)
    pygame.draw.circle(screen, RED, (paddle_right_location_x, paddle_right_location_y), paddle_radius)

    #Recatangle around paddles
    paddle_left = pygame.Rect(paddle_left_location_x - paddle_radius, paddle_left_location_y - paddle_radius, 2*paddle_radius, 2*paddle_radius)
    paddle_right = pygame.Rect(paddle_right_location_x - paddle_radius, paddle_right_location_y - paddle_radius, 2*paddle_radius, 2*paddle_radius)


    #Movement
    keys = pygame.key.get_pressed()

    #Left paddle movement
    if keys[pygame.K_w]:
        paddle_left_location_y -= paddle_speed
        paddle_left_location_y = max(paddle_left_location_y, 20)  # player does not move past top edge
    if keys[pygame.K_s]:
        paddle_left_location_y += paddle_speed
        paddle_left_location_y = min(paddle_left_location_y, SCREEN_HEIGHT - paddle_radius)  # player does not move past bottom edge

    #Right paddle movement
    if keys[pygame.K_UP]:
        paddle_right_location_y -= paddle_speed
        paddle_right_location_y = max(paddle_right_location_y, 20)  # player does not move past top edge
    if keys[pygame.K_DOWN]:
        paddle_right_location_y += paddle_speed
        paddle_right_location_y = min(paddle_right_location_y, SCREEN_HEIGHT - paddle_radius) # player does not move past bottom edge

    #Left Shooting movement
    if (keys[pygame.K_d]) and (left_bullet_motion == False) and (bullet_count_left <= 5):
        left_bullet = pygame.Rect(paddle_left_location_x + paddle_radius, paddle_left_location_y , bullet_length, bullet_width)
        bullet_count_left += 1
        left_bullet_motion = True
        pygame.mixer.Sound.play(fire)

    if left_bullet_motion:
        pygame.draw.rect(screen, BLACK, [left_bullet.x, left_bullet.y,left_bullet.w, left_bullet.h])
        left_bullet.x += bullet_speed
        if left_bullet.x >= SCREEN_WIDTH:
            left_bullet_motion = False


    #Right Shooting movement
    if (keys[pygame.K_LEFT]) and (right_bullet_motion == False) and (bullet_count_right <= 5):
        right_bullet = pygame.Rect(paddle_right_location_x - bullet_length + paddle_radius, paddle_right_location_y, bullet_length, bullet_width)
        bullet_count_right += 1
        right_bullet_motion = True
        pygame.mixer.Sound.play(fire)
    
    if right_bullet_motion:
        pygame.draw.rect(screen, RED, [right_bullet.x, right_bullet.y, right_bullet.w, right_bullet.h])
        right_bullet.x -= bullet_speed
        if right_bullet.x <= 0:
            right_bullet_motion = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    pygame.display.flip()

pygame.quit()
sys.exit()



