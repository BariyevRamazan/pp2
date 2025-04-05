import pygame
import sys

pygame.init()
width, height = 1000, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Simple Paint')

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
gray = (200, 200, 200)

current = None
start_pos = None
drawing = False
brush_color = black

class Button:
    def __init__(self, x, y, width, height, text, color, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.action = action

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        font = pygame.font.Font(None, 30)
        text_surface = font.render(self.text, True, white if self.color != gray else black)
        screen.blit(text_surface, (self.rect.x + 10, self.rect.y + 5))

    def check_action(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.action()

def set_black():
    global brush_color
    brush_color = black

def set_green():
    global brush_color
    brush_color = green

def set_red():
    global brush_color
    brush_color = red

def set_blue():
    global brush_color
    brush_color = blue

def clear_screen():
    screen.fill(white)

def exit_app():
    pygame.quit()
    sys.exit()

def set_eraser():
    global brush_color
    brush_color = white

def set_circle():
    global current
    current = 'circle'

def set_rectangle():
    global current
    current = 'rectangle'

def set_square():
    global current
    current = 'square'

def set_tr():
    global current
    current = 'tr'

def set_eq_t():
    global current
    current ="Eq_t"

def set_romb():
    global current
    current = 'romb'

buttons = [
    Button(10, 10, 60, 30, 'Black', black, set_black),
    Button(80, 10, 60, 30, 'Green', green, set_green),
    Button(150, 10, 60, 30, 'Red', red, set_red),
    Button(220, 10, 60, 30, 'Blue', blue, set_blue),
    Button(290, 10, 60, 30, 'Clear', gray, clear_screen),
    Button(360, 10, 60, 30, 'Exit', gray, exit_app),
    Button(430, 10, 60, 30, 'Eraser', gray, set_eraser),
    Button(500, 10, 60, 30, 'Circle', gray, set_circle),
    Button(570, 10, 60, 30, 'Rectangle', gray, set_rectangle),
    Button(640, 10, 60, 30, 'Square', gray, set_square),
    Button(710, 10, 60, 30, 'Triang', gray, set_tr),
    Button(780, 10, 60, 30, 'Eq_t', gray, set_eq_t),
    Button(850, 10, 60, 30, 'Romb', gray, set_romb)
]

clear_screen()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            drawing = True
            start_pos = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            drawing = False
            start_pos = None

        for button in buttons:
            button.check_action(event)

    if drawing:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if mouse_y > 50:
            if current == 'circle' and start_pos:
                pygame.draw.circle(screen, brush_color, start_pos, int(((mouse_x - start_pos[0]) ** 2 + (mouse_y - start_pos[1]) ** 2) ** 0.5))
            elif current == 'rectangle' and start_pos:
                pygame.draw.rect(screen, brush_color, pygame.Rect(start_pos[0], start_pos[1], mouse_x - start_pos[0], mouse_y - start_pos[1]), 2)
            elif current == 'square' and start_pos:
                size = min(abs(mouse_x - start_pos[0]), abs(mouse_y - start_pos[1]))
                pygame.draw.rect(screen, brush_color, pygame.Rect(start_pos[0], start_pos[1], size, size), 2)
            elif current == 'tr' and start_pos:
                points = [(start_pos[0], start_pos[1]), (mouse_x, start_pos[1]), (start_pos[0], mouse_y)]
                pygame.draw.polygon(screen, brush_color, points)
            elif current == 'Eq_t' and start_pos:
                height = (3 ** 0.5 / 2) * abs(mouse_x - start_pos[0])
                points = [(start_pos[0], start_pos[1]), (mouse_x, start_pos[1]), ((start_pos[0] + mouse_x) / 2, start_pos[1] - height)]
                pygame.draw.polygon(screen, brush_color, points)
            elif current == 'romb' and start_pos:
                width = abs(mouse_x - start_pos[0])
                height = abs(mouse_y - start_pos[1])
                points = [(start_pos[0], start_pos[1] - height), (start_pos[0] + width, start_pos[1]), (start_pos[0], start_pos[1] + height), (start_pos[0] - width, start_pos[1])]
                pygame.draw.polygon(screen, brush_color, points)

    pygame.draw.rect(screen, gray, (0, 0, width, 50))
    for button in buttons:
        button.draw(screen)

    pygame.display.update()
