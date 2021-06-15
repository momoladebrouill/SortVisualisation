import pygame as pyg
from random import randint
from math import*
pyg.init()
f=pyg.display.set_mode(size=(500,500))
pyg.display.set_caption("ARRRFG")
b=True
def carr(x,y,width=5,high=5,c=(250,0,randint(0,250))):
    pyg.draw.rect(f,c,(x,y,width,high))
l=[]
for i in range(500):
    l.append(i)
mix=[]
for i in range(500):
    mix.append(l.pop(randint(0,len(l)-1)))
try :
    while b:
        # actualiser:
        pyg.display.flip()

        # appliquer les images sur le jeu:
        carr(0,0,500,500,(0,0,0,250))
        
        for i in range(500):
            carr(250+cos(mix[i])*i,250+sin(mix[i])*i,c=(255,255,255))
        for i in range(500):
            carr(500-mix[i],i,c=(255,0,0))
        for i in range(500):
            carr(mix[i],i,c=(0,0,255))
        pressed=pyg.key.get_pressed()
        
        if pressed[pyg.K_SPACE]:
            
            for i in range(len(mix)-1):
                    if mix[i]<mix[i+1]:
                        mix[i+1],mix[i]=mix[i],mix[i+1]
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                b = False  # la boucle n'est plus vraie dons on arrete de trourner
                print("fin du jeu")
                pyg.mixer.music.fadeout(1)
                pyg.quit()
                    
except:
    pyg.quit()
    raise
    
