import pygame

pygame.init()

SONG_END = pygame.USEREVENT + 1
clock=pygame.time.Clock()
scr=pygame.display.set_mode((700,500))
done=True
songs={
    "Ace Of Base - Happy Nation.mp3":"happy.jpg",
    "Indila – Dernière danse.mp3":"indila.jpg",
    "Instupendo - Comfort Chain.mp3":"comfort.jpg",
    "Fifty Fifty - Cupid.mp3":"cupid.jpg",
    "347aidan - Dancing in My Room.mp3":"dir.jpg"
}
b=False
i=0
g=len(songs)
def play(i):
    scr.fill((0,0,0))
    pygame.mixer.music.load(list(songs.keys())[i%g])
    pygame.mixer.music.play()
    p=pygame.image.load(songs[list(songs.keys())[i%g]])
    p=pygame.transform.scale(p,(700,500))
    scr.blit(p,(0,0))

while done:
    for ev in pygame.event.get():
        if ev.type==pygame.QUIT:
            done=False
        if ev.type==SONG_END:
            i+=1
            play(i)
        if ev.type==pygame.KEYDOWN:
            if ev.key==pygame.K_a:
                play(i)
            if ev.key==pygame.K_s:
                pygame.mixer.music.stop()
                i+=1
                play(i)
            if ev.key==pygame.K_d:
                pygame.mixer.music.stop()
            if ev.key==pygame.K_f:
                pygame.mixer.music.stop()
                i-=1
                play(i)

    pre=pygame.key.get_pressed()
    pygame.display.flip()
    clock.tick(60)