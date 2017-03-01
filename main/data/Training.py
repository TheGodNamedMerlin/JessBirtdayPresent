import pygame as pg
from data import Tools, TalkingAboutMiky


class TrainingSceneState(object):

    def __init__(self):

        self.change = False
        self.timer = 0
        self.stateTimer = 0


        self.photos = [
            pg.image.load("data/images/Gym01.png").convert_alpha(),
            pg.image.load("data/images/Gym02.png").convert_alpha(),
            pg.image.load("data/images/Gym01.png").convert_alpha(),
            pg.image.load("data/images/Gym02.png").convert_alpha()
                ]



        self.UI = pg.image.load("data/images/TrainUi.png").convert_alpha()

        self.points = 1
        self.frame = 0
        self.slot = 0

        self.Scene2 = True
        self.Scene3 = True
        self.Scene4 = True
        self.Scene5 = True



    def get_update(self, clock):
        clock.tick(60)
        if self.stateTimer > 100:
            self.openingText = False
            self.gameStart = True

        if self.points > 94 and self.Scene2 == True:
            self.photos =[pg.image.load("data/images/Gym03.png").convert_alpha(),
            pg.image.load("data/images/Gym04.png").convert_alpha(),
            pg.image.load("data/images/Gym03.png").convert_alpha(),
            pg.image.load("data/images/Gym04.png").convert_alpha()
            ]

            self.Scene2 = False

        if self.points > 188 and self.Scene3 == True:
            self.photos =[pg.image.load("data/images/Gym05.png").convert_alpha(),
            pg.image.load("data/images/Gym06.png").convert_alpha(),
            pg.image.load("data/images/Gym05.png").convert_alpha(),
            pg.image.load("data/images/Gym06.png").convert_alpha()
            ]

            self.Scene3 = False

        if self.points > 282 and self.Scene4 == True:
            self.photos =[pg.image.load("data/images/Gym07.png").convert_alpha(),
            pg.image.load("data/images/Gym08.png").convert_alpha(),
            pg.image.load("data/images/Gym07.png").convert_alpha(),
            pg.image.load("data/images/Gym08.png").convert_alpha()
            ]

            self.Scene4 = False

        if self.points > 376 and self.Scene5 == True:
            self.photos =[pg.image.load("data/images/Gym09.png").convert_alpha(),
            pg.image.load("data/images/Gym10.png").convert_alpha(),
            pg.image.load("data/images/Gym09.png").convert_alpha(),
            pg.image.load("data/images/Gym10.png").convert_alpha()
            ]

            self.Scene5 = False



        if self.points >= 476:
            self.change = True



    def get_events(self, event):
        if event.type == pg.USEREVENT+1:
            if self.stateTimer >= 10:
                self.timer += 1
            self.stateTimer += 1



        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                self.points += 1
                self.frame += 1
                if self.frame > 3:
                    self.frame = 0
            if event.key == pg.K_6:
                self.points += 5




    def display_objects(self, window):
        window.blit(self.photos[self.frame], (0,0))
        pg.draw.rect(window, (255,255,255), (15, 10, 476, 116))
        pg.draw.rect(window, (255, 211, 38), (15, 10, self.points, 116))
        window.blit(self.UI, (0,0))

    def change_check(self):
        if self.change:
            return TalkingAboutMiky.MikySceneState()

        else:
            return False
