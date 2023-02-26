import pygame
from settings import *

class Transition:
    def __init__(self, reset, player):
        
        #Setup
        self.display_surface = pygame.display.get_surface()
        self.reset = reset
        self.player = player
        
        #Overlay image
        self.image = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.color = 255
        self.speed = -2
        
    def play(self):
        
        
        #Wake the player
        
        #Set the speed to -2 at end of transition
        
        self.color += self.speed
        if self.color <= 0:
            self.speed *= -1
            self.color = 0
            self.reset() #Call Reset
        if self.color > 255:
            self.color = 255
            self.player.sleep = False
            self.speed = -2
            
        self.image.fill((self.color, self.color, self.color))
        self.display_surface.blit(self.image, (0, 0), special_flags= pygame.BLEND_RGBA_MULT)