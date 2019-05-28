#Imports
import pygame, sys

class Ping():
    WHITE = 255,255,255
    PADDLE_WIDTH = 10
    PADDLE_HEIGHT = 40
    BALL_RADIUS = 5
    screenObjects = []

    def __init__(self, disWidth, disHeight):
        pygame.init()
    
        self.disHeight = disHeight
        self.disWidth = disWidth
        self.screen = pygame.display.set_mode((self.disWidth, self.disHeight))
        
        self.leftPaddle = Paddle(5, 10, (self.disHeight / 2 - self.PADDLE_HEIGHT / 2), self.PADDLE_WIDTH, self.PADDLE_HEIGHT)
        self.rightPaddle = Paddle(5, self.disWidth - 20, (self.disHeight / 2 - self.PADDLE_HEIGHT / 2), self.PADDLE_WIDTH, self.PADDLE_HEIGHT)    
        self.ball = Ball(-2, 0, self.disWidth // 2, self.disHeight // 2, self.BALL_RADIUS)
        
        self.screenObjects.extend([self.ball, self.leftPaddle, self.rightPaddle])
        
    def drawPitch(self):
        leftGutter = pygame.draw.line(self.screen, self.WHITE, (20, 0), (20, self.disHeight))
        rightGutter = pygame.draw.line(self.screen, self.WHITE, (self.disWidth - 20, 0), (self.disWidth - 20, self.disHeight))
        centralDivide = pygame.draw.line(self.screen, self.WHITE, (self.disWidth / 2, 0), (self.disWidth / 2, self.disHeight))
        
    def drawGameObjects(self, ball, leftPaddle, rightPaddle):
        pygame.draw.circle(self.screen, self.WHITE, (ball.xPos, ball.yPos), ball.radius)
        pygame.draw.rect(self.screen, self.WHITE, leftPaddle)
        pygame.draw.rect(self.screen, self.WHITE, rightPaddle)
        
    def wallCollisionCheck(self, ball):
        if ball.yPos < 0 or ball.yPos > self.disHeight:
            ball.yVel = -ball.yVel
        
    def paddleCollisionCheck(self, ball, leftPaddle, rightPaddle):
        if leftPaddle.collidepoint(ball.xPos - ball.radius, ball.yPos):
            ball.xVel = -ball.xVel
        
        if rightPaddle.collidepoint(ball.xPos + ball.radius, ball.yPos):
            ball.xVel = -ball.xVel
        
    def gutterBall(self, ball):
        pass
        
    def checkEvents(self):
        pressed = pygame.key.get_pressed()
            
        if pressed[pygame.K_ESCAPE]:
            print("exit!!!!")
            sys.exit()
    
        for event in pygame.event.get():        
            #for debugging
            #print(event)
            
            if event.type == (pygame.QUIT):
                sys.exit()
            
    def gameLoop(self):
        while True:
            self.checkEvents()
                    
            self.screen.fill((0, 0, 0))
            
            self.wallCollisionCheck(self.ball)
            self.paddleCollisionCheck(self.ball, self.leftPaddle, self.rightPaddle)
                    
            self.drawPitch()
            self.drawGameObjects(*self.screenObjects)
            self.ball.moveBall()
            self.leftPaddle.movePaddle(self.disHeight)
            #self.rightPaddle.movePaddle(self.disHeight)
            
            pygame.display.update()
            
            pygame.time.delay(10)
    
        
##################################################################       
        
class Ball():
    def __init__(self, xVel, yVel, xPos, yPos, radius):
        self.xVel = xVel
        self.yVel = yVel
        self.xPos = xPos
        self.yPos = yPos
        self.radius = radius
        
    def moveBall(self):
        self.xPos += self.xVel
        self.yPos += self.yVel

##################################################################

class Paddle(pygame.Rect):
    def __init__(self, vel, left, top, width, height):
        self.vel = vel
        self.top = top
        self.left = left
        self.width = width
        self.height = height
        super()
        
    def movePaddle(self, disHeight):
        keysPressed = pygame.key.get_pressed()
        
        if keysPressed[pygame.K_w] and self.top > 0:
            self.top -= self.vel
            
        if keysPressed[pygame.K_s] and self.top < disHeight:
            self.top += self.vel
            
##################################################################           
            
if __name__ == '__main__':
    ping = Ping(640,480)
    ping.gameLoop()