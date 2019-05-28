#Imports
import pygame, sys, random, ball, paddle

class Ping():
    WHITE = 255,255,255
    PADDLE_WIDTH = 10
    PADDLE_HEIGHT = 50
    BALL_RADIUS = 5
    
    leftPlayerScore = 0
    rightPlayerScore = 0
    
    ballYVel = random.randrange(-2, 2)
    
    screenObjects = []
    paddles = []
    balls = []

    def __init__(self, disWidth, disHeight):
        pygame.init()
    
        self.disHeight = disHeight
        self.disWidth = disWidth
        self.screen = pygame.display.set_mode((self.disWidth, self.disHeight))
        
        self.leftPaddle = paddle.Paddle(5, 10, (self.disHeight / 2 - self.PADDLE_HEIGHT / 2), self.PADDLE_WIDTH, self.PADDLE_HEIGHT, pygame.K_w, pygame.K_s)
        self.rightPaddle = paddle.Paddle(5, self.disWidth - 20, (self.disHeight / 2 - self.PADDLE_HEIGHT / 2), self.PADDLE_WIDTH, self.PADDLE_HEIGHT, pygame.K_UP, pygame.K_DOWN)
        self.ball = ball.Ball(-2, self.ballYVel, self.disWidth // 2, self.disHeight // 2, self.BALL_RADIUS)

        self.balls.extend([self.ball])
        self.paddles.extend([self.leftPaddle, self.rightPaddle])
        
        pygame.font.init()
        self.myfont = pygame.font.SysFont('Arial', 30)
                
    def drawPitch(self):
        leftGutter = pygame.draw.line(self.screen, self.WHITE, (20, 0), (20, self.disHeight))
        rightGutter = pygame.draw.line(self.screen, self.WHITE, (self.disWidth - 20, 0), (self.disWidth - 20, self.disHeight))
        centralDivide = pygame.draw.line(self.screen, self.WHITE, (self.disWidth / 2, 0), (self.disWidth / 2, self.disHeight))
        
    #refactor to take a list of objects to draw    
    def drawBalls(self, balls):
        for ball in balls:
            pygame.draw.circle(self.screen, self.WHITE, (ball.xPos, ball.yPos), ball.radius)
        
    def drawPaddles(self, paddles):
        for paddle in paddles:
            pygame.draw.rect(self.screen, self.WHITE, paddle)
        
    def wallCollisionCheck(self, ball):
        if ball.yPos < 0 or ball.yPos > self.disHeight:
            ball.yVel = -ball.yVel
        
    def paddleCollisionCheck(self, ball, leftPaddle, rightPaddle):
        if leftPaddle.collidepoint(ball.xPos - ball.radius, ball.yPos):
            ball.xVel = -ball.xVel
            ball.yVel = random.randrange(-2, 2)
        
        if rightPaddle.collidepoint(ball.xPos + ball.radius, ball.yPos):
            ball.xVel = -ball.xVel
            ball.yVel = random.randrange(-2, 2)
        
    def gutterBall(self, ball):
        if ball.xPos < 0:
            ball.xPos = self.disWidth // 2
            ball.yPos = self.disHeight // 2
            ball.yVel = random.randrange(-2, 2)
            self.rightPlayerScore += 1
            
        if ball.xPos > self.disWidth:
            ball.xPos = self.disWidth // 2
            ball.yPos = self.disHeight // 2
            ball.yVel = random.randrange(-2, 2)
            self.leftPlayerScore += 1
        
    def checkEvents(self):
        pressed = pygame.key.get_pressed()
            
        if pressed[pygame.K_ESCAPE]:
            print("exit!!!!")
            sys.exit()
    
        for event in pygame.event.get():        
            #for debugging
            print(event)
            
            if event.type == (pygame.QUIT):
                sys.exit()
            
    def gameLoop(self):
        while True:
            self.checkEvents()
            
            #clear the screen before redraw
            self.screen.fill((0, 0, 0))
            
            #check for collisions
            self.wallCollisionCheck(self.ball)
            self.paddleCollisionCheck(self.ball, self.leftPaddle, self.rightPaddle)
            self.gutterBall(self.ball)
            
            #Update the gameObjects
            self.ball.moveBall()
            self.leftPaddle.movePaddle(self.disHeight)
            self.rightPaddle.movePaddle(self.disHeight)
                    
            #draw the game objects
            self.drawPitch()
            self.drawBalls(self.balls)
            self.drawPaddles(self.paddles)
            
            leftPlayerScoreText = self.myfont.render(str(self.leftPlayerScore), False, self.WHITE)
            rightPlayerScoreText = self.myfont.render(str(self.rightPlayerScore), False, self.WHITE)
            self.screen.blit(leftPlayerScoreText,(self.disWidth / 2 - 30, 50))
            self.screen.blit(rightPlayerScoreText,(self.disWidth / 2 + 30, 50))

            #redraw the display
            pygame.display.update()
            
            #Insert 10ms delay
            pygame.time.delay(10)
    
        
##################################################################       
        


##################################################################


            
##################################################################           

class Player():
    def __init__():
        pass

##################################################################            
if __name__ == '__main__':
    ping = Ping(640,480)
    ping.gameLoop()