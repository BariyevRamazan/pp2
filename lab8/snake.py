import pygame
import sys
import random

pygame.init()

# Размеры величин
width, length = 1023, 718
cell_size = 20

screen = pygame.display.set_mode((width, length))
pygame.display.set_caption("Simple Snake")

# Фото
body = [
    pygame.image.load("pixils/head.png"),
    pygame.image.load("pixils/mid.png"),
    pygame.image.load("pixils/tail.png")
]
zone = pygame.image.load("images/zone.png")
apple = pygame.image.load("pixils/apple.png")

# Шрифт для текста уровня и очков
myfont = pygame.font.Font("fonts/Boldonse-Regular.ttf", 20)

# Самые важные параметры
points = 0
levels = 0
snake_pos = [100, 100]
snake_body = [[100, 100], [80, 100], [60, 100]]
direction = "RIGHT"
change_to = direction
speed = 5
clock = pygame.time.Clock()

# Первая яблоко
while True:
    x = random.randint(0, (width // cell_size) - 1) * cell_size
    y = random.randint(0, (length // cell_size) - 1) * cell_size
    if [x, y] not in snake_body:
        apple_pos = [x,y]
        break

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                change_to = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                change_to = "DOWN"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                change_to = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                change_to = "RIGHT"
    
    # Движение змейки
    direction = change_to
    if direction == "UP":
        snake_pos[1] -= cell_size
    elif direction == "DOWN":
        snake_pos[1] += cell_size
    elif direction == "LEFT":
        snake_pos[0] -= cell_size
    elif direction == "RIGHT":
        snake_pos[0] += cell_size

    # Проверка выхода за границы
    if snake_pos[0] >= width or snake_pos[0] < 0 or snake_pos[1] >= length or snake_pos[1] < 0:
        running = False

    # Проверка столкновения с собой чтобы потом игра закончилось
    if snake_pos in snake_body:
        running = False


    snake_body.insert(0, list(snake_pos))

    # Хавает ли змея яблоко
    if snake_pos == apple_pos or snake_pos == list(map(lambda x: x + cell_size, apple_pos))  or snake_pos == list(map(lambda x: x-cell_size, apple_pos)) :
        points += 1
        if points % 3 == 0:
            levels += 1
            speed += 4
        while True:
            x = random.randint(0, (width // cell_size) - 1) * cell_size
            y = random.randint(0, (length // cell_size) - 1) * cell_size
            if [x, y] not in snake_body and [x,y] != apple_pos :
                apple_pos = [x,y]
                break    
    else:
        snake_body.pop()

    # Фон и текст
    screen.blit(zone, (0, 0))
    text = myfont.render(f"Points: {points}  Level: {levels}", False, "RED")
    screen.blit(text, (50, 0))

    # Рисовка змеи
    for i, pos in enumerate(snake_body):
        if i == 0:
            if direction =="UP":
                head_new = pygame.transform.rotate(body[0], 90)
            elif direction == "DOWN" :
                head_new = pygame.transform.rotate(body[0], -90)
            elif direction == "LEFT":
                head_new = pygame.transform.rotate(body[0], 180)
            else:
                head_new = pygame.transform.rotate(body[0], 0)
            screen.blit(head_new, pygame.Rect(pos[0], pos[1], cell_size, cell_size))
        elif i == len(snake_body) - 1:
            if direction =="UP":
                tail_new = pygame.transform.rotate(body[2], 90)
            elif direction == "DOWN" :
                tail_new = pygame.transform.rotate(body[2], -90)
            elif direction == "LEFT":
                tail_new = pygame.transform.rotate(body[2], 180)
            else:
                tail_new = pygame.transform.rotate(body[2], 0)
            screen.blit(tail_new, pygame.Rect(pos[0], pos[1], cell_size, cell_size))
        else:
            if direction =="UP":
                mid_new = pygame.transform.rotate(body[1], 90)
            elif direction == "DOWN" :
                mid_new = pygame.transform.rotate(body[1], -90)
            else:
                mid_new = pygame.transform.rotate(body[1], 0)
            screen.blit(mid_new, pygame.Rect(pos[0], pos[1], cell_size, cell_size))

    # Яблоко
    screen.blit(apple, pygame.Rect(apple_pos[0], apple_pos[1], cell_size, cell_size))
    
    pygame.display.flip()
    clock.tick(speed)

pygame.quit()
sys.exit()
