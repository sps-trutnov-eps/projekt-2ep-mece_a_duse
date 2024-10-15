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
enemy=pygame.transform.flip(enemy,True,False)
hrac=pygame.transform.scale(hrac,(150,150))
utocim=True
timer=0
hrac_x=SCREEN_RESOLUTION[0]/3
enemy_x=SCREEN_RESOLUTION[0]*2/3
enemy_zivoty=1000
hrac_zivoty=2000
hrac_demage=100
enemy_demage=100
schopnosti=[0,0,0,0,0,0]
brneni=5
mec=3
smer=2
priste=0
hrac_max_zivoty=1000
a=0
enemy_demage=enemy_demage-enemy_demage/10*brneni
hrac_demage=hrac_demage*mec
buff=[0,0,0,0]#stun,shield,heal,poison
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
        if 359<hrac_x<500:#pohyb hrace
            hrac_x+=smer
        else:
            print("b")
            if hrac_x<400:
                utocim=False
                hrac_x-=smer
                hrac_x-=smer
                print("c")
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
                print("uder h")


    elif not utocim and buff[0]==0:#pohyb nepritele
         if 721>enemy_x>400:
           enemy_x+=smer
         else:
             print("a")
             if enemy_x>600:
                utocim=True
                enemy_x-=smer
                enemy_x-=smer
                print("d")
             else:
                if buff[3]>0:
                    hrac_zivoty+=enemy_demage*-1
                else:
                    if buff[2]>0:#pocitani demage
                        hrac_zivoty-=enemy_demage/5
                    elif 1==random.randint(1,5):
                        hrac_zivoty-=enemy_demage/2
                    else:
                        hrac_zivoty-=enemy_demage
                if hrac_zivoty>hrac_max_zivoty:
                    hrac_zivoty=hrac_max_zivoty
                smer=smer*-1
                enemy_x+=smer
                enemy_x+=smer
                enemy_x+=smer
                print("uder e")
                





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
        print("výhra")








    screen.blit(pozadi,(0,0))

    














    screen.blit(hrac,(hrac_x,SCREEN_RESOLUTION[1]/2))#vykreslovani
    screen.blit(enemy,(enemy_x,SCREEN_RESOLUTION[1]/2))
    pygame.display.update()
    clock.tick(fps)
