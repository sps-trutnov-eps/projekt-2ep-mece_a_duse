import pygame
import random
import sys

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
pozadi=pygame.image.load("sprites/pozadi.png")

#slovo=[]
#soubor = open('data.txt', 'r', encoding = 'utf-8')
#for radek in soubor:
#    slovo=radek[:-1]
#    save.append(slovo)
#soubor.close()

enemy=pygame.transform.scale(enemy,(150,150))
enemy=pygame.transform.flip(enemy,True,False)
hrac=pygame.transform.scale(hrac,(150,150))
utocim=True
timer=0
hrac_x=SCREEN_RESOLUTION[0]/3-160
enemy_x=SCREEN_RESOLUTION[0]*2/3
hrac_max_zivoty=1000
enemy_max_zivoty=1000
enemy_zivoty=enemy_max_zivoty
hrac_zivoty=hrac_max_zivoty
hrac_demage=100
enemy_demage=100
schopnosti=[0,0,0,0,0,0]
brneni=5
mec=10
shield=1-2/10
smer=5
priste=0
a=0
total_demage=0
enemy_demage=enemy_demage-enemy_demage/10*brneni
hrac_demage=hrac_demage*mec
buff=[0,0,0,0]#stun,shield,heal,poison
enemaci=[10,12,14,16,20]
porazeno=0
total_porazeno=0
money=0
level=0
xp=0
uroven=2
while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pass
            #return 10
        #for i, button in enumerate(buttons):
         #   if button.handle_event(event):
          #      pass
    stisknute_klavesy = pygame.key.get_pressed()
    timer+=1
    if utocim:
        if 199<hrac_x<500:#pohyb hrace
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
                    if priste==0:#urceni jaky utok udelat
                        enemy_zivoty-=hrac_demage
                        total_demage+=hrac_demage
                    if priste==1:
                        enemy_zivoty-=hrac_demage*2
                        total_demage+=hrac_demage*2
                    elif priste==2:
                        enemy_zivoty-=hrac_demage/2
                        total_demage+=hrac_demage/2
                        buff[0]=5
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
                    while a<len(buff)-1:
                        if buff[a]!=0:
                            buff[a]-=1
                        a+=1
                    a=0
                    print("uder h")
            if hrac_x<400:
                utocim=False
                hrac_x-=smer
                hrac_x-=smer
            else:
                if priste==0:#urceni jaky utok udelat
                    enemy_zivoty-=hrac_demage
                if priste==1:
                    enemy_zivoty-=hrac_demage*2
                elif priste==2:
                    enemy_zivoty-=hrac_demage/2
                    buff[0]=5
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
                smer=smer*-1
                hrac_x+=smer
                hrac_x+=smer
                hrac_x+=smer
                enemy_zivoty-=hrac_demage/4*buff[-1]
                priste=0
                while a<5:
                    if schopnosti[a]!=0:
                        schopnosti[a]-=1
                    a+=1
                a=0
                while a<len(buff)-1:
                    if buff[a]!=0:
                        buff[a]-=1
                    a+=1
                a=0


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
                    if buff[3]>0:
                        hrac_zivoty+=enemy_demage*-1
                    else:
                        if buff[2]>0:#pocitani demage
                            hrac_zivoty-=enemy_demage/5
                        elif 1==random.randint(1,5):
                            hrac_zivoty-=enemy_demage/shield
                        else:
                            hrac_zivoty-=enemy_demage
                    if hrac_zivoty>hrac_max_zivoty:
                        hrac_zivoty=hrac_max_zivoty
                    print("uder e")
                    if hrac_zivoty>hrac_max_zivoty:
                        hrac_zivoty=hrac_max_zivoty
                    smer=smer*-1
                    enemy_x+=smer
    




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






    if hrac_zivoty<0:
        print("prohra")
    elif enemy_zivoty<0:
        porazeno+=1
        total_porazeno+=1
        if porazeno==len(enemaci):
            print("výhra")
        else:
            print("porazil jsi jednoho")
            money+=random.randint(0,5**uroven)#novy nepritel
            xp+random.randint(0,round(100+1.4**level/2,0))
            enemy_max_zivoty=enemaci[porazeno]*2
            enemy_zivoty=enemy_max_zivoty
            enemy_demage=round(enemaci[porazeno]*0.4)+1











    screen.blit(pozadi,(0,0))

    













    pygame.draw.rect(screen,(255,0,0),(200,SCREEN_RESOLUTION[1]/4*3,hrac_zivoty/(hrac_max_zivoty/150),10))
    pygame.draw.rect(screen,(255,0,0),(700,SCREEN_RESOLUTION[1]/4*3,enemy_zivoty/(enemy_max_zivoty/150),10))
    screen.blit(hrac,(hrac_x,SCREEN_RESOLUTION[1]/2))#vykreslovani
    screen.blit(enemy,(enemy_x,SCREEN_RESOLUTION[1]/2))
    pygame.display.update()
    clock.tick(fps)
