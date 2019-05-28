# Imports
import pygame 
import sys 
import random 
import ball
import paddle


class Ping:
    WHITE = 255, 255, 255
    PADDLE_WIDTH = 10
    PADDLE_HEIGHT = 50
    BALL_RADIUS = 5

    left_player_score = 0
    right_player_score = 0
    
    ball_y_velocity = random.randrange(-2, 2)

    paddles = []
    balls = []

    def __init__(self, dis_width, dis_height):
        pygame.init()

        self.dis_height = dis_height
        self.dis_width = dis_width
        self.screen = pygame.display.set_mode((self.dis_width, self.dis_height))
        self.left_paddle = paddle.Paddle(
            5,
            10,
            (self.dis_height / 2 - self.PADDLE_HEIGHT / 2),
            self.PADDLE_WIDTH, self.PADDLE_HEIGHT, pygame.K_w,
            pygame.K_s)
        self.right_paddle = paddle.Paddle(
            5,
            self.dis_width - 20,
            (self.dis_height / 2 - self.PADDLE_HEIGHT / 2),
            self.PADDLE_WIDTH,
            self.PADDLE_HEIGHT,
            pygame.K_UP,
            pygame.K_DOWN)
        self.ball = ball.Ball(
            -2,
            self.ball_y_velocity,
            self.dis_width // 2,
            self.dis_height // 2,
            self.BALL_RADIUS)

        self.balls.extend([self.ball])
        self.paddles.extend([self.left_paddle, self.right_paddle])

        pygame.font.init()
        self.score_font = pygame.font.SysFont('Arial', 30)

    def draw_pitch(self):
        pygame.draw.line(self.screen, self.WHITE, (20, 0), (20, self.dis_height))
        pygame.draw.line(self.screen, self.WHITE, (self.dis_width - 20, 0), (self.dis_width - 20, self.dis_height))
        pygame.draw.line(self.screen, self.WHITE, (self.dis_width / 2, 0), (self.dis_width / 2, self.dis_height))

    # refactor to take a list of objects to draw
    def draw_balls(self, balls):
        for ball in balls:
            pygame.draw.circle(self.screen, self.WHITE, (ball.xPos, ball.yPos), ball.radius)

    def draw_paddles(self, paddles):
        for paddle in paddles:
            pygame.draw.rect(self.screen, self.WHITE, paddle)

    def wall_collision_check(self, ball):
        if ball.yPos < 0 or ball.yPos > self.dis_height:
            ball.yVel = -ball.yVel

    def paddle_collision_check(self, ball, left_paddle, right_paddle):
        if left_paddle.collidepoint(ball.xPos - ball.radius, ball.yPos):
            ball.xVel = -ball.xVel
            ball.yVel = random.randrange(-2, 2)

        if right_paddle.collidepoint(ball.xPos + ball.radius, ball.yPos):
            ball.xVel = -ball.xVel
            ball.yVel = random.randrange(-2, 2)

    def gutter_ball(self, ball):
        if ball.xPos < 0:
            ball.xPos = self.dis_width // 2
            ball.yPos = self.dis_height // 2
            ball.yVel = random.randrange(-2, 2)
            self.right_player_score += 1

        if ball.xPos > self.dis_width:
            ball.xPos = self.dis_width // 2
            ball.yPos = self.dis_height // 2
            ball.yVel = random.randrange(-2, 2)
            self.left_player_score += 1

    def check_events(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_ESCAPE]:
            print("exit!!!!")
            sys.exit()

        for event in pygame.event.get():
            # for debugging
            print(event)

            if event.type == pygame.QUIT:
                sys.exit()

    def game_loop(self):
        while True:
            self.check_events()

            # clear the screen before redraw
            self.screen.fill((0, 0, 0))

            # check for collisions
            self.wall_collision_check(self.ball)
            self.paddle_collision_check(self.ball, self.left_paddle, self.right_paddle)
            self.gutter_ball(self.ball)

            # Update the gameObjects
            self.ball.moveBall()
            self.left_paddle.move_paddle(self.dis_height)
            self.right_paddle.move_paddle(self.dis_height)

            # draw the game objects
            self.draw_pitch()
            self.draw_balls(self.balls)
            self.draw_paddles(self.paddles)

            left_player_score_text = self.score_font.render(str(self.left_player_score), False, self.WHITE)
            right_player_score_text = self.score_font.render(str(self.right_player_score), False, self.WHITE)
            self.screen.blit(left_player_score_text, (self.dis_width / 2 - 30, 50))
            self.screen.blit(right_player_score_text, (self.dis_width / 2 + 30, 50))

            # redraw the display
            pygame.display.update()

            # Insert 10ms delay
            pygame.time.delay(10)


class Player:
    def __init__(self):
        pass


if __name__ == '__main__':
    ping = Ping(640, 480)
    ping.game_loop()
