import pygame as pg
from data import Tools, Platformer02

class MikySceneState(object):

    def __init__(self):
        self.background01 = pg.image.load("data/images/Bedroom.png").convert_alpha()
        self.background02 = pg.image.load("data/images/backBanner.png").convert_alpha()
        self.background03 = pg.transform.flip(self.background02, True, False)

        self.change = False

        self.text = "Nice work jess! I think your ready for  "
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

        self.character = 4
        self.characterSide = 1

        self.textManager = Tools.textBox_manager()

    def get_update(self, clock):
        if self.timer > self.currentCharacter and self.timer < len(self.text):
            self.displayText += self.text[self.currentCharacter]
            self.currentCharacter += 1

        if self.stateTimer == 60 and self.Scene2 == True:
            self.timer = 0
            self.displayText = ""
            self.currentCharacter = 0
            self.text = "the next level of training. "
            self.Scene2 = False
            self.character = 4
            self.characterSide = 1

        if self.stateTimer == 120 and self.Scene3 == True:
            self.timer = 0
            self.displayText = ""
            self.currentCharacter = 0
            self.text = "nar fam, just kill me now. "
            self.Scene3 = False
            self.character = 0
            self.characterSide = 0

        if self.stateTimer == 180 and self.Scene4 == True:
            self.timer = 0
            self.displayText = ""
            self.currentCharacter = 0
            self.text = "I will take you to the next master so "
            self.Scene4 = False
            self.character = 2
            self.characterSide = 1

        if self.stateTimer == 240 and self.Scene5 == True:
            self.timer = 0
            self.displayText = ""
            self.currentCharacter = 0
            self.text = "you can learn the art of magic. "
            self.Scene5 = False
            self.character = 2
            self.characterSide = 1

        if self.stateTimer == 300 and self.Scene6 == True:
            self.timer = 0
            self.displayText = ""
            self.currentCharacter = 0
            self.text = "Cool like harry potter, Who teachers magic? "
            self.Scene6 = False
            self.character = 0
            self.characterSide = 0

        if self.stateTimer == 360 and self.Scene7 == True:
            self.timer = 0
            self.displayText = ""
            self.currentCharacter = 0
            self.text = "Magic Miky the all knowing all powerful Duck. "
            self.Scene7 = False
            self.character = 4
            self.characterSide = 1

        if self.stateTimer == 420 and self.Scene8 == True:
            self.timer = 0
            self.displayText = ""
            self.currentCharacter = 0
            self.text = "Do I get a wand and like a robe? "
            self.Scene8 = False
            self.character = 0
            self.characterSide = 0

        if self.stateTimer == 470 and self.Scene9 == True:
            self.timer = 0
            self.displayText = " "
            self.currentCharacter = 0
            self.text = "I mean of course all magic things wear robes. "
            self.Scene9 = False
            self.character = 4
            self.characterSide = 1

        if self.stateTimer == 550 and self.Scene10 == True:
            self.timer = 0
            self.displayText = ""
            self.currentCharacter = 0
            self.text = "Alright lets go then, I love robes. "
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
            return Platformer02.platformer()
        else:
            return False