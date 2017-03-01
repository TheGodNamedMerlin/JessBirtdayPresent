import pygame as pg
from data import Tools, DropDownScene

class openingSceneState(object):

    def __init__(self):
        self.background01 = pg.image.load("data/images/Bedroom.png").convert_alpha()
        self.background02 = pg.image.load("data/images/backBanner.png").convert_alpha()
        self.background03 = pg.transform.flip(self.background02, True, False)

        self.change = False

        self.text = "Woah! im looking lit, huh whats that? "
        self.displayText = ""

        self.timer = 0
        self.stateTimer = 0
        self.currentCharacter = 0
        self.Scene2 = True
        self.Scene3 = True
        self.Scene4 = True
        self.Scene5 = True
        self.Scene6 = True
        self.Scene7 = True
        self.Scene8 = True
        self.Scene9 = True
        self.Scene10 = True

        self.character = 0
        self.characterSide = 0

        self.textManager = Tools.textBox_manager()

    def get_update(self, clock):
        if self.timer > self.currentCharacter and self.timer < len(self.text):
            self.displayText += self.text[self.currentCharacter]
            self.currentCharacter += 1

        if self.stateTimer == 60 and self.Scene2 == True:
            self.timer = 0
            self.displayText = ""
            self.currentCharacter = 0
            self.text = "Jess! you awake? Where are you? "
            self.Scene2 = False
            self.character = 1
            self.characterSide = 1

        if self.stateTimer == 120 and self.Scene3 == True:
            self.timer = 0
            self.displayText = ""
            self.currentCharacter = 0
            self.text = "I just woke up, home come whats up? "
            self.Scene3 = False
            self.character = 0
            self.characterSide = 0

        if self.stateTimer == 180 and self.Scene4 == True:
            self.timer = 0
            self.displayText = ""
            self.currentCharacter = 0
            self.text = "You dont remember? You must've been really drunk. "
            self.Scene4 = False
            self.character = 1
            self.characterSide = 1

        if self.stateTimer == 240 and self.Scene5 == True:
            self.timer = 0
            self.displayText = ""
            self.currentCharacter = 0
            self.text = "Your actually such a mole. "
            self.Scene5 = False
            self.character = 0
            self.characterSide = 0

        if self.stateTimer == 300 and self.Scene6 == True:
            self.timer = 0
            self.displayText = ""
            self.currentCharacter = 0
            self.text = "...... Anyway Lewis got lost in the bushes and "
            self.Scene6 = False
            self.character = 1
            self.characterSide = 1

        if self.stateTimer == 360 and self.Scene7 == True:
            self.timer = 0
            self.displayText = ""
            self.currentCharacter = 0
            self.text = "no one has seen him "
            self.Scene7 = False
            self.character = 1
            self.characterSide = 1

        if self.stateTimer == 400 and self.Scene8 == True:
            self.timer = 0
            self.displayText = ""
            self.currentCharacter = 0
            self.text = "Aw shit! again, i better go look for him "
            self.Scene8 = False
            self.character = 0
            self.characterSide = 0

        if self.stateTimer == 450 and self.Scene9 == True:
            self.timer = 0
            self.displayText = " "
            self.currentCharacter = 0
            self.text = "He was last seen going into the bush paddock "
            self.Scene9 = False
            self.character = 1
            self.characterSide = 1

        if self.stateTimer == 520 and self.Scene10 == True:
            self.timer = 0
            self.displayText = ""
            self.currentCharacter = 0
            self.text = "Okay, mmmmmmmmmbye. "
            self.Scene10 = False
            self.character = 0
            self.characterSide = 0

        if self.stateTimer >= 600:
            self.change = True

    def get_events(self, event):
        if event.type == pg.USEREVENT+1:
            if self.stateTimer >= 10:
                self.timer += 1
            self.stateTimer += 1


    def display_objects(self, window):
        window.blit(self.background01, (0,0))
        if self.stateTimer > 9:
            if self.characterSide == 0:
                window.blit(self.background03, (0,0))
            else:
                window.blit(self.background02, (0,0))
        if self.stateTimer >= 10:
            self.textManager.text_box(self.displayText, window, self.character, self.characterSide)

    def change_check(self):
        if self.change:
            return DropDownScene.openingSceneState()
        else:
            return False