import pygame as pg
from data import Tools, IntroNewWorld

class caveSceneState(object):

    def __init__(self):
        self.background01 = pg.image.load("data/images/Cavebackground01.png").convert_alpha()
        self.background02 = pg.image.load("data/images/backBanner.png").convert_alpha()
        self.background02 = pg.transform.flip(self.background02, True, False)
        self.background03 = pg.image.load("data/images/Cavebackground02.png").convert_alpha()
        self.baseBody = pg.image.load("data/images/character.png").convert_alpha()
        self.rotate = 0
        self.rect = self.baseBody.get_rect()


        self.change = False

        self.text = "LEWIS!?! You in here? Hello? "
        self.displayText = ""

        self.timer = 0
        self.stateTimer = 0
        self.currentCharacter = 0
        self.Scene2 = True
        self.Scene3 = True
        self.Scene4 = True

        self.character = 0
        self.characterSide = 0

        self.textManager = Tools.textBox_manager()

        self.disText = True

        self.spin = False

    def get_update(self, clock):
        if self.timer > self.currentCharacter and self.timer < len(self.text):
            self.displayText += self.text[self.currentCharacter]
            self.currentCharacter += 1

        if self.stateTimer == 60 and self.Scene2 == True:
            self.timer = 0
            self.displayText = ""
            self.currentCharacter = 0
            self.text = "Whats that glow? "
            self.Scene2 = False
            self.character = 0
            self.characterSide = 0

        if self.stateTimer == 120 and self.Scene3 == True:
            self.timer = 0
            self.displayText = ""
            self.currentCharacter = 0
            self.text = "aaaaaaaaaaaaaa!?!??! It's sucking me in! "
            self.Scene3 = False
            self.character = 0
            self.characterSide = 0

        if self.stateTimer >= 180 and self.Scene4 == True:
            self.jess = pg.transform.rotozoom(self.baseBody, self.rotate, 0.5)
            self.rotate += 1
            self.spin = True

        if self.stateTimer >= 240:
            self.change = True

    def get_events(self, event):
        if event.type == pg.USEREVENT+1:
            if self.stateTimer >= 10:
                self.timer += 1
            self.stateTimer += 1


    def display_objects(self, window):
        window.blit(self.background01, (0,0))
        if self.stateTimer > 9:
                window.blit(self.background02, (0,0))
        if self.stateTimer >= 10:
            if self.disText:
                self.textManager.text_box(self.displayText, window, self.character, self.characterSide)

        if self.spin:
            window.blit(self.background03, (0,0))
            window.blit(self.jess, (420, 240))

    def change_check(self):
        if self.change:
            return IntroNewWorld.IntroNewWorld()
        else:
            return False