import pygame as pg
from data import Tools, Platformer01

class openingSceneState(object):

    def __init__(self):
        self.background01 = pg.image.load("data/images/MeetingBoobackground.png").convert_alpha()
        self.background02 = pg.image.load("data/images/backBanner.png").convert_alpha()
        self.background03 = pg.transform.flip(self.background02, True, False)

        self.change = False

        self.text = "Hello Jess, are you okay? "
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
        self.Scene11 = True
        self.Scene12 = True
        self.Scene13 = True
        self.Scene14 = True
        self.Scene15 = True


        self.character = 2
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
            self.text = "Boo! Your talking and your the size of a lion. "
            self.Scene2 = False
            self.character = 0
            self.characterSide = 0

        if self.stateTimer == 120 and self.Scene3 == True:
            self.timer = 0
            self.displayText = ""
            self.currentCharacter = 0
            self.text = "I'M BOO THE BARBARIAN, DEFENDER OF THE HOUSE OF SHARP! "
            self.Scene3 = False
            self.character = 2
            self.characterSide = 1

        if self.stateTimer == 180 and self.Scene4 == True:
            self.timer = 0
            self.displayText = ""
            self.currentCharacter = 0
            self.text = "lmao kay. "
            self.Scene4 = False
            self.character = 0
            self.characterSide = 0

        if self.stateTimer == 210 and self.Scene5 == True:
            self.timer = 0
            self.displayText = ""
            self.currentCharacter = 0
            self.text = "I got so many questions like where are we? "
            self.Scene5 = False
            self.character = 0
            self.characterSide = 0

        if self.stateTimer == 270 and self.Scene6 == True:
            self.timer = 0
            self.displayText = ""
            self.currentCharacter = 0
            self.text = "How do I get home? Oh and Lewis "
            self.Scene6 = False
            self.character = 0
            self.characterSide = 0

        if self.stateTimer == 330 and self.Scene7 == True:
            self.timer = 0
            self.displayText = ""
            self.currentCharacter = 0
            self.text = "Have you seen Lewis, BooBoo? "
            self.Scene7 = False
            self.character = 0
            self.characterSide = 0

        if self.stateTimer == 390 and self.Scene8 == True:
            self.timer = 0
            self.displayText = ""
            self.currentCharacter = 0
            self.text = "Slow down and i shall explain. "
            self.Scene8 = False
            self.character = 2
            self.characterSide = 1

        if self.stateTimer == 450 and self.Scene9 == True:
            self.timer = 0
            self.displayText = ""
            self.currentCharacter = 0
            self.text = "I have been sent by the one who feeds me to "
            self.Scene9 = False
            self.character = 2
            self.characterSide = 1

        if self.stateTimer == 510 and self.Scene10 == True:
            self.timer = 0
            self.displayText = ""
            self.currentCharacter = 0
            self.text = "find you, assist you in saving the king and "
            self.Scene10 = False
            self.character = 2
            self.characterSide = 1

        if self.stateTimer == 570 and self.Scene11 == True:
            self.timer = 0
            self.displayText = ""
            self.currentCharacter = 0
            self.text = "bring peace to the land. "
            self.Scene11 = False
            self.character = 2
            self.characterSide = 1

        if self.stateTimer == 630 and self.Scene12 == True:
            self.timer = 0
            self.displayText = ""
            self.currentCharacter = 0
            self.text = "Ah will I have time? i got work on Monday. "
            self.Scene12 = False
            self.character = 0
            self.characterSide = 0

        if self.stateTimer == 700 and self.Scene13 == True:
            self.timer = 0
            self.displayText = ""
            self.currentCharacter = 0
            self.text = "Will leave immediately, grab your things "
            self.Scene13 = False
            self.character = 2
            self.characterSide = 1

        if self.stateTimer == 770 and self.Scene14 == True:
            self.timer = 0
            self.displayText = ""
            self.currentCharacter = 0
            self.text = "Where are we going? "
            self.Scene14 = False
            self.character = 0
            self.characterSide = 0

        if self.stateTimer == 840 and self.Scene15 == True:
            self.timer = 0
            self.displayText = ""
            self.currentCharacter = 0
            self.text = "I am taking you to the one who feeds me "
            self.Scene15 = False
            self.character = 2
            self.characterSide = 1

        if self.stateTimer >= 900:
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
            return Platformer01.platformer()
        else:
            return False