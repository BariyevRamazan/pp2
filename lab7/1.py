import datetime
import pygame
import time

pygame.init()
CEN=(350,250)
def rot(im, an, offset):
    rom=pygame.transform.rotate(im, -an)
    ror=rom.get_rect(center=CEN)
    return rom,ror
s=pygame.image.load("sec_hand (1).png")
m=pygame.image.load("min_hand (1).png")
scr=pygame.display.set_mode((700,500))
muk=pygame.image.load("clock.png")
x=350-muk.get_width()/2
y=250-muk.get_height()/2
done=True
while done:
    for ev in pygame.event.get():
        if ev.type==pygame.QUIT:
            done=False
    time.sleep(1)
    se=datetime.datetime.now().second
    mi=datetime.datetime.now().minute
    angs=(se%60)*6-60
    angm=(mi%60)*6+60
    rh,rp=rot(m,angm,CEN)
    lh,lp=rot(s,angs,CEN)
    scr.blit(muk,(x,y))
    scr.blit(lh,lp)
    scr.blit(rh,rp)
    pygame.display.update()
    pygame.display.flip()