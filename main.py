#import modules
import pygame
import os
from pygame.locals import *

SCREENWIDTH = 1280
SCREENHEIGHT = 720


def main():
    global screen
    global background
    global icon    
    #init
    pygame.init()

    #set dimensions of screen
    screen = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))

    #set icon and title of screen
    icon = pygame.image.load("Assets/icon.jpg")
    pygame.display.set_icon(icon)    
    pygame.display.set_caption("Bongocat: The game")


    def draw_background():
        background = pygame.image.load("Assets/background0.png")
        screen.blit(pygame.transform.scale(background, (SCREENWIDTH,SCREENHEIGHT)), (0,0))

    #draw title
    def draw_title():
        scale = 0.85
        width = 877
        height = 161

        title = pygame.image.load("Assets/Main-Menu/Bongocatthegame.png")
        screen.blit(pygame.transform.scale(title, (int(width*scale), int(height*scale))), (int(SCREENWIDTH / 2 - 350), 75))
    
    def draw_playbtn():
        scale = 0.7
        width = 397
        height = 87

        playbtn = pygame.image_load("Assets/Main-Menu/Buttons/PLAYbtn.png")
        screen.blit(pygame.transform.scale(title, (int(width*scale), int(height*scale))), (int(SCREENWIDTH / 2 - 350), 500))
    
    draw_background()
    draw_title()
    draw_playbtn()
    pygame.display.flip()


    while True:
        event = pygame.event.wait()
        if event.type == QUIT:
            pygame.display.quit()


if __name__ == "__main__":
    main()