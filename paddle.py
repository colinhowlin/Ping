import pygame


class Paddle(pygame.Rect):
    def __init__(self, vel, left, top, width, height, upKey, downKey):
        self.vel = vel
        self.top = top
        self.left = left
        self.width = width
        self.height = height
        self.upKey = upKey
        self.downKey = downKey
        super()
        
    def move_paddle(self, dis_height):
        keysPressed = pygame.key.get_pressed()
        
        if keysPressed[self.upKey] and self.top > 0:
            self.top -= self.vel
            print("Up key pressed")
            
        if keysPressed[self.downKey] and self.top < dis_height - self.height:
            self.top += self.vel
            print("down key pressed")