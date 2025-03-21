import pygame
white = (255, 255, 255)
green = (255, 255, 255)
pygame.init()

size = 500
center = (size//2 , size//2)
window = pygame.display.set_mode((size,size))
clock = pygame.time.Clock()

def draw_seconds(surface,second):
    hand_length = size * 0.4
    angle = - second*6
    end_x = center[0] + hand_length * pygame.math.Vector2(0,-1).rotate(angle).x
    end_y= center[1] + hand_length * pygame.math.Vector2(0,-1).rotate(angle).y
    pygame.draw.line(surface,gray,center,(end_x,end_y), 5 )

def main():
    running = True
    while running:
        window.fill(white)
        now = datetime.now()
        draw_seconds(window,now.second)
        pygame.display.flip()
        clock.tick(1)

        for event in pygame.event.get():
            if event.type == game.QUIT:
                running = False
    pygame.quit()

main()