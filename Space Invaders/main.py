import math
import random

import pygame
from pygame import mixer

# Initialize the pygame
pygame.init()

# Creating the screen game       ((X Axis, Y Axis))
screen = pygame.display.set_mode((800, 600))  # TWO brackets important

# Title and Icon
pygame.display.set_caption("Space invaders")
icon = pygame.image.load("icons8-phoenix-squadron-32.png")
pygame.display.set_icon(icon)

# Background
# The -1 value in play makes it so that the music is kept in an infinite loop
mixer.music.load('background.wav')
mixer.music.play(-1)

# PLayer
playerImg = pygame.image.load('icons8-navette-spatiale-64.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemy_img = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6
for i in range(num_of_enemies):
    enemy_img.append(pygame.image.load('icons8-vaisseau-spatial-64.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)

# Bullet
# ready means that the bullet is non-visible
# fire means that the bullet will be visible and in a state of movement

bullet_img = pygame.image.load('icons8-balle-2-30.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 3
bullet_state = "ready"
# Score

score_value = 0
# 'freesansbold' is the only free front in pygame
# We can import fonts from the internet

font = pygame.font.Font('SuperLegendBoy.ttf', 16)

textX = 10
textY = 10
# Game over text
game_over_font = pygame.font.Font('SuperLegendBoy.ttf', 64)

def game_over_text():
    game_over = game_over_font.render("GAME OVER", True, (0, 0, 0))
    screen.blit(game_over, (150, 250))

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (0, 0, 0))
    screen.blit(score, (x, y))


# This function utility is drawing the playerImg in the coordinates specified
def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemy_img[i], (x, y))


# The fire_bullet function will be called when the space key is pressed
# We will use global to call the bullet_state variable that we defined earlier
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

# Game Loop that will keep the window screen open until we decide to close it
running = True
while running:
    # Background Color / RGB
    screen.fill((100, 100, 100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # If keystroke is pressed check whether it's right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change += -0.5
            if event.key == pygame.K_RIGHT:
                playerX_change += 0.5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_Sound = mixer.Sound('laser.wav')
                    # Or mixer.Sound.play()
                    # We didn't use the -1 value because we don't want it to loop forever
                    bullet_Sound.play()
                    # Gets the current x coordinate of the spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # The player's boundaries
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Enemy movements
    for i in range(num_of_enemies):
        # Game over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            collision_Sound = mixer.Sound('explosion.wav')
            collision_Sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            print(score_value)
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(40, 150)

        enemy(enemyX[i], enemyY[i], i)
    # Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # The function player should always be after the screen.fill()
    player(playerX, playerY)

    show_score(textX, textY)

    # Important for mechanisms etc. Updates the game window (IMPORTANT)
    pygame.display.update()
