import pygame

pygame.init()


prozor = pygame.display.set_mode((800,800))
pygame.display.set_caption("doom")

slika = pygame.image.load("nm.png")

#Boje
BELA = (255,255,255)
CRNA = (0,0,0)
CRVENA = (255,0,0)
ZELENA = (0,255,0)
PLAVA = (0,0,255)
LJUBICASTA = (100,10,100)

radi = True
while radi:
    for dogadjaj in pygame.event.get():
        if dogadjaj.type == pygame.QUIT:
            radi = False

    prozor.fill(BELA)
    pygame.display.update()

pygame.quit()