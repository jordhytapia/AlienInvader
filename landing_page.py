import pygame as pg
import sys
import os
from alien import AlienFleet, Alien
# from settings import Settings
from vector import Vector
from button import Button
from os import path

GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (130, 130, 130)

BG = pg.image.load(os.path.join("images","background-black.png"))
BG = pg.transform.scale(BG, (1200,900))



class LandingPage:
    alien_one_imgs = [pg.image.load(f'images/ditto{n}.png') for n in range(2)]
    alien_two_imgs = [pg.image.load(f'images/dratini{n}.png') for n in range(2)]
    alien_three_imgs = [pg.image.load(f'images/flygon{n}.png') for n in range(2)]
    ufo_imgs = [pg.image.load(f'images/deoxys{n}.png') for n in range(2)]

    def __init__(self, game):
        self.screen = game.screen
        self.landing_page_finished = False
        self.highScore = 0


        headingFont = pg.font.SysFont(None, 192)
        subheadingFont = pg.font.SysFont(None, 122)
        font = pg.font.SysFont(None, 48)

        strings = [('SPACE', WHITE, headingFont), ('INVADERS', WHITE, subheadingFont),
                ('= 10 PTS', WHITE, font), ('= 20 PTS', WHITE, font),
                            ('= 30 PTS', WHITE, font), ('= 100', WHITE, font),
               # ('PLAY GAME', GREEN, font),
                (f'HIGH SCORE: {self.highScore}', WHITE, font)]

        self.texts = [self.get_text(msg=s[0], color=s[1], font=s[2]) for s in strings]

        self.posns = [150, 230]
        alien = [60 * x + 400 for x in range(4)]
        play_high = [x for x in range(650, 760, 80)]
        play_high = 730
        self.posns.extend(alien)
        self.posns.append(730)

        centerx = self.screen.get_rect().centerx

        self.play_button = Button(self.screen, "PLAY GAME", ul=(centerx - 125, 650))


        n = len(self.texts)
        self.rects = [self.get_text_rect(text=self.texts[i], centerx=centerx, centery=self.posns[i]) for i in range(n)]
        self.alien_one = Alien(game=game, image_list=LandingPage.alien_one_imgs,
                               v=Vector(), ul=(centerx - 150, 365))
        self.alien_two = Alien(game=game, image_list=LandingPage.alien_two_imgs,
                               v=Vector(), ul=(centerx - 150, 425))
        self.alien_three = Alien(game=game, image_list=LandingPage.alien_three_imgs,
                               v=Vector(), ul=(centerx - 150, 490))
        self.ufo = Alien(game=game, image_list=LandingPage.ufo_imgs,
                               v=Vector(), ul=(centerx - 150, 565))

    def get_text(self, font, msg, color): return font.render(msg, True, color, BLACK)

    def get_text_rect(self, text, centerx, centery):
        rect = text.get_rect()
        rect.centerx = centerx
        rect.centery = centery
        return rect

    def check_events(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                sys.exit()
            if e.type == pg.KEYUP and e.key == pg.K_p:   # pretend PLAY BUTTON pressed
                self.landing_page_finished = True
            elif e.type == pg.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pg.mouse.get_pos()
                if self.play_button.rect.collidepoint(mouse_x, mouse_y):
                    self.landing_page_finished = True

    def update(self):       # TODO make aliens move
        pass

    def show(self):
        while not self.landing_page_finished:
            self.update()
            self.draw()
            self.check_events()   # exits game if QUIT pressed

    def draw_text(self):
        n = len(self.texts)
        for i in range(n):
            self.screen.blit(self.texts[i], self.rects[i])

    def draw(self):
        self.screen.blit(BG,(0,0))
        self.alien_one.draw()
        self.alien_two.draw()
        self.alien_three.draw()
        self.ufo.draw()
        self.draw_text()
        self.play_button.draw()
        self.loadData()
        # self.alien_fleet.draw()   # TODO draw my aliens
        # self.lasers.draw()        # TODO dray my button and handle mouse events
        pg.display.flip()

    def loadData(self):
        self.dir = path.dirname(__file__)
        with open(path.join(self.dir, "High_Score.txt"), 'w') as f:
            try:
                self.highScore = int(f.read())
            except:
                self.highScore = 200


