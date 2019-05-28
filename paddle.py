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
        
    def movePaddle(self, disHeight):
        keysPressed = pygame.key.get_pressed()
        
        if keysPressed[self.upKey] and self.top > 0:
            self.top -= self.vel
            print("Up key pressed")
            
        if keysPressed[self.downKey] and self.top < disHeight - self.height:
            self.top += self.vel
            print("down key pressed")