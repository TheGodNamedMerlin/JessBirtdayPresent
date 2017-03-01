import pygame as pg
from data import Tools, Training

class MeetingJuileSceneState(object):

    def __init__(self):
        self.background01 = pg.image.load("data/images/MeetingJuileBackground.png").convert_alpha()
        self.background02 = pg.image.load("data/images/backBanner.png").convert_alpha()
        self.background03 = pg.transform.flip(self.background02, True, False)

        self.change = False

        self.text = "As you have requested master, I brang Jess here. "
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

        self.character = 3
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
            self.text = "Boo who is this? "
            self.Scene2 = False
            self.character = 0
            self.characterSide = 0

        if self.stateTimer == 120 and self.Scene3 == True:
            self.timer = 0
            self.displayText = ""
            self.currentCharacter = 0
            self.text = "You dont know? Why its genjutsu Julie! "
            self.Scene3 = False
            self.character = 3
            self.characterSide = 0

        if self.stateTimer == 180 and self.Scene4 == True:
            self.timer = 0
            self.displayText = ""
            self.currentCharacter = 0
            self.text = "Jess, Welcome to my dojo. I hope your ready to train. "
            self.Scene4 = False
            self.character = 4
            self.characterSide = 1

        if self.stateTimer == 240 and self.Scene5 == True:
            self.timer = 0
            self.displayText = ""
            self.currentCharacter = 0
            self.text = "Train? What am I training for? "
            self.Scene5 = False
            self.character = 0
            self.characterSide = 0

        if self.stateTimer == 300 and self.Scene6 == True:
            self.timer = 0
            self.displayText = ""
            self.currentCharacter = 0
            self.text = "Your bae lewis, has been captured by a witch "
            self.Scene6 = False
            self.character = 4
            self.characterSide = 1

        if self.stateTimer == 360 and self.Scene7 == True:
            self.timer = 0
            self.displayText = ""
            self.currentCharacter = 0
            self.text = "and its upto you to stop her and save everyone. "
            self.Scene7 = False
            self.character = 4
            self.characterSide = 1

        if self.stateTimer == 420 and self.Scene8 == True:
            self.timer = 0
            self.displayText = ""
            self.currentCharacter = 0
            self.text = "Why can't you save Lewis your like a ninja? "
            self.Scene8 = False
            self.character = 0
            self.characterSide = 0

        if self.stateTimer == 470 and self.Scene9 == True:
            self.timer = 0
            self.displayText = " "
            self.currentCharacter = 0
            self.text = "This may be true but i have stuffed my leg "
            self.Scene9 = False
            self.character = 4
            self.characterSide = 1

        if self.stateTimer == 530 and self.Scene10 == True:
            self.timer = 0
            self.displayText = ""
            self.currentCharacter = 0
            self.text = "So the duty falls on you. "
            self.Scene10 = False
            self.character = 4
            self.characterSide = 1

        if self.stateTimer == 590 and self.Scene11 == True:
            self.timer = 0
            self.displayText = ""
            self.currentCharacter = 0
            self.text = "RRRRRiiiigggghhhhtttt..... Well i guess we better start. "
            self.Scene11 = False
            self.character = 0
            self.characterSide = 0

        if self.stateTimer >= 650:
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
            return Training.TrainingSceneState()
        else:
            return False