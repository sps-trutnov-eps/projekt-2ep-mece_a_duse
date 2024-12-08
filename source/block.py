import sys
import random
import pygame
import math

pygame.init()
def block(screen: pygame.Surface) -> int:
    font=pygame.font.Font(None, 64)
    jabka=[]
    rozliseni_okna = (1080, 720)
    soubor = open('data.txt', 'r', encoding = 'utf-8')
    save=[]
    for radek in soubor:
        slovo=radek[:-1]
        save.append(int(slovo))
    soubor.close()
    score=0
    a=0
    b=0
    c=0
    d=0
    timer=0
    veci=8
    x=0
    tisk=0
    region=0
    e=[]
    posun=[int(rozliseni_okna[0]//2),int(rozliseni_okna[1]//2)]
    okno = pygame.display.set_mode(rozliseni_okna)
    pozadi=pygame.image.load("sprites/pozadi.png")
    hrac=pygame.image.load("sprites/hrac sam.png")
    hvezda=pygame.image.load("sprites/star.png")
    jabko=pygame.image.load("sprites/apple.png")
    stit=pygame.image.load("sprites/stit.png")
    hrac=pygame.transform.scale(hrac,(100,100))
    stit=pygame.transform.scale(stit,(64,64))
    clock = pygame.time.Clock()
    stit_rotated=stit
    image_rect = stit.get_rect(center=(0, 0))
    while True:
        okno.blit(pozadi,(0,0))
        for udalost in pygame.event.get():
            if udalost.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        stisknute_klavesy = pygame.key.get_pressed()
        
        timer-=1
        if timer<0:#vytváření jablek
            e=[]
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
            e.append(a)
            e.append(b)#jabka[pozice x, pozice y, uhel, rychlos x, rychlost y, cas, hvezda, region]
            if b==0:
                e.append(math.atan(a/0.1))
            else:
                e.append(math.atan(a/b))
            e.append(a/c*3)
            e.append(b/c*3)
            if a==0:
                e.append(b/(b/c*3))
            else:
                e.append(a/(a/c*3))
            if random.randint(0,10)==1:
                e.append(True)
                a=0
            else:
                e.append(False)
                a=0
            if e[-4]>0:
                a+=2
            if e[-3]<0:
                a+=1
            e.append(a)
            #print(e)
            jabka.append(e)
            #print(jabka)
        a=0
        while a<len(jabka):#pohyb jablek
            jabka[a][0]-=jabka[a][3]
            jabka[a][1]-=jabka[a][4]
            jabka[a][5]-=1
            a+=1
        a=0
        if stisknute_klavesy[pygame.K_s]:#vymaže všechny jabka
            jabka=[]
        
        
        mys=pygame.mouse.get_pos()#vypočítávání kam dát štít
        mys=mys[0]-posun[0],mys[1]-posun[1]
        a=(mys[0]**2+mys[1]**2)**0.5
        a=a/50
        pozice=mys[0]/a,mys[1]/a
        if pozice[1]!=0:
            d=math.atan(pozice[0]/pozice[1])
        a=0    
        #a=len(jabka)
        
        
        region=0
        if mys[1]!=0:
            if mys[0]>0:
                region+=2
            if mys[1]<0:
                region+=1
            #print(region)
            image_rect = stit.get_rect(center=(pozice[0]+posun[0],pozice[1]+posun[1]))#rotace a vykreslování štítu
            rotated_rect = stit_rotated.get_rect(center=image_rect.center)
            if region==0:
                stit_rotated=pygame.transform.rotate(stit,-d*60)
                stit_rotated=pygame.transform.flip(stit_rotated,True,False)
            elif region==1:
                stit_rotated=pygame.transform.rotate(stit,-d*60)
                stit_rotated=pygame.transform.flip(stit_rotated,False,True)
            elif region==2:
                stit_rotated=pygame.transform.rotate(stit,d*60-180)
            else:
                stit_rotated=pygame.transform.rotate(stit,d*60)
            stit_rotated=pygame.transform.rotate(stit_rotated,90)
            
            
        if mys[0]<0:#vykreslování hráče
            hrac=pygame.transform.flip(hrac,True,False)
            okno.blit(hrac,(rozliseni_okna[0]/2-50, rozliseni_okna[1]/2-50))
            hrac=pygame.transform.flip(hrac,True,False)
        else:
            okno.blit(hrac,(rozliseni_okna[0]/2-50, rozliseni_okna[1]/2-50))
        if stisknute_klavesy[pygame.K_a] and timer%10==0:
            print(region)
            print(d)
        while a<len(jabka):#detekce trefení jablek
            if jabka[a][5]<-40:
                jabka.remove(jabka[a])
            elif -5<jabka[a][5]<0:
                if jabka[a][6]:
                    score+=2
                else:
                    if score>save[20]:
                        save[20]=score
                    save[12]+=score
                    save[13]+=score
                    score=0
                b=0
                jabka.remove(jabka[a])
            elif jabka[a][5]<25:
                if d-0.5<jabka[a][2]<d+0.5 or d-0.5<jabka[a][2]-3<d+0.5 or d-0.5<jabka[a][2]+3<d+0.5:
                    if abs(jabka[a][2])>0.75:
                        x=1
                    else:
                        x=2
                    
                    if jabka[a][7]==3:
                        x*=-1
                    elif jabka[a][7]==2 and x==2:
                        x*=-1
                    elif jabka[a][7]==1 and x==1:
                        x*=-1
                        
                    
                    if jabka[a][5]>0 and (jabka[a][7]==region or jabka[a][7]+x==region):
                        #print(jabka[a][2])
                        b=0
                        if jabka[a][6]==False:
                            score+=1
                        jabka[a][3]*=-1
                        jabka[a][4]*=-1
                        jabka[a][5]*=-1
                        
                        
                    #else:
                     #   print(jabka[a][2])
                      #  print("jabka reg ",jabka[a][7])
                       # print("x ",x)
                        #print(region)
            a+=1
        #print(d)
            
            
            
        if (pygame.mouse.get_pressed()[0] and mys[0]<100-posun[0] and mys[1]<100-posun[1]) or stisknute_klavesy[pygame.K_ESCAPE]:#ukonceni minihry
            print("konec")        
            with open("data.txt", "r") as file:
                lines = file.readlines()
                
            #print(len(lines))
            a=0
            while a!=len(save):
                lines[a]=str(save[a])+"\n"
                a+=1
                
            with open("data.txt", "w") as file:
                file.writelines(lines)
            return 3
            
            
        text=font.render(str(score),True ,(0,0,0))#score
        okno.blit(text,(900,120))
        a=0
        while a<len(jabka):#vykreslování jablek
            if jabka[a][6]==False:
                okno.blit(jabko,(jabka[a][0]+posun[0]-16,jabka[a][1]+posun[1]-16))
            else:
                okno.blit(hvezda,(jabka[a][0]+posun[0]-16,jabka[a][1]+posun[1]-16))
            a+=1
        a=0
        okno.blit(stit_rotated, rotated_rect.topleft)
        #pygame.draw.rect(okno,(0,0,0),(posun[0]+pozice[0],posun[1]+pozice[1],10,10))
        pygame.display.update()
        clock.tick(60)












