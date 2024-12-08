import pygame
import random
import sys
import math
pygame.init()
def arena(screen: pygame.Surface) -> int:
    SCREEN_RESOLUTION=[1080,720]
    """
    Display the level menu and handle user interaction.

    Args:
        screen (pygame.Surface): The surface to draw the menu on.

    Returns:
        int: The 0 to return to the main menu or 9 if the window is closed.
    """
    pygame.display.set_caption('Meče & Duše: Nekonečná Aréna')
    button_texts = ['', 'Exit']
    screen_width = SCREEN_RESOLUTION[0] // 2
    screen_height = SCREEN_RESOLUTION[1] // 2 - (64 * (len(button_texts) // 2))
    #buttons = [
    #    Button(text, screen_width, screen_height + i * 64)
    #    for i, text in enumerate(button_texts)
    #]
    screen = pygame.display.set_mode(SCREEN_RESOLUTION)
    clock = pygame.time.Clock()
    hrac=pygame.image.load("sprites/hrac.png")
    pozadi=pygame.image.load("sprites/arena.png")
    hrac_luk=pygame.image.load("sprites/hrac s lukem.png")
    sip=pygame.image.load("sprites/šíp.png")
    bar=pygame.image.load("sprites/arena-bar.png")
    zamek=pygame.image.load("sprites/zámek.png")
    icony=[pygame.image.load("sprites/icona lebka.png")]
    icony.append(pygame.image.load("sprites/icona meč.png"))
    icony.append(pygame.image.load("sprites/icona omráčení.png"))
    icony.append(pygame.image.load("sprites/icona rdce.png"))
    icony.append(pygame.image.load("sprites/icona štít.png"))
    uder=pygame.image.load("sprites/uder2.png")
    potion=pygame.image.load("sprites/potion.png")
    coin=pygame.image.load("sprites/coin.png")
    save=[]
    soubor = open('data.txt', 'r', encoding = 'utf-8')
    for radek in soubor:
        slovo=radek[:-1]
        save.append(int(slovo))
    soubor.close()
    #print(save)
    hrac_luk=pygame.transform.scale(hrac_luk,(150,150))
    sip=pygame.transform.scale(sip,(100,100))
    hrac=pygame.transform.scale(hrac,(150,150))
    enemy=pygame.transform.flip(hrac,True,False)
    utocim=True
    timer=0
    hrac_x=SCREEN_RESOLUTION[0]/3-160
    enemy_x=SCREEN_RESOLUTION[0]*2/3
    hrac_max_zivoty=save[12]
    uroven=save[23]
    enemaci=[uroven*10,uroven*10+2,uroven*10+4,uroven*10+6,uroven*10+10]
    porazeno=0

    enemy_max_zivoty=enemaci[porazeno]**2
    enemy_zivoty=enemy_max_zivoty
    enemy_demage=round(enemaci[porazeno]**1.4)+1
    enemy_demage=enemy_demage-enemy_demage/10*save[4]


    hrac_zivoty=hrac_max_zivoty
    hrac_demage=save[11]
    schopnosti=[0,0,0,0,0,0,0]

    shield=1-save[5]/10
    luk=round(math.log(save[14])*5,0)#  %
    stit=round(math.log(save[13])*5,0)
    luk_demage=save[14]*save[6]
    smer=5
    priste=0
    a=0
    b=0
    c=0
    dodge=round(math.log(save[15]*5))
    hrac_demage=hrac_demage*save[3]
    buff=[0,0,0,0,0]#stun,heal,sheild,poison,strenght
    #potion#demageboost,heal,cooldowrecharg,shield

    porazeno=0
    #uder mece
    def mec(a,b,uder,screen):#hráč=True, priste,uder,screen
        #print("uder")
        if a:
            d=740
            if b==0:
                c=1
            elif b==1:
                c=2
            elif b==3:
                c=1
            elif b==7:
                c=10
            else:
                return
        else:
            uder=pygame.transform.flip(uder,True,False)
            c=1
            d=270
        c*=5
        b=0
        while c!=0:
            sprite_rect = uder.get_rect(center=(d+random.randint(0,70), 400+random.randint(-20,50)))
            if c%5==0:
                uder_rotated=pygame.transform.rotate(uder,random.randint(-60,60))
                rotated_rect = uder_rotated.get_rect(center=sprite_rect.center)
                screen.blit(uder_rotated, rotated_rect.topleft)
            pygame.display.update()
            clock.tick(60)
            c-=1
    def stiit(stit,screen):
        stit=pygame.transform.scale(stit,(150,150))
        screen.blit(stit,(200,360))
        a=10
        while a>0:
            a-=1
            pygame.display.update()
            clock.tick(60)

    font=pygame.font.Font(None, 40)
    pop=[0,0,0,0,0,0]#enemy dem t,hrac dem t,poison dem t

    font2=pygame.font.Font(None, 20)
    while True:
        mys=pygame.mouse.get_pos()
        for udalost in pygame.event.get():
            if udalost.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif udalost.type == pygame.MOUSEBUTTONUP and mys[1]>680:
                if 150<mys[0]<190 and save[7]!=0:
                        save[7]-=1
                        buff[4]+=10#bonus demage
                elif 190<mys[0]<230 and save[8]!=0:
                    save[8]-=1
                    hrac_zivoty=hrac_max_zivoty#heal
                elif 230<mys[0]<270 and save[9]!=0:
                    save[9]-=1
                    a=0
                    while a!=len(schopnosti):#charge
                        schopnosti[a]=0
                        a+=1
                elif 270<mys[0]<310 and save[10]!=0:
                    save[10]-=1
                    buff[2]+=10#shield
                #return 10
            #for i, button in enumerate(buttons):
             #   if button.handle_event(event):
              #      pass
        stisknute_klavesy = pygame.key.get_pressed()
        timer+=1
        if utocim and smer!=0:
            #print("a")
            if 199<hrac_x<500:#pohyb hrace
                #print("b")
                screen.blit(pozadi,(0,0))
                if hrac_x==200 and smer==5:
                    if luk>random.randint(0,100):
                        hrac_x+=smer
                        smer=0
                hrac_x+=smer
                timer=0
            else:
                if timer<2 and hrac_x>400:
                    #print("mozna")
                    mec(True,priste,uder,screen) #animace
                    screen.blit(pozadi,(0,0))
                else:
                    if hrac_x<400:
                        #print("otocka")
                        utocim=False
                        hrac_x=200
                    else:
                        #print("demage")
                        if priste!=4 and priste!=5 and priste!=6:
                            pop[3]=60
                        if buff[4]!=0:
                            hrac_demage=hrac_demage*2
                        if priste==0:#utok
                            enemy_zivoty-=hrac_demage
                            save[16]+=hrac_demage
                            pop[2]=hrac_demage
                        if priste==1:#double utok
                            enemy_zivoty-=hrac_demage*2
                            save[16]+=hrac_demage*2
                            pop[2]=hrac_demage*2
                        elif priste==2:#shiel utok
                            buff[0]=5
                            pop[2]="bonk"
                        elif priste==3:#poison
                            enemy_zivoty-=hrac_demage/2
                            save[16]+=hrac_demage/2
                            pop[2]=hrac_demage/2
                            buff[3]+=1
                        elif priste==4:#heal
                            hrac_zivoty+=hrac_max_zivoty/4
                            if hrac_zivoty>hrac_max_zivoty:
                                hrac_zivoty=hrac_max_zivoty
                        elif priste==5:#shield
                            buff[2]=5
                        elif priste==6:#heal2
                            buff[1]=5
                        elif priste==7:#super utok
                            enemy_zivoty-=hrac_demage*10
                            save[16]+=hrac_demage*10
                            pop[2]=hrac_demage*10
                        smer=smer*-1
                        hrac_x+=smer
                        hrac_x+=smer
                        priste=0
                        a=0
                        while a<7:
                            if schopnosti[a]!=0:
                                schopnosti[a]-=1
                            a+=1
                        a=0
                        if buff[4]!=0:
                            hrac_demage=hrac_demage/2
                        if buff[3]>0:
                            enemy_zivoty-=hrac_demage*buff[3]/4
                            save[16]+=hrac_demage*buff[3]/4
                            pop[4]=hrac_demage*buff[3]/4
                            pop[5]=60
                        else:
                            pop[4]=0
                        while a<len(buff)-1:
                            if buff[a]!=0 and a!=3:
                                buff[a]-=1
                            a+=1
                        a=0
                        #print("uder h")

        elif buff[0]!=0:
            #print("spravna otocka")
            #print(hrac_x,utocim,smer)
            smer*=-1
            utocim=True
        elif not utocim:#pohyb nepritele
             #print("taddy")
             if 721>enemy_x>400:
                 screen.blit(pozadi,(0,0))
                 enemy_x+=smer
                 timer=0
             else:
                 if timer<2 and enemy_x<600:
                     mec(utocim,0,uder,screen)#animace enemy
                     if random.randint(0,100)<stit:
                         b=1
                     else:
                         screen.blit(pozadi,(0,0))
                 if enemy_x>600:
                    utocim=True
                    enemy_x-=smer
                 else:
                    pop[1]=60
                    if random.randint(0,100)<dodge:
                        #print("dodge")
                        c=20
                        pop[0]=0
                    elif buff[1]>0:
                        hrac_zivoty+=enemy_demage
                        pop[0]=-enemy_demage
                    else:
                        if buff[2]>0:#pocitani demage
                            hrac_zivoty-=enemy_demage/5
                            pop[0]=enemy_demage/5
                        elif b==1:
                            stiit(icony[4],screen)
                            hrac_zivoty-=enemy_demage/shield
                            pop[0]=enemy_demage/shield
                            #print("block")
                        else:
                            hrac_zivoty-=enemy_demage
                            pop[0]+=enemy_demage
                    if hrac_zivoty>hrac_max_zivoty:
                        hrac_zivoty=hrac_max_zivoty
                        
                    #print("uder e")
                    smer=smer*-1
                    enemy_x+=smer
        if smer==0:#střelba z luku
            #print("strelba")
            screen.blit(pozadi,(0,0))
            if timer<30:
                screen.blit(hrac_luk,(200,SCREEN_RESOLUTION[1]/2))
            elif timer<50:
                screen.blit(sip,(timer*20-250,SCREEN_RESOLUTION[1]/2))
            else:
                enemy_zivoty-=luk_demage
                pop[3]=10
                pop[2]=luk_demage
                smer=5
        if c>1:
            c-=1
            hrac_x=100
        elif c==1:
            c-=1   
            hrac_x=201
        else:
            pass
            
                

        if stisknute_klavesy[pygame.K_1] or (pygame.mouse.get_pressed()[0] and mys[1]>650 and 330<mys[0]<400):#aktivace specialních utoků
            if schopnosti[0]==0 and priste==0:
                schopnosti[0]=5#double_demage
                priste=1
        elif stisknute_klavesy[pygame.K_2] or (pygame.mouse.get_pressed()[0] and mys[1]>650 and 400<mys[0]<470):
            if schopnosti[1]==0 and priste==0 and save[1]>=10:
                schopnosti[1]=10#stun
                priste=2
        elif stisknute_klavesy[pygame.K_3] or (pygame.mouse.get_pressed()[0] and mys[1]>650 and 470<mys[0]<540):
            if schopnosti[2]==0 and priste==0 and save[1]>=20:
                schopnosti[2]=10#poison
                priste=3
        elif stisknute_klavesy[pygame.K_4] or (pygame.mouse.get_pressed()[0] and mys[1]>650 and 540<mys[0]<610):
            if schopnosti[3]==0 and priste==0 and save[1]>=30:
                schopnosti[3]=20#heal
                priste=4
        elif stisknute_klavesy[pygame.K_5] or (pygame.mouse.get_pressed()[0] and mys[1]>650 and 610<mys[0]<680):
            if schopnosti[4]==0 and priste==0 and save[1]>=40:
                schopnosti[4]=20#shield
                priste=5
        elif stisknute_klavesy[pygame.K_6] or (pygame.mouse.get_pressed()[0] and mys[1]>650 and 680<mys[0]<750):
            if schopnosti[5]==0 and priste==0 and save[1]>=50:
                schopnosti[5]=30#heal2
                priste=6
        elif stisknute_klavesy[pygame.K_7] or (pygame.mouse.get_pressed()[0] and mys[1]>650 and 750<mys[0]<820):
            if schopnosti[6]==0 and priste==0 and save[1]>=60:
                schopnosti[6]=30#superdeamge
                priste=7
                

                
        


        a=0
        if hrac_x<205 and enemy_x>715:
            if hrac_zivoty<0:
                a=1
                save[18]+=1
                #print("prohra")
            elif enemy_zivoty<0:
                porazeno+=1
                save[17]+=1
                if porazeno>len(enemaci)-1:
                    save[23]+=1
                    a=1
                    #print("výhra")
                else:
                    #print("porazil jsi jednoho")
                    buff[0]=0
                    buff[3]=0
                    save[0]+=random.randint(0,uroven*2)+uroven#novy nepritel
                    save[2]+=random.randint(0,round(100+1.5**save[23],0))
                    if save[2]>100+1.5**save[1]/2:
                        save[2]-=round(100+1.5**save[1]/2,0)
                        save[2]=int(save[2])
                        save[1]+=1
                    enemy_max_zivoty=enemaci[porazeno]**2
                    enemy_zivoty=enemy_max_zivoty
                    enemy_demage=round(enemaci[porazeno]**1.4)+1
                    enemy_demage=enemy_demage-enemy_demage/10*save[4]
                    utocim=True
                    smer*=-1
                    
        
        if (pygame.mouse.get_pressed()[0] and mys[0]<100 and mys[1]<100) or a==1 or stisknute_klavesy[pygame.K_ESCAPE]:#ukonceni areny
            #print("konec")        
            with open("data.txt", "r") as file:
                lines = file.readlines()
                
            #print(len(lines))
            a=0
            while a!=len(save):
                lines[a]=str(save[a])+"\n"
                a+=1
                
            with open("data.txt", "w") as file:
                file.writelines(lines)
            return 0
        a=0
        
        
        
        

        hrac_zivoty=round(hrac_zivoty,1)
        enemy_zivoty=round(enemy_zivoty,1)
        pop[0]=round(pop[0],1)
        if pop[2]==int:
            pop[2]=round(pop[2],1)
        pop[4]=int(round(pop[4],0))
        if pop[1]!=0:
            if pop[0]<0:
                text=font.render("+"+str(-pop[0]), True, (0, 0, 0))
            else:
                text=font.render(str(pop[0]), True, (0, 0, 0))
            screen.blit(text, (250-2,300-2+pop[1]))
            screen.blit(text, (250+2,300-2+pop[1]))
            screen.blit(text, (250-2,300+2+pop[1]))
            screen.blit(text, (250+2,300+2+pop[1]))
            if pop[0]<0:
                text=font.render("+"+str(-pop[0]), True, (255, 255, 255))
            else:
                text=font.render(str(pop[0]), True, (255, 255, 255))
            screen.blit(text, (250,300+pop[1]))
            
            pop[1]-=1
        elif pop[3]!=0:
            text=font.render(str(pop[2]), True, (0, 0, 0))
            screen.blit(text, (750-2,300-2+pop[3]))
            screen.blit(text, (750+2,300-2+pop[3]))
            screen.blit(text, (750-2,300+2+pop[3]))
            screen.blit(text, (750+2,300+2+pop[3]))
            text=font.render(str(pop[2]), True, (255, 255, 255))
            screen.blit(text, (750,300+pop[3]))
            pop[3]-=1
        if pop[5]!=0:
            text=font.render(str(pop[4]), True, (0, 255, 0))
            screen.blit(text, (850-2,300-2+pop[5]))
            screen.blit(text, (850+2,300-2+pop[5]))
            screen.blit(text, (850-2,300+2+pop[5]))
            screen.blit(text, (850+2,300+2+pop[5]))
            text=font.render(str(pop[4]), True, (255, 255, 255))
            screen.blit(text, (850,300+pop[5]))
            pop[5]-=1





        a=0
        screen.blit(bar,(SCREEN_RESOLUTION[0]/2-210,SCREEN_RESOLUTION[1]-70))#vykreslovani
        while a<70:
            if save[1]<a:
                screen.blit(zamek,(SCREEN_RESOLUTION[0]/2-210+a*7,SCREEN_RESOLUTION[1]-70))
            else:
                if schopnosti[int(a/10)]!=0:
                    pygame.draw.rect(screen,(0,0,0),(SCREEN_RESOLUTION[0]/2-210+a*7,SCREEN_RESOLUTION[1]-70,70,70))
                    text=font.render(str(schopnosti[int(a/10)]),True,(255,255,255))
                    screen.blit(text,(SCREEN_RESOLUTION[0]/2-185+a*7,SCREEN_RESOLUTION[1]-45))
            a+=10
        
        screen.blit(potion,(150,660))
        a=0
        while a<4:
            text=font.render(str(save[7+a]), True, (0,0,0))
            screen.blit(text,(170+a*40,680))
            a+=1
        
        
        if buff[0]>0:
            screen.blit(icony[2],(890,520))
            text=font2.render(str(buff[0]),True,(0,0,0))
            screen.blit(text,(920,550))
        if buff[1]>0:
            screen.blit(icony[3],(430,520))
            text=font2.render(str(buff[1]),True,(0,0,0))
            screen.blit(text,(460,550))
        if buff[2]>0:
            screen.blit(icony[4],(390,520))
            text=font2.render(str(buff[2]),True,(0,0,0))
            screen.blit(text,(420,550))
        if buff[3]>0:
            screen.blit(icony[0],(850,520))
            text=font2.render(str(buff[3]),True,(0,0,0))
            screen.blit(text,(880,550))
        if buff[4]>0:
            screen.blit(icony[1],(350,520))
            text=font2.render(str(buff[4]),True,(0,0,0))
            screen.blit(text,(380,550))
        
        
        pygame.draw.rect(screen,(255,0,0),(200,SCREEN_RESOLUTION[1]/4*3,hrac_zivoty/hrac_max_zivoty*150,10))
        pygame.draw.rect(screen,(255,0,0),(700,SCREEN_RESOLUTION[1]/4*3,enemy_zivoty/enemy_max_zivoty*150,10))
        text=font2.render(str(hrac_zivoty)+"/"+str(hrac_max_zivoty), True, (0,0,0))
        screen.blit(text, (250,SCREEN_RESOLUTION[1]/4*3))
        text=font2.render(str(enemy_zivoty)+"/"+str(enemy_max_zivoty), True, (0,0,0))
        screen.blit(text, (750,SCREEN_RESOLUTION[1]/4*3))
        a=save[0]
        b=0
        if a>1000:
            while a>10:
                a/=10
                a=round(a,3)
                b+=1
            text=font.render(str(a)+"E"+str(b), True, (0,0,0))
        else:
            text=font.render(str(a), True, (0,0,0))
        screen.blit(text,(SCREEN_RESOLUTION[0]-150,SCREEN_RESOLUTION[1]-40))
        screen.blit(coin,(SCREEN_RESOLUTION[0]-50,SCREEN_RESOLUTION[1]-50))
        pygame.draw.rect(screen,(0,0,0),(330,SCREEN_RESOLUTION[1]-110,490,30))
        pygame.draw.rect(screen,(0,0,200),(330,SCREEN_RESOLUTION[1]-110,save[2]/(100+1.5**save[1]/2)*490,30))
        text=font.render(str(save[1]), True, (255,255,255))
        screen.blit(text,(SCREEN_RESOLUTION[0]/2,SCREEN_RESOLUTION[1]-105))
        text=font.render("boj: "+str(save[23]),True,(0,0,0))
        screen.blit(text,(480,64))
        if smer!=0 or timer>30:
            screen.blit(hrac,(hrac_x,SCREEN_RESOLUTION[1]/2))
        screen.blit(enemy,(enemy_x,SCREEN_RESOLUTION[1]/2))
        pygame.display.update()
        clock.tick(60)
        






        


