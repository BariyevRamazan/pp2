import pygame, sys
from pygame.locals import *
import random, time

pygame.init()
clock = pygame.time.Clock()
width = 400
height = 600
SPEED = 5
SCORE = 0
speed = 60

myfont = pygame.font.Font("fonts//Boldonse-Regular.ttf", 20)
font_small = pygame.font.Font("fonts//Boldonse-Regular.ttf", 20)
game_over = myfont.render("Game Over!", True, "BLACK")


background = pygame.image.load("AnimatedStreet.png")

DISPLAYSURF = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game")


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > height:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, width - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (width // 2, height - 80)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT] and self.rect.right < width:
            self.rect.move_ip(5, 0)


coin = pygame.image.load("coin.png")
cell_size = 10
x = random.randint(0, (width // cell_size) - 1) * cell_size
y = 0
coin_pos = [x, y]

P1 = Player()
E1 = Enemy()

enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

points = 0
levels = 1


while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    coin_pos[1] += SPEED
    if coin_pos[1] > height:
        x = random.randint(0, (width // cell_size) - 1) * cell_size
        y = 0
        coin_pos = [x, y]

    if P1.rect.collidepoint(coin_pos):
        points += 1
        if points % 3 == 0:
            levels += 1
            speed += 4
        x = random.randint(0, (width // cell_size) - 1) * cell_size
        y = 0
        coin_pos = [x, y]

    DISPLAYSURF.blit(background, (0, 0))
    score_text = font_small.render(f"Enemies Passed: {SCORE} | Coins: {points}", True, "BLACK")
    DISPLAYSURF.blit(score_text, (10, 10))
    DISPLAYSURF.blit(coin, coin_pos)

    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound("crash.wav").play()
        time.sleep(0.5)
        DISPLAYSURF.fill("RED")
        DISPLAYSURF.blit(game_over, (width // 2 - 140, height // 2 - 30))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    clock.tick(speed)
