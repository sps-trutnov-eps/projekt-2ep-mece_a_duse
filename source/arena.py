import pygame
import random
import sys
import math
pygame.init()
#def arena(screen: pygame.Surface) -> int:
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
fps = 60
hrac=pygame.image.load("sprites/hrac.png")
enemy=pygame.image.load("sprites/hrac sam.png")
pozadi=pygame.image.load("sprites/arena.png")
hrac_luk=pygame.image.load("sprites\hrac s lukem.png")
sip=pygame.image.load("sprites\šíp.png")
save=[]
soubor = open('data.txt', 'r', encoding = 'utf-8')
for radek in soubor:
    slovo=radek[:-1]
    save.append(int(slovo))
soubor.close()
print(save)
hrac_luk=pygame.transform.scale(hrac_luk,(150,150))
sip=pygame.transform.scale(sip,(100,100))
enemy=pygame.transform.scale(enemy,(150,150))
enemy=pygame.transform.flip(enemy,True,False)
hrac=pygame.transform.scale(hrac,(150,150))
utocim=True
timer=0
hrac_x=SCREEN_RESOLUTION[0]/3-160
enemy_x=SCREEN_RESOLUTION[0]*2/3
hrac_max_zivoty=save[12]
uroven=save[23]
enemaci=[uroven*10,uroven*10+2,uroven*10+4,uroven*10+6,uroven*10+10]
porazeno=0

enemy_max_zivoty=enemaci[porazeno]*2
enemy_zivoty=enemy_max_zivoty
enemy_demage=round(enemaci[porazeno]*0.4)+1
enemy_demage=enemy_demage-enemy_demage/10*save[4]


hrac_zivoty=hrac_max_zivoty
hrac_demage=save[11]
schopnosti=[0,0,0,0,0,0]
mec=save[3]
shield=1-save[5]/10
luk=round(math.log(save[14])*5,0)#  %
luk_demage=save[14]*save[6]
smer=5
priste=0
a=0
total_demage=save[16]

hrac_demage=hrac_demage*mec
buff=[0,0,0,0,0]#stun,shield,heal,poison,strenght
potion=[save[7],save[8],save[9],save[10]]#demageboost,heal,cooldowrecharg,shield

porazeno=0
total_porazeno=save[17]
money=save[0]
level=save[1]
xp=save[2]


font=pygame.font.Font(None, 40)
pop=[0,0,0,0]#enemy dem t,hrac dem t

font2=pygame.font.Font(None, 20)

while True:
    screen.blit(pozadi,(0,0))
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            #return 10
        #for i, button in enumerate(buttons):
         #   if button.handle_event(event):
          #      pass
    stisknute_klavesy = pygame.key.get_pressed()
    timer+=1
    if utocim and smer!=0:
        if 199<hrac_x<500:#pohyb hrace
            if hrac_x==200 and smer==5:
                if luk>random.randint(0,100):
                    hrac_x+=smer
                    smer=0
            hrac_x+=smer
            timer=0
        else:
            if timer<5:
                pass #animace
            else:
                if hrac_x<400:
                    utocim=False
                    hrac_x-=smer
                else:
                    pop[3]=60
                    if buff[4]!=0:
                        hrac_demage=hrac_demage*2
                    if priste==0:#urceni jaky utok udelat
                        enemy_zivoty-=hrac_demage
                        total_demage+=hrac_demage
                        pop[2]=hrac_demage
                    if priste==1:
                        enemy_zivoty-=hrac_demage*2
                        total_demage+=hrac_demage*2
                        pop[2]=hrac_demage*2
                    elif priste==2:
                        enemy_zivoty-=hrac_demage/2
                        total_demage+=hrac_demage/2
                        buff[0]=5
                        pop[2]=hrac_demage/2
                    elif priste==3:
                        hrac_zivoty+=hrac_max_zivoty/4
                        if hrac_zivoty>hrac_max_zivoty:
                            hrac_zivoty=hrac_max_zivoty
                    elif priste==4:
                        buff[2]=5
                    elif priste==5:
                        buff[3]==2
                    elif priste==6:
                        enemy_zivoty-=hrac_demage*10
                        total_demage+=hrac_demage*10
                        pop[2]=hrac_demage*10
                    smer=smer*-1
                    hrac_x+=smer
                    hrac_x+=smer
                    enemy_zivoty-=hrac_demage/4*buff[-1]
                    priste=0
                    while a<5:
                        if schopnosti[a]!=0:
                            schopnosti[a]-=1
                        a+=1
                    a=0
                    if buff[4]!=0:
                        hrac_demage=hrac_demage/2
                    while a<len(buff)-1:
                        if buff[a]!=0:
                            buff[a]-=1
                        a+=1
                    a=0
                    print("uder h")


    elif not utocim and buff[0]==0:#pohyb nepritele
         if 721>enemy_x>400:
           enemy_x+=smer
           timer=0
         else:
             if timer<5:
                 pass#animace enemy
             if enemy_x>600:
                utocim=True
                enemy_x-=smer
             else:
                 if enemy_x>600:
                    utocim=True
                    enemy_x-=smer
                 else:
                    pop[1]=60
                    if buff[3]>0:
                        hrac_zivoty+=enemy_demage
                        pop[0]=-enemy_demage
                    else:
                        if buff[2]>0:#pocitani demage
                            hrac_zivoty-=enemy_demage/5
                            pop[0]=enemy_demage/5
                        elif 1==random.randint(1,5):
                            hrac_zivoty-=enemy_demage/shield
                            pop[0]=enemy_demage/shield
                            print("block")
                        else:
                            hrac_zivoty-=enemy_demage
                            pop[0]+=enemy_demage
                    if hrac_zivoty>hrac_max_zivoty:
                        hrac_zivoty=hrac_max_zivoty
                        
                    print("uder e")
                    smer=smer*-1
                    enemy_x+=smer
    elif smer==0:
        if timer<30:
            screen.blit(hrac_luk,(200,SCREEN_RESOLUTION[1]/2))
        elif timer<50:
            screen.blit(sip,(timer*20-250,SCREEN_RESOLUTION[1]/2))
        else:
            enemy_zivoty-=luk_demage
            pop[3]=10
            pop[2]=luk_demage
            smer=5
            




    if stisknute_klavesy[pygame.K_q] and schopnosti[0]==0 and priste==0:#aktivace specialních utoků
        schopnosti[0]=5
        priste=1
    elif stisknute_klavesy[pygame.K_w] and schopnosti[1]==0 and priste==0:
        schopnosti[1]=5
        priste=2
    elif stisknute_klavesy[pygame.K_e] and schopnosti[2]==0 and priste==0:
        schopnosti[2]=5
        priste=3
    elif stisknute_klavesy[pygame.K_r] and schopnosti[3]==0 and priste==0:
        schopnosti[3]=5
        priste=4
    elif stisknute_klavesy[pygame.K_t] and schopnosti[4]==0 and priste==0:
        schopnosti[4]=5
        priste=5
    elif stisknute_klavesy[pygame.K_z] and schopnosti[5]==0 and priste==0:
        schopnosti[5]=5
        priste=6
    elif stisknute_klavesy[pygame.K_u] and schopnosti[6]==0 and priste==0:
        schopnosti[6]=5
        priste=7
    elif stisknute_klavesy[pygame.K_i] and schopnosti[7]==0 and priste==0:
        schopnosti[7]=5
        priste=8
    elif stisknute_klavesy[pygame.K_o] and schopnosti[8]==0 and priste==0:
        schopnosti[8]=5
        priste=9
    elif stisknute_klavesy[pygame.K_p] and schopnosti[9]==0 and priste==0:
        schopnosti[9]=5
        priste=10
    elif stisknute_klavesy[pygame.K_a] and potion[0]!=0:
        buff[4]+=5
    elif stisknute_klavesy[pygame.K_s] and potion[1]!=0:
        hrac_zivoty+=hrac_max_zivoty/2
        if hrac_zivoty>hrac_max_zivoty:
            hrac_zivoty=hrac_max_zivoty
    elif stisknute_klavesy[pygame.K_d] and potion[2]!=0:
        for i in schopnosti:
            schopnosti[i-1]=0
    elif stisknute_klavesy[pygame.K_f] and potion[3]!=0:
        buff[1]+=10





    if hrac_zivoty<0:
        print("prohra")
    elif enemy_zivoty<0:
        porazeno+=1
        total_porazeno+=1
        if porazeno>len(enemaci)-1:
            print("výhra")
        else:
            print("porazil jsi jednoho")
            print(porazeno)
            print(len(enemaci))
            money+=random.randint(0,5**uroven)#novy nepritel
            xp+random.randint(0,round(100+1.4**level/2,0))
            enemy_max_zivoty=enemaci[porazeno]*2
            enemy_zivoty=enemy_max_zivoty
            enemy_demage=round(enemaci[porazeno]*0.4)+1
            enemy_demage=enemy_demage-enemy_demage/10*save[4]












    hrac_zivoty=round(hrac_zivoty,1)
    enemy_zivoty=round(enemy_zivoty,1)
    pop[0]=round(pop[0],1)
    pop[2]=round(pop[2],1)
    if pop[1]!=0:
        text=font.render(str(pop[0]), True, (0, 0, 0))
        screen.blit(text, (250-2,300-2+pop[1]))
        screen.blit(text, (250+2,300-2+pop[1]))
        screen.blit(text, (250-2,300+2+pop[1]))
        screen.blit(text, (250+2,300+2+pop[1]))
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







    pygame.draw.rect(screen,(255,0,0),(200,SCREEN_RESOLUTION[1]/4*3,hrac_zivoty/(hrac_max_zivoty/150),10))
    pygame.draw.rect(screen,(255,0,0),(700,SCREEN_RESOLUTION[1]/4*3,enemy_zivoty/(enemy_max_zivoty/150),10))
    text=font2.render(str(hrac_zivoty)+"/"+str(hrac_max_zivoty), True, (0,0,0))
    screen.blit(text, (250,SCREEN_RESOLUTION[1]/4*3))
    text=font2.render(str(enemy_zivoty)+"/"+str(enemy_max_zivoty), True, (0,0,0))
    screen.blit(text, (750,SCREEN_RESOLUTION[1]/4*3))
    if smer!=0 or timer>30:
        screen.blit(hrac,(hrac_x,SCREEN_RESOLUTION[1]/2))#vykreslovani
    screen.blit(enemy,(enemy_x,SCREEN_RESOLUTION[1]/2))
    pygame.display.update()
    clock.tick(fps)
