import sys
import random
import pygame
pygame.init()
def melee(screen: pygame.Surface) -> int:
    font=pygame.font.Font(None, 64)

    rozliseni_okna = (1080, 720)
    save=[]
    soubor = open('data.txt', 'r', encoding = 'utf-8')
    for radek in soubor:
        slovo=radek[:-1]
        save.append(int(slovo))
    soubor.close()
    nahore=[]
    vpravo=[]
    vlevo=[]
    timer=100
    timer2=0
    a=0
    score=0
    rotace=False 
    rychlost=rozliseni_okna[0]/500*3
    okno = pygame.display.set_mode(rozliseni_okna)
    pozadi=pygame.image.load("sprites/pozadi.png")
    hrac=pygame.image.load("sprites/hrac.png")
    hvezda=pygame.image.load("sprites/star.png")
    jabko=pygame.image.load("sprites/apple.png")
    uder=pygame.image.load("sprites/uder.png")
    kruh=pygame.image.load("sprites/kruh.png")
    uder=pygame.transform.scale(uder,(200,200))
    hrac=pygame.transform.scale(hrac,(100,100))
    uder_nahoru=pygame.transform.rotate(uder,90)
    uder_vlevo=pygame.transform.flip(uder,True ,False )
    clock = pygame.time.Clock()
    while True:
        okno.blit(pozadi,(0,0))
        for udalost in pygame.event.get():
            if udalost.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        stisknute_klavesy = pygame.key.get_pressed()
        if timer<0:
            a=random.randint(1,3)
            if a==1:
                vlevo.append(100)
            elif a==2:
                nahore.append(100)
            else:
                vpravo.append(100)
            timer=1000/(score+20)
        else:
            timer-=1
        a=0
        while a!= len(nahore):
            nahore[a]-=1
            if nahore[a]==0:
                if score>save[19]:
                    save[19]=score
                save[11]+=score
                score=0
                nahore.remove(0)
                a-=1
            a+=1
        a=0
        while a!= len(vpravo):
            vpravo[a]=vpravo[a]-1
            if vpravo[a]==0:
                if score>save[19]:
                    save[19]=score
                save[11]+=score
                score=0
                vpravo.remove(0)
                a-=1
            a+=1
        a=0
        while a!= len(vlevo):
            vlevo[a]=vlevo[a]-1
            if vlevo[a]==0:
                if score>save[19]:
                    save[19]=score
                save[11]+=score
                score=0
                vlevo.remove(0)
                a-=1
            a+=1
        a=0
        if timer2==0:
            if stisknute_klavesy[pygame.K_UP]:
                timer2=10
                if not rotace:
                    uder_nahoru=pygame.transform.flip(uder_nahoru,True,False)
                    okno.blit(uder_nahoru,(rozliseni_okna[0]/2-40, rozliseni_okna[1]*2/3-230))
                    uder_nahoru=pygame.transform.flip(uder_nahoru,True,False)
                else:
                    okno.blit(uder_nahoru,(rozliseni_okna[0]/2-140, rozliseni_okna[1]*2/3-230))
                while len(nahore)!=0:
                    if nahore[0]<20:
                        #if 19>nahore[0]>17:
                         #   score+=1
                        score+=1
                        nahore.remove(nahore[0])
                    else:
                        break 
            elif stisknute_klavesy[pygame.K_RIGHT]:
                timer2=10
                okno.blit(uder,(rozliseni_okna[0]/2+30, rozliseni_okna[1]*2/3-170))
                rotace=False
                while len(vpravo)!=0:
                    if vpravo[0]<20:
                        if 19>vpravo[0]>17:
                            score+=1
                        score+=1
                        vpravo.remove(vpravo[0])
                    else:
                        break 
            elif stisknute_klavesy[pygame.K_LEFT]:
                timer2=10
                okno.blit(uder_vlevo,(rozliseni_okna[0]/2-170, rozliseni_okna[1]*2/3-170))
                rotace=True
                a=0
                while len(vlevo)!=0:
                    if vlevo[a]<20:
                        if 19>vlevo[0]>17:
                            score+=1
                        score+=1
                        vlevo.remove(vlevo[0])
                    else:
                        break
        else:
            timer2-=1
            
            
        mys=pygame.mouse.get_pos()
        if (pygame.mouse.get_pressed()[0] and mys[0]<100 and mys[1]<100) or stisknute_klavesy[pygame.K_ESCAPE]:#ukonceni minihry
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


       
       
        #okno.blit(kruh,(418,432))
        #okno.blit(kruh,(680,432))
        #okno.blit(kruh,(418,432))
        a=0
        while a!=len(nahore):
            okno.blit(jabko,(rozliseni_okna[0]/2,-nahore[a]*rychlost+rozliseni_okna[1]*2/3-70))
            a+=1
        a=0
        while a!=len(vpravo):
            okno.blit(jabko,((vpravo[a]+90)*rychlost-30,rozliseni_okna[1]/5*3))
            a+=1
        a=0
        while a!=len(vlevo):
            okno.blit(jabko,((100-vlevo[a])*rychlost-100,rozliseni_okna[1]/5*3))
            a+=1
        a=0
        text=font.render(str(score),True ,(0,0,0))#score
        okno.blit(text,(900,120))
        if rotace:
            hrac=pygame.transform.flip(hrac,True,False)
            okno.blit(hrac,(rozliseni_okna[0]/2-25, rozliseni_okna[1]*2/3-70))
            hrac=pygame.transform.flip(hrac,True,False)
        else:
            okno.blit(hrac,(rozliseni_okna[0]/2-40, rozliseni_okna[1]*2/3-70))
        
        pygame.display.update()
        clock.tick(60)











