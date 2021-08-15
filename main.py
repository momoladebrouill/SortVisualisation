import pygame as pyg
from random import randint
from math import*
from colorsys import hsv_to_rgb
pyg.init()
f=pyg.display.set_mode((500,500))
clock=pyg.time.Clock()
font=pyg.font.SysFont('comic sans ms',50)
pyg.display.set_caption("Bubble sort vizualisation")

def carr(x,y,width=5,high=5,c=(250,0,randint(0,250))):
    pyg.draw.rect(f,c,(x,y,width,high))
l=[]
mix=[]
for i in range(500):
    l.append(i)
for i in range(500):
    mix.append(l.pop(randint(0,len(l)-1)))
b=True
shuffle=False
sort=True
try :
    while b:
        b+=1
        pyg.display.flip()
        clock.tick(30)
        carr(0,0,500,500,(0,0,0,250))
        for i in range(500):
            carr(mix[i],i,1,500-i,hsv_to_rgb(i/500,1,255))
        pressed=pyg.key.get_pressed()
        
        if pressed[pyg.K_SPACE]:
            ...
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                b = False 
                pyg.quit()
            elif event.type==pyg.KEYUP:
                if event.key==pyg.K_SPACE:
                    sort=True
                else:
                    shuffle=False
            elif event.type==pyg.KEYDOWN:
                if event.key==pyg.K_SPACE:
                    sort=False
                else:
                    shuffle=True
        if shuffle:
            n_mix=[]
            for i in range(500):
                n_mix.append(mix.pop(randint(0,len(mix)-1)))
            mix=n_mix[:]
        if sort:
            for i in range(len(mix)-1):
                if mix[i]<mix[i+1]:
                    mix[i+1],mix[i]=mix[i],mix[i+1]
        else:
            f.blit(font.render('Pause',1,(255,255,255)),(20,0))
        
except:
    pyg.quit()
    raise
    
