import pygame
from pygame import *


class Player(pygame.sprite.Sprite):

    def __init__(self, surf):
        pygame.sprite.Sprite.__init__(self)
        self.screen = surf
        self.rect = pygame.rect.Rect((20, 20), (20, 20))
        #self.image.set_colorkey((255, 255, 255))
        #self.rect = self.image.get_rect()
        self.rect.centerx = 20
        self.x_speed = 0
        self.y_speed = 0
        self.jump = False
        self.jump_counter = 0

    def update(self):
        self.x_speed = 0
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            self.x_speed = -2
        elif keys[K_RIGHT]:
            self.x_speed = 2

        if keys[K_j]:
            self.jump = True

        if self.jump:
            self.jump_counter += 1/30
            self.y_speed = -3*(-((self.jump_counter - 2) ** 2) + 4)
            print(f"Jump Counter: {self.jump_counter}, Y Speed: {-self.y_speed}!")

        self.rect.centerx += self.x_speed
        self.rect.centery += self.y_speed

        if self.rect.bottom >= 300:
            self.jump = False
            self.y_speed = 0
            self.jump_counter = 0
