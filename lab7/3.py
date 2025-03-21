import pygame

pygame.init()

clock=pygame.time.Clock()
scr=pygame.display.set_mode((700,500))
scr.fill((255,255,255))
x=350
y=250
r=25
done=True
while done:
    for ev in pygame.event.get():
        if ev.type==pygame.QUIT:
            done=False
    pre=pygame.key.get_pressed()
    if pre[pygame.K_DOWN] and y+r+20<=500:y+=20
    elif pre[pygame.K_DOWN]: y=475
    if pre[pygame.K_UP] and y-r-20>=0:y-=20
    elif pre[pygame.K_UP]:y=25
    if pre[pygame.K_LEFT] and x-r-20>=0:x-=20
    elif pre[pygame.K_LEFT]:x=25
    if pre[pygame.K_RIGHT] and x+r+20<=700:x+=20
    elif pre[pygame.K_RIGHT]:x=675
    scr.fill((255,255,255))
    pygame.draw.circle(scr,(255,0,0),(x,y),radius=r)
    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)