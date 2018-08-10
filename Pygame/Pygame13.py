import pygame
import random
from sys import exit

class Bullet:
    def __init__(self):
        self.x=0
        self.y=-1
        self.image=pygame.image.load('bullet.png').convert_alpha()
        self.active=False

    def move(self):
        if self.active:
            self.y-=3
        if self.y<0:
            self.active = False
    def restart(self):
        mouseX, mouseY=pygame.mouse.get_pos()
        self.x=mouseX-self.image.get_width()/2
        self.y=mouseY-self.image.get_height()/2
        self.active=True

class Enemy:
    def restart(self):
        self.x=random.randint(50,400)
        self.y=random.randint(-200,-50)        
        self.speed=random.random()+0.1

    def __init__(self):
        self.restart()
        self.image=pygame.image.load('enemy.png').convert_alpha()

    def move(self):
        if self.y<800:
            self.y+=self.speed
        else:
            self.restart()
class Plane:
    def restart(self):
        self.x=200
        self.y=600
    def __init__(self):
        self.restart()
        self.image=pygame.image.load('plane.png').convert_alpha()

    def move(self):
        x,y=pygame.mouse.get_pos()
        x-=self.image.get_width()/2
        y-=self.image.get_height()/2
        self.x=x
        self.y=y


def checkHit(enemy,bullet):
    if (bullet.x>enemy.x and bullet.x<enemy.x+enemy.image.get_width())and \
       (bullet.y>enemy.y and bullet.y<enemy.y+enemy.image.get_height()):
        enemy.restart()
        bullet.active=False
        return True
    return False

def checkCrash(enemy,plane):
    if (plane.x+0.7*plane.image.get_width()>enemy.x)and\
       (plane.x+0.3*plane.image.get_width()<enemy.x+enemy.image.get_width())and\
       (plane.y+0.7*plane.image.get_height()>enemy.y)and\
       (plane.y + 0.3*plane.image.get_height()<enemy.y + enemy.image.get_height()):
        return True
    return False
        

pygame.init()
screen=pygame.display.set_mode((450,800),0,32)
pygame.display.set_caption('Hello,World!')
background=pygame.image.load('back.jpg').convert()
plane=Plane()
bullets=[]
for i in range(5):
    bullets.append(Bullet())
count_b=len(bullets)
index_b=0
interval_b=0

enemies=[]
for i in range(5):
    enemies.append(Enemy())
gameover=False
score=0
score_max=0
font=pygame.font.Font(None,32)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        if gameover and event.type==pygame.MOUSEBUTTONDOWN:
            plane.restart()
            for e in enemies:
                e.restart()
            for b in bullets:
                b.active=False
            score=0
            gameover=False
    screen.blit(background,(0,0))
    if not gameover:
        interval_b-=1
        if interval_b<0:
            bullets[index_b].restart()
            interval_b=100
            index_b=(index_b+1)%count_b

        for b in bullets:
            if b.active:
                for e in enemies:
                    if checkHit(e,b):
                        score+=100
                b.move()
                screen.blit(b.image,(b.x,b.y))
        for e in enemies:
            if checkCrash(e,plane):
                gameover=True
            e.move()
            screen.blit(e.image,(e.x,e.y))
        plane.move()
        screen.blit(plane.image,(plane.x,plane.y))
        text = font.render("Score: %d"%score,1,(0,0,0))
        screen.blit(text,(0,0))
    else:
        f=open('game_score.txt')
        score_max=f.read()
        Score_max=int(score_max)
        f.close()
        if score>Score_max:
            Score_max=score
            score_Max=str(Score_max)
            f=open('game_score.txt','w')
            f.write(score_Max)
            f.close()
        
        text = font.render("Score: %d"%score,1,(0,0,0))
        text1 = font.render("Score_max: %d"%Score_max,1,(0,0,0))
        screen.blit(text,(170,400))
        screen.blit(text1,(150,380))
    pygame.display.update()
