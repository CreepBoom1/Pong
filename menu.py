import pygame
import time
import random
from pygame import *
from game import *

music = True
sound = True
theme1 = True
theme2 = False
theme3 = False
theme4 = False
theme5 = False
p1wsmovement = True
p1arrowmovement = False
p2wsmovement = False
p2arrowmovement = True
pygame.init()
mixer.init()
init()
mixer_music.load("sounds/Relief.mp3")
mixer_music.set_volume(0.5)
mixer_music.play()
click = mixer.Sound("sounds/ponghit.mp3")
click.set_volume(0.1)
window = pygame.display.set_mode((1000,800))
window.fill((0,0,0))
clock = pygame.time.Clock()
pressed_keys = key.get_pressed()
#---------------------------------------------------Classes--------------------------------------------------------------
class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = (0,0,0)
        if color:
            self.fill_color = color
    def color(self, new_color):
        self.fill_color = new_color
    def fill(self):
        pygame.draw_rect(window, self.fill_color, self.rect)

class Picture(Area):
    def __init__(self, filename, x=0, y=0, width=10, height=5, color=None):
        Area.__init__(self, x, y, width ,height ,color)
        self.image = pygame.image.load(filename)
    def draw_picture(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Label(Area):
    def set_text(self, text, fsize, text_color = (255,255,255)):
        self.text = text
        self.image = pygame.font.Font("Retrofont.ttf", fsize).render(text, True, text_color)
    def draw_text(self, shift_x = 0, shift_y = 0):
        window.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))
#-----------------------------------Label and Picture wall--------------------------------------------------------------
menu_title_text = Label(120, 50, 300, 150)
menu_title_text.set_text("Pongtastic v1.0", 80)
menu_vsplayer = Picture("sprites/button_vsplayer.png", 250,250,200,200)
menu_vscomputer = Picture("sprites/button_vscomputer.png", 550, 250, 200, 200)
menu_info = Picture("sprites/button_info.png", 100, 500, 200, 200)
menu_settings = Picture("sprites/button_settings.png", 400, 500,200,200)
menu_exit = Picture("sprites/button_exit.png", 700, 500, 200, 200)
pause_text = Label(500, 400, 100, 100)
pause_text.set_text("Pause", 60)
settings_back = Picture("sprites/back.png", 20, 20, 50, 50)
settings_music = Picture("sprites/on.png", 750, 90, 100, 100)
settings_sound = Picture("sprites/on.png", 750, 290, 100, 100)
settings_music_text = Label(250, 100, 300, 150)
settings_music_text.set_text("Music", 60)
settings_sound_text = Label(250, 280, 300, 150)
settings_sound_text.set_text("Sound", 60)
settings_theme_text = Label(50, 500, 300, 150)
settings_theme_text.set_text("Theme", 60)
settings_theme_note = Label(50, 700, 300, 150)
settings_theme_note.set_text("Note: it will be applied on the first game you play", 20)
settings_theme1 = Picture("sprites/on.png", 100, 600, 50, 50)
settings_theme1.image = pygame.transform.scale(settings_theme1.image, (50, 50))
settings_theme2 = Picture("sprites/off.png", 200, 600, 50, 50)
settings_theme2.image = pygame.transform.scale(settings_theme2.image, (50, 50))
settings_theme3 = Picture("sprites/off.png", 300, 600, 50, 50)
settings_theme3.image = pygame.transform.scale(settings_theme3.image, (50, 50))
settings_theme4 = Picture("sprites/off.png", 400, 600, 50, 50)
settings_theme4.image = pygame.transform.scale(settings_theme4.image, (50, 50))
settings_theme5 = Picture("sprites/off.png", 500, 600, 50, 50)
settings_theme5.image = pygame.transform.scale(settings_theme5.image, (50, 50))
info_back = Picture("sprites/back.png", 20, 20, 50, 50)
info_text1 = Label(200, 100, 300, 150)
info_text1.set_text("Pongtastic v1.0", 50)
info_text2 = Label(150, 250, 300, 150)
info_text2.set_text("WS/Arrow keys to move the platform", 30)
info_text3 = Label(150, 650, 300, 150)
info_text3.set_text("Game made by Ivan Bovenko", 30)
game_wsmovement = Picture("sprites/wscontrols.png", 560, 300, 50, 50)
game_wsmovement_trigger = Picture("sprites/on.png", 580, 500, 50, 50)
game_wsmovement_trigger.image = pygame.transform.scale(game_wsmovement_trigger.image, (50, 50))
game_arrowmovement = Picture("sprites/arrowcontrols.png", 760, 300, 100, 100)
game_arrowmovement.image = pygame.transform.scale(game_arrowmovement.image, (89, 178))
game_arrowmovement_trigger = Picture("sprites/off.png", 780, 500, 50, 50)
game_arrowmovement_trigger.image = pygame.transform.scale(game_arrowmovement_trigger.image, (50, 50))
game_wsmovement2 = Picture("sprites/wscontrols.png", 160, 300, 50, 50)
game_wsmovement2_trigger = Picture("sprites/off.png", 180, 500, 50, 50)
game_wsmovement2_trigger.image = pygame.transform.scale(game_wsmovement2_trigger.image, (50, 50))
game_arrowmovement2 = Picture("sprites/arrowcontrols.png", 360, 300, 50, 50)
game_arrowmovement2.image = pygame.transform.scale(game_arrowmovement2.image, (89, 178))
game_arrowmovement2_trigger = Picture("sprites/on.png", 380, 500, 50, 50)
game_arrowmovement2_trigger.image = pygame.transform.scale(game_arrowmovement2_trigger.image, (50, 50))
game_back = Picture("sprites/back.png", 20, 20, 200, 200)
game_play = Picture("sprites/play.png", 450, 650, 75, 75)
game_play.image = pygame.transform.scale(game_play.image, (75,75))
p1movement_text = Label(550, 650, 300, 150)
p1movement_text.set_text("Player 1 movement", 30)
p2movement_text = Label(50,650, 300, 150)
p2movement_text.set_text("Player 2 movement", 30)
vscomputer_text = Label(250, 50, 300, 150)
vscomputer_text.set_text("Player VS Computer", 40)
screen = "menu"
while True:
    window.fill((0, 0, 0))
#--------------------------------------------------------------------Menu-----------------------------------------------
    if screen == "menu":

        menu_info.draw_picture()
        menu_vsplayer.draw_picture()
        menu_vscomputer.draw_picture()
        menu_settings.draw_picture()
        menu_exit.draw_picture()
        menu_title_text.draw_text()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if menu_settings.rect.collidepoint(x, y):
                    screen = "settings"
                    click.play()
                if menu_exit.rect.collidepoint(x,y):
                    pygame.quit()
                    click.play()
                if menu_info.rect.collidepoint(x,y):
                    screen = "info"
                    click.play()
                if menu_vscomputer.rect.collidepoint(x,y):
                    click.play()
                    screen = "vscomputer"

                if menu_vsplayer.rect.collidepoint(x,y):
                    click.play()
                    screen = "vsplayer"


    elif screen == "pause":
        pause_text.draw_text()
    elif screen == "info":
#-------------------------------------------Info------------------------------------------------------------------------
        info_back.draw_picture()
        info_text1.draw_text()
        info_text2.draw_text()
        info_text3.draw_text()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
            if info_back.rect.collidepoint(x, y):
                click.play()
                screen = "menu"
#------------------------------------Vs Computer------------------------------------------------------------------------
    elif screen == "vscomputer":

        game_wsmovement.draw_picture()
        game_wsmovement_trigger.draw_picture()
        game_arrowmovement.draw_picture()
        game_arrowmovement_trigger.draw_picture()
        game_back.draw_picture()
        game_play.draw_picture()
        vscomputer_text.draw_text()
        p1movement_text.draw_text()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
            if game_back.rect.collidepoint(x,y):
                click.play()
                screen = "menu"
            if game_play.rect.collidepoint(x,y):
                click.play()
                if theme1 == True:
                    mixer_music.load("sounds/Relief.mp3")
                    mixer_music.set_volume(0.5)
                    if music == True:
                        mixer_music.play()
                elif theme2 == True:
                    mixer_music.load("sounds/Reign.mp3")
                    mixer_music.set_volume(0.5)
                    if music == True:
                        mixer_music.play()
                elif theme3 == True:
                    mixer_music.load("sounds/Tempest.mp3")
                    mixer_music.set_volume(0.5)
                    if music == True:
                        mixer_music.play()
                elif theme4 == True:
                    mixer_music.load("sounds/Challenge.mp3")
                    mixer_music.set_volume(0.5)
                    if music == True:
                        mixer_music.play()
                elif theme5 == True:
                    mixer_music.load("sounds/Tournament.mp3")
                    mixer_music.set_volume(0.5)
                    if music == True:
                        mixer_music.play()
                vscomputer_run(window, p1arrow_control)
                screen = "menu"
            if game_arrowmovement_trigger.rect.collidepoint(x,y) and p1arrowmovement == False:
                p1arrowmovement = True
                p1wsmovement = False
                p1arrow_control = True
                click.play()
                game_arrowmovement_trigger = Picture("sprites/on.png", 780, 500, 50, 50)
                game_arrowmovement_trigger.image = pygame.transform.scale(game_arrowmovement_trigger.image, (50, 50))
                game_wsmovement_trigger = Picture("sprites/off.png", 580, 500, 50, 50)
                game_wsmovement_trigger.image = pygame.transform.scale(game_wsmovement_trigger.image, (50, 50))
            elif game_wsmovement_trigger.rect.collidepoint(x,y) and p1wsmovement == False:
                p1arrowmovement = False
                p1wsmovement = True
                p1arrow_control = False
                click.play()
                game_wsmovement_trigger = Picture("sprites/on.png", 580, 500, 50, 50)
                game_wsmovement_trigger.image = pygame.transform.scale(game_wsmovement_trigger.image, (50, 50))
                game_arrowmovement_trigger = Picture("sprites/off.png", 780, 500, 50, 50)
                game_arrowmovement_trigger.image = pygame.transform.scale(game_arrowmovement_trigger.image, (50, 50))
#--------------------------------------------------VS PLAYER------------------------------------------------------------
    elif screen == "vsplayer":

        game_wsmovement.draw_picture()
        game_wsmovement2.draw_picture()
        game_wsmovement_trigger.draw_picture()
        game_wsmovement2_trigger.draw_picture()
        game_arrowmovement.draw_picture()
        game_arrowmovement2.draw_picture()
        game_arrowmovement_trigger.draw_picture()
        game_arrowmovement2_trigger.draw_picture()
        game_back.draw_picture()
        game_play.draw_picture()
        vscomputer_text.draw_text()
        p1movement_text.draw_text()
        p2movement_text.draw_text()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
            if game_back.rect.collidepoint(x,y):
                click.play()
                screen = "menu"
            if game_play.rect.collidepoint(x,y):
                click.play()
                if theme1 == True:
                    mixer_music.load("sounds/Relief.mp3")
                    mixer_music.set_volume(0.5)
                    if music == True:
                        mixer_music.play()
                elif theme2 == True:
                    mixer_music.load("sounds/Reign.mp3")
                    mixer_music.set_volume(0.5)
                    if music == True:
                        mixer_music.play()
                elif theme3 == True:
                    mixer_music.load("sounds/Tempest.mp3")
                    mixer_music.set_volume(0.5)
                    if music == True:
                        mixer_music.play()
                elif theme4 == True:
                    mixer_music.load("sounds/Challenge.mp3")
                    mixer_music.set_volume(0.5)
                    if music == True:
                        mixer_music.play()
                elif theme5 == True:
                    mixer_music.load("sounds/Tournament.mp3")
                    mixer_music.set_volume(0.5)
                    if music == True:
                        mixer_music.play()
                vsplayer_run(window, p1arrow_control, p2arrow_control)
                screen = "menu"
            if game_arrowmovement_trigger.rect.collidepoint(x,y) and p1arrowmovement == False:
                p1arrowmovement = True
                p1wsmovement = False
                p1arrow_control = True
                click.play()
                game_arrowmovement_trigger = Picture("sprites/on.png", 780, 500, 50, 50)
                game_arrowmovement_trigger.image = pygame.transform.scale(game_arrowmovement_trigger.image, (50, 50))
                game_wsmovement_trigger = Picture("sprites/off.png", 580, 500, 50, 50)
                game_wsmovement_trigger.image = pygame.transform.scale(game_wsmovement_trigger.image, (50, 50))
            elif game_wsmovement_trigger.rect.collidepoint(x,y) and p1wsmovement == False:

                p1arrowmovement = False
                p1wsmovement = True
                p1arrow_control = False
                click.play()
                game_wsmovement_trigger = Picture("sprites/on.png", 580, 500, 50, 50)
                game_wsmovement_trigger.image = pygame.transform.scale(game_wsmovement_trigger.image, (50, 50))
                game_arrowmovement_trigger = Picture("sprites/off.png", 780, 500, 50, 50)
                game_arrowmovement_trigger.image = pygame.transform.scale(game_arrowmovement_trigger.image, (50, 50))
            elif game_arrowmovement2_trigger.rect.collidepoint(x,y) and p2arrowmovement == False:
                p2arrowmovement = True
                p2wsmovement = False
                p2arrow_control = True
                click.play()
                game_arrowmovement2_trigger = Picture("sprites/on.png", 380, 500, 50, 50)
                game_arrowmovement2_trigger.image = pygame.transform.scale(game_arrowmovement2_trigger.image, (50, 50))
                game_wsmovement2_trigger = Picture("sprites/off.png", 180, 500, 50, 50)
                game_wsmovement2_trigger.image = pygame.transform.scale(game_wsmovement2_trigger.image, (50, 50))
            elif game_wsmovement2_trigger.rect.collidepoint(x,y) and p2wsmovement == False:
                p2arrowmovement = False
                p2wsmovement = True
                p2arrow_control = False
                click.play()
                game_wsmovement2_trigger = Picture("sprites/on.png", 180, 500, 50, 50)
                game_wsmovement2_trigger.image = pygame.transform.scale(game_wsmovement2_trigger.image, (50, 50))
                game_arrowmovement2_trigger = Picture("sprites/off.png", 380, 500, 50, 50)
                game_arrowmovement2_trigger.image = pygame.transform.scale(game_arrowmovement2_trigger.image, (50, 50))

#---------------------------------------------Settings------------------------------------------------------------------
    elif screen == "settings":

        settings_back.draw_picture()
        settings_music.draw_picture()
        settings_sound.draw_picture()
        settings_theme1.draw_picture()
        settings_theme2.draw_picture()
        settings_theme3.draw_picture()
        settings_theme4.draw_picture()
        settings_theme5.draw_picture()
        settings_sound_text.draw_text()
        settings_music_text.draw_text()
        settings_theme_text.draw_text()
        settings_theme_note.draw_text()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if settings_music.rect.collidepoint(x,y) and music == False:
                    settings_music = Picture("sprites/on.png", 750, 90, 150, 100)
                    music = True
                    mixer.music.play()
                    click.play()
                elif settings_music.rect.collidepoint(x,y) and music == True:
                    settings_music = Picture("sprites/off.png", 750, 90, 150, 100)
                    music = False
                    mixer.music.stop()
                    click.play()
                if settings_sound.rect.collidepoint(x,y) and sound == False:
                    settings_sound = Picture("sprites/on.png", 750, 290, 100, 100)
                    sound = True
                    click.set_volume(0.3)
                    hit.set_volume(1)
                    click.play()

                elif settings_sound.rect.collidepoint(x,y) and sound == True:
                    settings_sound = Picture("sprites/off.png", 750, 290, 150, 100)
                    sound = False
                    click.set_volume(0)
                    hit.set_volume(0)
                    click.play()
                if settings_theme1.rect.collidepoint(x,y) and theme1 == False:
                    click.play()
                    settings_theme1 = Picture("sprites/on.png", 100, 600, 50, 50)
                    settings_theme1.image = pygame.transform.scale(settings_theme1.image, (50, 50))
                    settings_theme2 = Picture("sprites/off.png", 200, 600, 50, 50)
                    settings_theme2.image = pygame.transform.scale(settings_theme2.image, (50, 50))
                    settings_theme3 = Picture("sprites/off.png", 300, 600, 50, 50)
                    settings_theme3.image = pygame.transform.scale(settings_theme3.image, (50, 50))
                    settings_theme4 = Picture("sprites/off.png", 400, 600, 50, 50)
                    settings_theme4.image = pygame.transform.scale(settings_theme4.image, (50, 50))
                    settings_theme5 = Picture("sprites/off.png", 500, 600, 50, 50)
                    settings_theme5.image = pygame.transform.scale(settings_theme5.image, (50, 50))


                    theme1 = True
                    theme2 = False
                    theme3 = False
                    theme4 = False
                if settings_theme2.rect.collidepoint(x,y) and theme2 == False:
                    click.play()
                    settings_theme1 = Picture("sprites/off.png", 100, 600, 50, 50)
                    settings_theme1.image = pygame.transform.scale(settings_theme1.image, (50, 50))
                    settings_theme2 = Picture("sprites/on.png", 200, 600, 50, 50)
                    settings_theme2.image = pygame.transform.scale(settings_theme2.image, (50, 50))
                    settings_theme3 = Picture("sprites/off.png", 300, 600, 50, 50)
                    settings_theme3.image = pygame.transform.scale(settings_theme3.image, (50, 50))
                    settings_theme4 = Picture("sprites/off.png", 400, 600, 50, 50)
                    settings_theme4.image = pygame.transform.scale(settings_theme4.image, (50, 50))
                    settings_theme5 = Picture("sprites/off.png", 500, 600, 50, 50)
                    settings_theme5.image = pygame.transform.scale(settings_theme5.image, (50, 50))


                    theme1 = False
                    theme2 = True
                    theme3 = False
                    theme4 = False
                    theme5 = False
                if settings_theme3.rect.collidepoint(x,y) and theme3 == False:
                    click.play()
                    settings_theme1 = Picture("sprites/off.png", 100, 600, 50, 50)
                    settings_theme1.image = pygame.transform.scale(settings_theme1.image, (50, 50))
                    settings_theme2 = Picture("sprites/off.png", 200, 600, 50, 50)
                    settings_theme2.image = pygame.transform.scale(settings_theme2.image, (50, 50))
                    settings_theme3 = Picture("sprites/on.png", 300, 600, 50, 50)
                    settings_theme3.image = pygame.transform.scale(settings_theme3.image, (50, 50))
                    settings_theme4 = Picture("sprites/off.png", 400, 600, 50, 50)
                    settings_theme4.image = pygame.transform.scale(settings_theme4.image, (50, 50))
                    settings_theme5 = Picture("sprites/off.png", 500, 600, 50, 50)
                    settings_theme5.image = pygame.transform.scale(settings_theme5.image, (50, 50))


                    theme1 = False
                    theme2 = False
                    theme3 = True
                    theme4 = False
                    theme5 = False
                if settings_theme4.rect.collidepoint(x,y) and theme4 == False:
                    click.play()
                    settings_theme1 = Picture("sprites/off.png", 100, 600, 50, 50)
                    settings_theme1.image = pygame.transform.scale(settings_theme1.image, (50, 50))
                    settings_theme2 = Picture("sprites/off.png", 200, 600, 50, 50)
                    settings_theme2.image = pygame.transform.scale(settings_theme2.image, (50, 50))
                    settings_theme3 = Picture("sprites/off.png", 300, 600, 50, 50)
                    settings_theme3.image = pygame.transform.scale(settings_theme3.image, (50, 50))
                    settings_theme4 = Picture("sprites/on.png", 400, 600, 50, 50)
                    settings_theme4.image = pygame.transform.scale(settings_theme4.image, (50, 50))
                    settings_theme5 = Picture("sprites/off.png", 500, 600, 50, 50)
                    settings_theme5.image = pygame.transform.scale(settings_theme5.image, (50, 50))


                    theme1 = False
                    theme2 = False
                    theme3 = False
                    theme4 = True
                    theme5 = False
                if settings_theme5.rect.collidepoint(x,y) and theme5 == False:
                    click.play()
                    settings_theme1 = Picture("sprites/off.png", 100, 600, 50, 50)
                    settings_theme1.image = pygame.transform.scale(settings_theme1.image, (50, 50))
                    settings_theme2 = Picture("sprites/off.png", 200, 600, 50, 50)
                    settings_theme2.image = pygame.transform.scale(settings_theme2.image, (50, 50))
                    settings_theme3 = Picture("sprites/off.png", 300, 600, 50, 50)
                    settings_theme3.image = pygame.transform.scale(settings_theme3.image, (50, 50))
                    settings_theme4 = Picture("sprites/off.png", 400, 600, 50, 50)
                    settings_theme4.image = pygame.transform.scale(settings_theme4.image, (50, 50))
                    settings_theme5 = Picture("sprites/on.png", 500, 600, 50, 50)
                    settings_theme5.image = pygame.transform.scale(settings_theme5.image, (50, 50))


                    theme1 = False
                    theme2 = False
                    theme3 = False
                    theme4 = False
                    theme5 = True
                if settings_back.rect.collidepoint(x,y):
                    screen = "menu"
                    click.play()



    clock.tick(60)
    pygame.display.update()



