#Importing
import random
import sys
import pygame
import os
import math

#Initialize Pygame
pygame.init()

#runs
run = 0

#Pygame Sound
pygame.mixer.init()
fire = pygame.mixer.Sound('fire.wav')
small_bang = pygame.mixer.Sound('bangSmall.wav')
beep = pygame.mixer.Sound('beep (1).wav')
bullet_hit = pygame.mixer.Sound('extraShip.wav')

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

#powerup sizes/location/stats
powerup_size = random.randint(15,50)
powerup_x = random.randint(200, SCREEN_WIDTH - 200)
powerup_y = random.randint(0, SCREEN_HEIGHT - powerup_size)
number_of_powerups_used = 0

#Paddle Sizes
paddle_left_location_x = 40
paddle_left_location_y = SCREEN_HEIGHT // 2

paddle_right_location_x = SCREEN_WIDTH - 40
paddle_right_location_y = SCREEN_HEIGHT // 2

paddle_radius = 20
paddle_speed = 10

#Ball sizes
ball_x = SCREEN_WIDTH // 2
ball_y = SCREEN_HEIGHT // 2
ball_speed_x = 3
ball_speed_y = 3
ball_radius = 10

#Font
font = pygame.font.SysFont(None, 48)

#bullet stats
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
    run += 1
    #Paddles
    pygame.draw.circle(screen, BLACK, (paddle_left_location_x, paddle_left_location_y), paddle_radius)
    pygame.draw.circle(screen, RED, (paddle_right_location_x, paddle_right_location_y), paddle_radius)

    #create ball
    pygame.draw.circle(screen, BLUE, (ball_x, ball_y), ball_radius)

    #Recatangle around paddles and ball
    paddle_left = pygame.Rect(paddle_left_location_x - paddle_radius, paddle_left_location_y - paddle_radius, 2*paddle_radius, 2*paddle_radius)
    paddle_right = pygame.Rect(paddle_right_location_x - paddle_radius, paddle_right_location_y - paddle_radius, 2*paddle_radius, 2*paddle_radius)
    ball = pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, 2*ball_radius, 2*ball_radius)

    #Ball in motion
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    #Ball bouncing off walls
    if ball_y <= 0 or ball_y >= SCREEN_HEIGHT:
        ball_speed_y *= -1

    if ball_x <= 0 or ball_x >= SCREEN_WIDTH:
        ball_x = SCREEN_WIDTH // 2
        ball_y = SCREEN_HEIGHT // 2

    #Ball bouncing off paddles  
    if math.sqrt((ball_x - paddle_left_location_x)**2 + (ball_y - paddle_left_location_y)**2) <= paddle_radius + ball_radius:
        ball_speed_x *= -1
        pygame.mixer.Sound.play(beep)
    
    if math.sqrt((ball_x - paddle_right_location_x)**2 + (ball_y - paddle_right_location_y)**2) <= paddle_radius + ball_radius:
        ball_speed_x *= -1
        pygame.mixer.Sound.play(beep)


    # Key Movement
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


    # Left Bullet colliding with paddles
    if left_bullet.colliderect(paddle_right):
        if 0 <= right_score <= 2:
            left_score += 3
        elif right_score >= 3:
            right_score -= 3
        
        left_bullet = pygame.Rect(0,0,-100,100)
        pygame.mixer.Sound.play(bullet_hit)
    
    #Right bullet colliding with paddles
    if right_bullet.colliderect(paddle_left):
        if 0 <= left_score <= 2:
            right_score += 3
        elif left_score >= 3:
            left_score -= 3
        
        right_bullet = pygame.Rect(0,0,100,-100)
        pygame.mixer.Sound.play(bullet_hit)


    #Powerup creation

    pygame.draw.rect(screen, GREEN, (powerup_x, powerup_y, powerup_size, powerup_size))
    
    #Rectangle around powerup
    powerup = pygame.Rect(powerup_x, powerup_y, powerup_size, powerup_size)

    #left bullet collision with powerup
    if left_bullet.colliderect(powerup): #Length formula math.sqrt((x-x)^2 + (y-y)^2)
        left_random = random.randint(0,8)
        left_bullet = pygame.Rect(0,0,-1000,1000)

        if left_random == 1:
            left_score += 1
        
        elif left_random == 2:
            right_score -= 1
        
        elif left_random == 3:
            left_score += 2
        
        elif left_random == 4:
            right_score -= 2
        
        elif left_random == 5:
            ball_speed_x += 1
            ball_speed_y += 1
        
        elif left_random == 6:
            ball_radius -= 1
        
        elif left_random == 7:
            ball_radius += 1
        
        elif left_random == 8:
            left_score += 3
        

        powerup_size = random.randint(15,50)
        powerup_x = random.randint(200, SCREEN_WIDTH - 200)
        powerup_y = random.randint(0, SCREEN_HEIGHT - powerup_size)

    #Right bullet collision with powerup
    if right_bullet.colliderect(powerup): #Length formula math.sqrt((x-x)^2 + (y-y)^2)
        right_random = random.randint(0,8)
        right_bullet = pygame.Rect(0,0,1000,-1000)

        if right_random == 1:
            right_score += 1
        
        elif right_random == 2:
            left_score -= 1
        
        elif right_random == 3:
            right_score += 2
        
        elif right_random == 4:
            left_score -= 2
        
        elif right_random == 5:
            ball_speed_x += 1
            ball_speed_y += 1
        
        elif right_random == 6:
            ball_radius -= 1
        
        elif right_random == 7:
            ball_radius += 1
        
        elif right_random == 8:
            right_score += 3


        powerup_size = random.randint(15,50)
        powerup_x = random.randint(200, SCREEN_WIDTH - 200)
        powerup_y = random.randint(0, SCREEN_HEIGHT - powerup_size)


    #Scoring
    if ball_x >= SCREEN_WIDTH - ball_radius/4:
        left_score += 1 
    
    elif ball_x <= ball_radius/4:
        right_score += 1 

    #Scoring Display

    text = font.render(f"{left_score} - {right_score}", True, BLACK)
    center_text = (SCREEN_HEIGHT // 1.6, SCREEN_WIDTH // 20)
    screen.blit(text, (center_text))

    if (left_score >= 10) or (right_score >= 10):
        text = font.render(f"Game Over", True, BLACK)
        center_text = (SCREEN_WIDTH // 3, SCREEN_HEIGHT // 2)
        screen.blit(text, (center_text))
        pygame.display.flip()
        pygame.time.delay(5000)
        running = False


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    pygame.display.flip()

pygame.quit()
sys.exit()




