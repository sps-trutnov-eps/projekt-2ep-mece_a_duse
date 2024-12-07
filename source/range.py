import pygame 
import random 
import sys 
pygame.init() 
clock = pygame.time.Clock() 
rozliseni_okna = (1080,720) 
fps = 60 
 
 
soubor = open('data.txt', 'r', encoding = 'utf-8') 
save=[] 
for radek in soubor: 
    slovo=radek[:-1] 
    save.append(int(slovo)) 
soubor.close() 
 
font=pygame.font.Font(None, 64) 
 
pozadi=pygame.image.load("sprites/pozadi.png") 
strela=pygame.image.load("sprites/šíp.png") 
strela=pygame.transform.rotate(strela,90) 
timer=0 
a=0 
b=False  
c=0 
d=0 
e=[] 
terce=[] 
sip=[0,1000,1000] 
okno = pygame.display.set_mode(rozliseni_okna) 
score=0 
 
 
while True: 
    for udalost in pygame.event.get(): 
        if udalost.type == pygame.QUIT: 
            pygame.quit() 
            sys.exit() 
    stisknute_klavesy = pygame.key.get_pressed() 
    mys=pygame.mouse.get_pos() 
    okno.blit(pozadi,(0,0)) 
     
     
    if timer==0:#vytváření terčů 
        e=[] 
        timer=1000/(score+10) 
        e.append(random.randint(70,150)) 
        e.append(random.randint(e[0],rozliseni_okna[0]-e[0])) 
        e.append(random.randint(e[0],rozliseni_okna[1]-e[0])) 
        e.append(240) 
        terce.append(e) 
    else: 
        timer-=1 
 
    if pygame.mouse.get_pressed()[0] and sip[0]==0: 
        sip[0]=60 
 
    if sip[0]==40: 
        sip[1]=mys[0] 
        sip[2]=mys[1] 
    if sip[0]>0: 
        if not (pygame.mouse.get_pressed()[0] and sip[0]==41): 
            sip[0]-=1 
    if sip[0]==1: 
        a=0 
        while a<len(terce): 
            if (sip[1]-terce[a][1])**2+(sip[2]-terce[a][2])**2<terce[a][0]**2:
                score+=1
                terce.remove(terce[a]) 
            else : 
                a+=1 
        sip[1]=1000 
        sip[2]=1000 
     
     
     
    text=font.render(str(score),True ,(0,0,0))#score 
    okno.blit(text,(900,120)) 
     
     
    strela2=pygame.transform.scale(strela,(sip[0]*6,sip[0]*3)) 
     
     
     
    if b: 
        if score>save[20]: 
            save[20]=score 
        save[12]+=score 
        save[13]+=score 
        score=0 
         
         
         
         
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
        #return 0#Pavle Tady to přepiš!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!         
         
         
         
    b=False   
    a=0 
     
     
     
     
    while a<len(terce): 
         
        pygame.draw.ellipse(okno,(255,0,0),(terce[a][1]-terce[a][0]/2,terce[a][2]-terce[a][0]/2,terce[a][0],terce[a][0])) 
        pygame.draw.ellipse(okno,(255,255,255),(terce[a][1]-terce[a][0]/4,terce[a][2]-terce[a][0]/4,terce[a][0]/2,terce[a][0]/2)) 
        pygame.draw.ellipse(okno,(255,0,0),(terce[a][1]-terce[a][0]/8,terce[a][2]-terce[a][0]/8,terce[a][0]/4,terce[a][0]/4)) 
 
 
 
        if terce[a][3]>0: 
             terce[a][3]-=1 
        elif terce[a][3]==0: 
            terce[a][0]-=1 
        if terce[a][0]==0: 
            b=True 
            terce.remove(terce[a]) 
        else:     
            a+=1 
         
     
     
     
         
         
    if 0<sip[0]<60: 
        okno.blit(strela2,(sip[1]-sip[0]*3,sip[2]-10+sip[0]*1.5)) 
     
    pygame.display.update() 
    clock.tick(fps) 
 
