import pygame
import os
from random import randint
import math

pygame.init()
pygame.mixer.init()


display_width=1536  #displaySize
display_height=400



os.environ['SDL_VIDEO_WINDOW_POS'] = "0,30"

gDisplay = pygame.display.set_mode((display_width,display_height))





pygame.display.set_caption("KILL'EM ALL")
clock = pygame.time.Clock()

lives=10
lives_left=lives
inProgress=True
score=0




def display_lives():
    if lives_left>0:
        message = "lives: %s/%s" % (lives_left, lives)
    else:
        message = "YOU LOST"

    font = pygame.font.Font('freesansbold.ttf', 50)
    label = font.render(message+" score: "+str(score), 1, (0, 0, 0))
    gDisplay.blit(label, ((0, 0)))


class Home:
    lives=int
    alive=bool
    isOut=bool
    downTime=int
    missTime=int
    delay=int
    tempo=int
    time_shown=int
    key=str

    x = int
    y = int

    mole_x = int
    mole_y = int

    hole_x = int
    hole_y = int

    holeIMG = pygame.image
    moleIMG = pygame.image
    starsIMG = pygame.image


    def __init__(self,x=20,y=50,tempo=50,key=x):

        self.isOut=True
        self.downTime=0
        self.missTime=0
        self.delay=randint(0,30)
        self.tempo=tempo
        self.time_shown=0
        self.key=key

        self.x=x
        self.y=y

        self.mole_x=self.x+40
        self.mole_y=self.y

        self.hole_x=self.x
        self.hole_y=self.y+120

        self.holeIMG = pygame.image.load("hole.png")
        self.moleIMG = pygame.image.load("mole.png")
        self.starsIMG = pygame.image.load("stars.png")
        self.font = pygame.font.Font('freesansbold.ttf', 70)
        self.missFont = pygame.font.SysFont('comicsans.ttf', 70)
        self.roar = pygame.mixer.Sound("roar.wav")
        self.roar.set_volume(0.5)
        self.miss = pygame.mixer.Sound("miss.wav")
        self.hide = pygame.mixer.Sound("hide.wav")
        self.show = pygame.mixer.Sound("show.wav")
        self.show.set_volume(0.5)

    def key_display(self):
        label = self.font.render(self.key, 1, (0, 0, 0))
        gDisplay.blit(label, ((self.x+100, self.y+160)))

    def display(self):
        gDisplay.blit(self.moleIMG,((self.mole_x, self.mole_y)))
        gDisplay.blit(self.holeIMG,((self.hole_x, self.hole_y)))
        if self.downTime>0:
            gDisplay.blit(self.starsIMG, ((self.x+35, self.y+60)))
            self.downTime-=1
        if self.missTime > 0:
            label = self.missFont.render("miss", 1, (255, 64, 0))
            gDisplay.blit(label, ((self.x+70, self.y+60)))
            self.missTime-=1
        self.time_shown+=1
        self.key_display()

    def check_for_timeout(self):
        if (self.time_shown > 120 and self.isOut==True):
            self.hide.play()
            self.time_shown=0
            self.mole_hide()
            return (-1)
        else: return (0)


    def mole_show(self):
        if (math.fmod(pygame.time.get_ticks()+self.delay, self.tempo) == 0) and randint(0,3)==0:
            if inProgress==True:
                self.show.play()
                self.isOut=True
                self.mole_y=self.y
                self.time_shown=0


    def mole_hide(self):
        self.mole_y=self.y+100
        self.isOut=False

    def stars_show(self):
        gDisplay.blit(self.starsIMG, ((self.x, self.y)))

    def hit(self):
        if self.isOut:
            self.roar.play()
            self.mole_hide()
            self.downTime=10
            return(1)
        else:
            self.miss.play()
            self.missTime = 10
            return(-1)





home0=Home(5,key='x')
home1=Home(260,key='c')
home2=Home(515,key='v')
home3=Home(770,key='b')
home4=Home(1025,key='n')
home5=Home(1280,key='m')


def logic():
    global score
    global lives_left

    if(inProgress):
        home0.mole_show()
        home1.mole_show()
        home2.mole_show()
        home3.mole_show()
        home4.mole_show()
        home5.mole_show()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            return 1

        if event.type == pygame.KEYDOWN:
            if(inProgress):
                if event.key==pygame.K_x:
                    val=home0.hit()
                    if val == 1:
                        score += 1
                    if val== -1:
                        lives_left -= 1
                elif event.key==pygame.K_c:
                    val=home1.hit()
                    if val == 1:
                        score += 1
                    if val== -1:
                        lives_left -= 1
                elif event.key==pygame.K_v:
                    val = home2.hit()
                    if val == 1:
                        score += 1
                    if val == -1:
                        lives_left -= 1
                elif event.key==pygame.K_b:
                    val = home3.hit()
                    if val == 1:
                        score += 1
                    if val == -1:
                        lives_left -= 1
                elif event.key==pygame.K_n:
                    val = home4.hit()
                    if val == 1:
                        score += 1
                    if val == -1:
                        lives_left -= 1
                elif event.key==pygame.K_m:
                    val = home5.hit()
                    if val == 1:
                        score += 1
                    if val == -1:
                        lives_left -= 1






            print(event)


def main_loop():
    home0.mole_hide()
    home1.mole_hide()
    home2.mole_hide()
    home3.mole_hide()
    home4.mole_hide()
    home5.mole_hide()
    global lives_left
    global inProgress
    while not logic():





        gDisplay.fill((16,128,0))
        home0.display()
        home1.display()
        home2.display()
        home3.display()
        home4.display()
        home5.display()

        lives_left=lives_left+home1.check_for_timeout()+home2.check_for_timeout()+home3.check_for_timeout()+home4.check_for_timeout()+home5.check_for_timeout()
        if(lives_left<1):
            inProgress=False
            home0.mole_hide()
            home1.mole_hide()
            home2.mole_hide()
            home3.mole_hide()
            home4.mole_hide()
            home5.mole_hide()

        display_lives()
        pygame.display.flip()
        clock.tick(64)
        print(score)


main_loop()
pygame.quit()
quit()

