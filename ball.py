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