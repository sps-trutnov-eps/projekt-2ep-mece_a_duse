import sys
import random
import pygame
import math

pygame.init()
font=pygame.font.Font(None, 64)
jabka=[]
rozliseni_okna = (1080, 720)
score=0
a=0
b=0
c=0
d=0
timer=0
veci=6
x=0.5
tisk=0
posun=[rozliseni_okna[0]/2,rozliseni_okna[1]/2]
okno = pygame.display.set_mode(rozliseni_okna)
pozadi=pygame.image.load("sprites/pozadi.png")
hrac=pygame.image.load("sprites/hrac.png")
hvezda=pygame.image.load("sprites/star.png")
jabko=pygame.image.load("sprites/apple.png")
hrac=pygame.transform.scale(hrac,(100,100))
clock = pygame.time.Clock()
fps = 60
while True:
    okno.blit(pozadi,(0,0))
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    stisknute_klavesy = pygame.key.get_pressed()
    
    
    timer-=1
    if timer<0:
        timer=1000/(score+20)
        d=random.randint(0,3)
        if d==0:
            a=-posun[0]-50
            b=random.randint(-posun[0],posun[0])
        elif d==1:
            a=random.randint(-posun[0],posun[0])
            b=posun[0]+50
        elif d==2:
            a=posun[0]+50
            b=random.randint(-posun[0],posun[0])
        else:
            a=random.randint(-posun[0],posun[0])
            b=-posun[0]-50
        c=(a**2+b**2)**0.5
        jabka.append(a)
        jabka.append(b)
        if b==0:
            jabka.append(math.atan(a/0.1))
        else:
            jabka.append(math.atan(a/b))
        jabka.append(a/c*3)
        jabka.append(b/c*3)
        if a==0:
            jabka.append(b/(b/c*3))
        else:
            jabka.append(a/(a/c*3))
        #print(jabka)
    a=0
    while a<len(jabka):
        jabka[a]-=jabka[a+3]
        jabka[a+1]-=jabka[a+4]
        jabka[a+5]-=1
        a+=veci
    a=0
    if stisknute_klavesy[pygame.K_s]:
        jabka=[]
    
    
    mys=pygame.mouse.get_pos()
    mys=mys[0]-posun[0],mys[1]-posun[1]
    a=(mys[0]**2+mys[1]**2)**0.5
    a=a/100
    pozice=mys[0]/a,mys[1]/a
    if pozice[1]!=0:
        d=math.atan(pozice[0]/pozice[1])
    if tisk==1:
        if pozice[1]!=0:
            print(d)
        if len(jabka)!=0:
            print(jabka[2])
    a=0    
    #a=len(jabka)
    while a<len(jabka):
        if jabka[a+5]<0:
            score=0
            b=0
            while b != veci:
                jabka.remove(jabka[a])
                b+=1
        elif 20<jabka[a+5]<40:
            if d-x<jabka[a+2]<d+x or d-x<jabka[a+2]-3<d+x or d-x<jabka[a+2]+3<d+x:
                #print(jabka[a+2])
                b=0
                score+=1
                while b != veci:
                    jabka.remove(jabka[a])
                    b+=1
        a+=veci
    
    
    
    
    
    text=font.render(str(score),True ,(0,0,0))
    okno.blit(text,(150,100))
    okno.blit(hrac,(rozliseni_okna[0]/2-50, rozliseni_okna[1]/2-50))
    a=0
    while a<len(jabka):
        okno.blit(jabko,(jabka[a]+posun[0]-16,jabka[a+1]+posun[1]-16))
        a+=veci
    a=0
    pygame.draw.rect(okno,(0,0,0),(posun[0]+pozice[0],posun[1]+pozice[1],10,10))
    pygame.display.update()
    clock.tick(fps)












