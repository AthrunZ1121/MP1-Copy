import pygame, sys
from pygame.locals import *

pygame.init()

#Create a displace surface object
#Below line will let you toggle from maximize to the initial size
screen1 = pygame.display.set_mode((400, 300), RESIZABLE)
oldwidth = screen1.get_width()
oldheight = screen1.get_height()
sky_surface = pygame.image.load('111.png').convert()

mainLoop = True

while mainLoop:
    screen1.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainLoop = False
        elif event.type == VIDEORESIZE:
            scalex = screen1.get_width() / oldwidth
            scaley = screen1.get_height() / oldheight
            
            sky_surface= pygame.transform.scale(sky_surface, (sky_surface.get_width()*scalex, sky_surface.get_height()*scaley))
            oldwidth = screen1.get_width()
            oldheight = screen1.get_height()
   
    screen1.blit(sky_surface,(0,0))
    pygame.display.update()

pygame.quit()