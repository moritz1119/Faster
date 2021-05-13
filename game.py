import pygame
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Calibri', 30)
myfont2 = pygame.font.SysFont('Calibri', 20)
WIN_WIDTH = 200
WIN_HEIGHT = 400
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Faster")
red=(255,0,0)
blue=(0,0,255)
white=(255,255,255)
zähler_spieler=200
spielbeendet = False
spiel_begonnen = False
score_red = 0
score_blue = 0
def draw(spieler):
    pygame.draw.rect(screen,blue,(0,0,200,400),0)
    pygame.draw.rect(screen,red,(0,spieler,200,400),0)
def spiel_beendet():
    global spielbeendet
    if zähler_spieler == 400:
        spielbeendet = True
    if zähler_spieler == 0:
        spielbeendet = True
def reset():
    global zähler_spieler, spielbeendet, score_red, score_blue, spiel_begonnen
    if zähler_spieler == 0:
        score_red += 1
    elif zähler_spieler == 400:
        score_blue += 1
    zähler_spieler = 200
    spielbeendet=False
    spiel_begonnen = False
def draw_font():
    global spielbeendet, zähler_spieler, score_red, score_blue
    if spielbeendet == True:
        if zähler_spieler == 0:
            textsurface = myfont.render('RED WINS', False, white)
            screen.blit(textsurface,(100-textsurface.get_width()/2,200-textsurface.get_height()/2))
        elif zähler_spieler == 400:
            textsurface = myfont.render('BLUE WINS', False, white)
            screen.blit(textsurface,(100-textsurface.get_width()/2,200-textsurface.get_height()/2))
        textsurface2 = myfont2.render('PRESS R TO PLAY AGAIN', False, white)
        screen.blit(textsurface2,(100-textsurface2.get_width()/2,230-textsurface2.get_height()/2))
    #Punkte
    scorered = myfont2.render(str(score_red), False, white)
    screen.blit(scorered,(20-scorered.get_width()/2,380-scorered.get_height()/2))
    scoreblue = myfont2.render(str(score_blue), False, white)
    screen.blit(scoreblue,(20-scoreblue.get_width()/2,20-scoreblue.get_height()/2))
    #Erklärung
    if spiel_begonnen == False:
        erklaerung_blue = myfont2.render("PRESS ENTER", False, white)
        screen.blit(erklaerung_blue,(100-erklaerung_blue.get_width()/2,50-erklaerung_blue.get_height()/2))
        erklaerung_red = myfont2.render("PRESS SPACE", False, white)
        screen.blit(erklaerung_red,(100-erklaerung_red.get_width()/2,350-erklaerung_red.get_height()/2))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if spielbeendet==False:
                if event.key == pygame.K_RETURN:
                    zähler_spieler+=10
                    spiel_begonnen = True
                if event.key == pygame.K_SPACE:
                    zähler_spieler-=10
                    spiel_begonnen = True
            if event.key == pygame.K_r:
                if spielbeendet == True:
                    reset()
    spiel_beendet()
    draw(zähler_spieler)
    draw_font()
    pygame.display.update()
