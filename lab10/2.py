import pygame
import sys
import random
import time
import psycopg2


conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="kot13",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS user_data (
        username VARCHAR(50) PRIMARY KEY,
        score INTEGER DEFAULT 0,
        level INTEGER DEFAULT 0
    )
""")
conn.commit()
username = input("Enter username: ")
cur.execute("SELECT score, level FROM user_data WHERE username = %s", (username,))
user = cur.fetchone()

if user:
    points, levels = user
    print(f"Welcome back, {username}! Your level: {levels}, score: {points}")
else:
    cur.execute("INSERT INTO user_data (username, score, level) VALUES (%s, %s, %s)", (username, 0, 0))
    conn.commit()
    print(f"New user {username} created.")
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
big = pygame.image.load("big2.png")
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

# Первая еда
apple_pos = None
food_weight = 1
food_spawn_time = 0
food_type = "apple"

def generate_food():
    global apple_pos, food_weight, food_type, food_spawn_time
    coin_type = random.choice(["apple", "big"]) 
    if coin_type == "apple":
        food_weight = 1
        food_type = "apple"
    else:
        food_weight = 2
        food_type = "big"
    
    # Генерация случайных координат для еды
    x = random.randint(0, (width // cell_size) - 1) * cell_size
    y = random.randint(0, (length // cell_size) - 1) * cell_size
    if [x, y] not in snake_body:
        apple_pos = [x, y]
        food_spawn_time = time.time() 

generate_food()  # Изначально создаем еду

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
            elif event.key == pygame.K_SPACE:  
                cur.execute(
                    "UPDATE user_data SET score = %s, level = %s WHERE username = %s",
                    (points, levels, username)
                )
                conn.commit()
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

    # Проверка столкновения с собой
    if snake_pos in snake_body:
        running = False

    snake_body.insert(0, list(snake_pos))

    # Хавает ли змея еду
    if snake_pos == apple_pos or snake_pos == list(map(lambda x: x + cell_size, apple_pos))  or snake_pos == list(map(lambda x: x-cell_size, apple_pos)) :
        points += food_weight
        if points % 3 == 0:
            levels += 1
            speed += 4
        generate_food()  # Генерируем новую еду
    else:
        snake_body.pop()


    if time.time() - food_spawn_time > 10:
        apple_pos = None
        generate_food() 

    screen.blit(zone, (0, 0))
    text = myfont.render(f"Points: {points}  Level: {levels}", False, "RED")
    screen.blit(text, (50, 0))

    # Рисовка змеи
    for i, pos in enumerate(snake_body):
        if i == 0:
            if direction == "UP":
                head_new = pygame.transform.rotate(body[0], 90)
            elif direction == "DOWN":
                head_new = pygame.transform.rotate(body[0], -90)
            elif direction == "LEFT":
                head_new = pygame.transform.rotate(body[0], 180)
            else:
                head_new = pygame.transform.rotate(body[0], 0)
            screen.blit(head_new, pygame.Rect(pos[0], pos[1], cell_size, cell_size))
        elif i == len(snake_body) - 1:
            if direction == "UP":
                tail_new = pygame.transform.rotate(body[2], 90)
            elif direction == "DOWN":
                tail_new = pygame.transform.rotate(body[2], -90)
            elif direction == "LEFT":
                tail_new = pygame.transform.rotate(body[2], 180)
            else:
                tail_new = pygame.transform.rotate(body[2], 0)
            screen.blit(tail_new, pygame.Rect(pos[0], pos[1], cell_size, cell_size))
        else:
            if direction == "UP":
                mid_new = pygame.transform.rotate(body[1], 90)
            elif direction == "DOWN":
                mid_new = pygame.transform.rotate(body[1], -90)
            else:
                mid_new = pygame.transform.rotate(body[1], 0)
            screen.blit(mid_new, pygame.Rect(pos[0], pos[1], cell_size, cell_size))

    # Рисуем еду
    if apple_pos:
        if food_type == "apple":
            screen.blit(apple, pygame.Rect(apple_pos[0], apple_pos[1], cell_size, cell_size))
        elif food_type == "big":
            screen.blit(big, pygame.Rect(apple_pos[0], apple_pos[1], cell_size, cell_size))

    pygame.display.flip()
    clock.tick(speed)
cur.close()
conn.close()
pygame.quit()
sys.exit()
