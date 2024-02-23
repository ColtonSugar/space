import pygame
import random

# Initialize Pygame
pygame.init()

# Screen settings
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)  # Black

# Player settings
PLAYER_SIZE = 50
PLAYER_COLOR = (0, 0, 255)  # Blue
PLAYER_SPEED = 5

# Enemy settings
ENEMY_SIZE = 50
ENEMY_COLOR = (255, 0, 0)  # Red
ENEMY_SPEED = 1
ENEMY_RESPAWN_RATE = 1  # Higher number means slower respawn

# Bullet settings
BULLET_SIZE = 5
BULLET_COLOR = (255, 255, 255)  # White
BULLET_SPEED = 5

# Setup the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invader")

# Player
player = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 60, PLAYER_SIZE, PLAYER_SIZE)

# Enemies
enemies = [pygame.Rect(random.randint(0, SCREEN_WIDTH - ENEMY_SIZE), 0, ENEMY_SIZE, ENEMY_SIZE) for _ in range(5)]

# Bullets
bullets = []

def move_player():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT] and player.x < SCREEN_WIDTH - PLAYER_SIZE:
        player.x += PLAYER_SPEED

def move_bullets():
    for bullet in bullets[:]:
        bullet.y -= BULLET_SPEED
        if bullet.y < 0:
            bullets.remove(bullet)

def move_enemies():
    global running  # Need to access the global running variable to end the game
    for enemy in enemies[:]:
        enemy.y += ENEMY_SPEED
        if enemy.y + ENEMY_SIZE >= SCREEN_HEIGHT:  # Check if any enemy has reached the bottom
            running = False  # End the game
            print("Game Over!")  # Optionally, print a message to the console

def check_collisions():
    for bullet in bullets[:]:
        for enemy in enemies[:]:
            if bullet.colliderect(enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)
                enemies.append(pygame.Rect(random.randint(0, SCREEN_WIDTH - ENEMY_SIZE), 0, ENEMY_SIZE, ENEMY_SIZE))
                break

def draw_objects():
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen, PLAYER_COLOR, player)
    for bullet in bullets:
        pygame.draw.rect(screen, BULLET_COLOR, bullet)
    for enemy in enemies:
        pygame.draw.rect(screen, ENEMY_COLOR, enemy)
    pygame.display.flip()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(pygame.Rect(player.x + player.width // 2 - BULLET_SIZE / 2, player.y, BULLET_SIZE, BULLET_SIZE))
    
    move_player()
    move_bullets()
    move_enemies()
    check_collisions()
    draw_objects()

    pygame.time.Clock().tick(60)

pygame.quit()