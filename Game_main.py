#This is the main file of the game

"""Package"""
import pygame
import random
import itertools
from pygame import *

"""Code"""

"""init"""
pygame.init()
screen = pygame.display.set_mode([410, 500]) #size of the screen : width x height
run = True
pygame.font.init()
police_number = pygame.font.SysFont('Arial', 50)

"""Structure"""
class Square(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.value = random.choice([2, 4])
        self.surface = pygame.Surface((90, 90))

        if self.value == 2:
            self.surface.fill((233, 221, 209))
        else:
            self.surface.fill((232, 217, 189))

        self.rect = self.surface.get_rect()
        self.text = police_number.render("{}".format(self.value), False, (0, 0, 0))
        self.rect_text = self.text.get_rect(center = self.rect.center)


        




    def update(self, pressed_key):
        if pressed_key[K_UP]:
            self.rect.move_ip(0, -90)
        if pressed_key[K_LEFT]:
            self.rect.move_ip(-90, 0)
        if pressed_key[K_DOWN]:
            self.rect.move_ip(0, 90)
        if pressed_key[K_RIGHT]:
            self.rect.move_ip(90, 0)

        #border of screen
        if self.rect.left < 10:
            self.rect.left = 10
        if self.rect.right > 400:
            self.rect.right = 400
        if self.rect.top <= 100:
            self.rect.top = 100
        if self.rect.bottom >= 490:
            self.rect.bottom = 490

        #update position of the number
        self.rect_text = self.text.get_rect(center = self.rect.center)
        

        

#initializing the square
square_ini = Square()

"""Gameloop"""
while run:


    #initializing the game screen
    pygame.display.set_caption("2048")
    screen.fill((255, 255, 255)) #173, 157, 142

    pygame.draw.rect(screen, (173, 157, 142), (0, 90, 410, 410))

    for i, j in itertools.product(range(4), range(4)):
        pygame.draw.rect(screen, (193, 180, 164), (i*100+10, j*100+100, 90, 90))

    screen.blit(square_ini.surface, square_ini.rect)
    screen.blit(square_ini.text, square_ini.rect_text)

    #game
    pressed_key = pygame.key.get_pressed()

    square_ini.update(pressed_key)

    for event in pygame.event.get():

        #if user wants to quit
        if event.type == pygame.QUIT:
            run = False

        

    pygame.display.flip()

pygame.quit()