from pygame import*

import random

p1arrow_control = False
p2arrow_control = True
global screen
global vscomputer
mixer.init()
init()
hit = mixer.Sound("sounds/ponghit2.mp3")

BACKGROUND_COLOR = (50, 50, 50)


clock = time.Clock()
class GameSprite(sprite.Sprite):
    def __init__(self, y, x, width, height, image_name, speed=2):
        super().__init__()
        self.image = transform.scale(
        image.load(image_name),
        (width, height)
    )
        self.speed_x = self.speed_y = speed
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
    def draw(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player1(GameSprite):

    def p1WS(self, player1):
        pressed_keys = key.get_pressed()
        if pressed_keys[K_w] and player1.rect.y > 0:
            self.rect.y -= self.speed_y
        if pressed_keys[K_s] and player1.rect.y < 600:
            self.rect.y += self.speed_y
    def p1arrows(self, player1):
        pressed_keys = key.get_pressed()
        if pressed_keys[K_UP] and player1.rect.y > 0:
            self.rect.y -= self.speed_y
        if pressed_keys[K_DOWN] and player1.rect.y < 650:
            self.rect.y += self.speed_y

class Ball(GameSprite):
    def move(self, window):
        #if self.rect.x <= 0 or self.rect.x >= window.get_width() - self.rect.width:
            #self.speed_x *= -1
        if self.rect.y <= 0 or self.rect.y >= window.get_height() - self.rect.height:
            self.speed_y *= -1
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y



    def score(self, ball):
        ball.rect.x = 500
        ball.rect.y = 400
    def scorep1(self):
        global p1score
        p1score += 1
    def scorep2(self):
        global p2score
        p2score += 1
    def collide(self, Gamesprite):
        return self.rect.colliderect(Gamesprite.rect)
class Player2(GameSprite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.reaction_delay = 10

    def automove(self, ball):
        if self.reaction_delay <= 0:
            if ball.rect.y < self.rect.y:
                self.rect.y -= self.speed_y
            elif ball.rect.y > self.rect.y:
                self.rect.y += self.speed_y
            self.reaction_delay = 2
        else:
            self.reaction_delay -= 1
    def p2WS(self, player2):
        pressed_keys = key.get_pressed()
        if pressed_keys[K_w] and player2.rect.y > 0:
            self.rect.y -= self.speed_y
        if pressed_keys[K_s] and player2.rect.y < 650:
            self.rect.y += self.speed_y
    def p2arrows(self, player2):
        pressed_keys = key.get_pressed()
        if pressed_keys[K_UP] and player2.rect.y > 0:
            self.rect.y -= self.speed_y
        if pressed_keys[K_DOWN] and player2.rect.y < 650:
            self.rect.y += self.speed_y



def vscomputer_run(window, p1arrow_control):
    global p1score
    global p2score
    window.fill(BACKGROUND_COLOR)
    bg = transform.scale(
        image.load("sprites/bg.png"),
        (window.get_width(), window.get_height())
    )

    p1score = 0
    p2score = 0
    p1win = False
    p2win = False
    game = True
    player1 = Player1(350, 890, 50, 150, "sprites/paddle.png", 10)
    player2 = Player2(350, 50, 100, 150, "sprites/paddle2.png", 12)
    ball = Ball(400, 460, 40, 40, "sprites/ball.png", 6)

    while game:

        for e in event.get():
            pressed_keys = key.get_pressed()
            if e.type == QUIT or pressed_keys[K_ESCAPE]:
                game = False

        if p1score == 99:
            p1win = True
        if p2score == 99:
            p2win = True
        window.blit(bg, (0, 0))
        p1scoretext = font.Font("Retrofont.ttf", 100).render(str(p1score), True, (255, 255, 255))
        window.blit(p1scoretext, (750, 40))
        p2scoretext = font.Font("Retrofont.ttf", 100).render(str(p2score), True, (255, 255, 255))
        window.blit(p2scoretext, (200, 40))
        if ball.collide(player1) or ball.collide(player2):
            if ball.rect.x > player1.rect.x or ball.rect.x < player2.rect.x:
                ball.speed_x *= -1
                hit.play()
        if p1win == True:
            p1wintext = font.SysFont("Freesansbold", 100).render("Player 1 Wins", True, (255, 255, 255))
            window.blit(p1wintext, (300, 400))


        if p2win == True:
            p2wintext = font.Font("Retrofont.ttf", 100).render("Player 2 Wins", True, (255, 255, 255))
            window.blit(p2wintext, (300, 400))
            time.wait(5000)
            game = False
        if ball.rect.x > 1000:
            ball.speed_x -= 1
            ball.score(ball)
            ball.scorep2()
            time.wait(3000)
        if ball.rect.x < -100:
            ball.speed_x += 1
            ball.score(ball)
            ball.scorep1()
            time.wait(3000)
        if p1arrow_control == True:
            player1.p1arrows(player2)
        else:
            player1.p1WS(player2)
        player1.draw(window)
        player2.update()
        player2.draw(window)
        player2.automove(ball)
        ball.draw(window)
        ball.move(window)
        display.update()
        clock.tick(60)
def vsplayer_run(window, p1arrow_control, p2arrow_control):

    global p1score
    global p2score
    window.fill(BACKGROUND_COLOR)
    bg = transform.scale(
        image.load("sprites/bg.png"),
        (window.get_width(), window.get_height())
    )

    p1score = 0
    p2score = 0
    p1win = False
    p2win = False
    game = True
    player1 = Player1(350, 890, 50, 150, "sprites/paddle.png", 10)
    player2 = Player2(350, 50, 100, 150, "sprites/paddle2.png", 10)
    ball = Ball(400, 460, 40, 40, "sprites/ball.png", 6)

    while game:

        for e in event.get():
            pressed_keys = key.get_pressed()
            if e.type == QUIT or pressed_keys[K_ESCAPE]:
                game = False

        if p1score == 99:
            p1win = True
        if p2score == 99:
            p2win = True
        window.blit(bg, (0, 0))
        p1scoretext = font.Font("Retrofont.ttf", 100).render(str(p1score), True, (255, 255, 255))
        window.blit(p1scoretext, (750, 40))
        p2scoretext = font.Font("Retrofont.ttf", 100).render(str(p2score), True, (255, 255, 255))
        window.blit(p2scoretext, (200, 40))
        if ball.collide(player1) or ball.collide(player2):
            if ball.rect.x > player1.rect.x or ball.rect.x < player2.rect.x:
                ball.speed_x *= -1
                hit.play()
        if p1win == True:
            p1wintext = font.Font("Retrofont.tff", 100).render("Player 1 Wins", True, (255, 255, 255))
            window.blit(p1wintext, (300, 400))


        if p2win == True:
            p2wintext = font.Font("Retrofont.ttf", 100).render("Player 2 Wins", True, (255, 255, 255))
            window.blit(p2wintext, (300, 400))
            time.wait(5000)
            game = False
        if ball.rect.x > 1000:
            ball.speed_x -= 1
            ball.score(ball)
            ball.scorep2()
            time.wait(3000)
        if ball.rect.x < -100:
            ball.speed_x += 1
            ball.score(ball)
            ball.scorep1()
            time.wait(3000)
        if p1arrow_control == True:
            player1.p1arrows(player1)
        elif p1arrow_control == False:
            player1.p1WS(player1)
        player1.draw(window)
        player2.update()
        player2.draw(window)
        if p2arrow_control == True:
            player2.p2arrows(player2)
        elif p2arrow_control == False:
           player2.p2WS(player2)
        ball.draw(window)
        ball.move(window)
        display.update()
        clock.tick(60)
