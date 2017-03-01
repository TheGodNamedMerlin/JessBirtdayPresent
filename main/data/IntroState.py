import pygame as pg
from data import characterCreator

class IntroState(object):

    def __init__(self):


        self.finalText = "          eeerrr.... What happened last night.... What time"
        self.finalText2 = "                                                            is it? i better get dressed."
        self.text = ""
        self.text2 = ""
        self.font = pg.font.Font("data/images/01.TTF", 24)
        self.renderText = self.font.render(self.text, True, (255,255,255))
        self.renderText2 = self.font.render(self.text2, True, (255, 255,255))

        self.timer = 0
        self.stateTimer = 0

        self.currentCharacter = 10
        self.currentCharacter2 = 0

        self.change = False

    def get_update(self, clock):
        if self.timer > self.currentCharacter and self.currentCharacter < len(self.finalText):
            self.text += self.finalText[self.currentCharacter]
            self.currentCharacter += 1

        elif self.timer > self.currentCharacter2 and self.currentCharacter2 < len(self.finalText2):
            self.text2 += self.finalText2[self.currentCharacter2]
            self.currentCharacter2 += 1



        self.renderText = self.font.render(self.text, True, (255,255,255))
        self.renderText2 = self.font.render(self.text2, True, (255, 255,255))

        if self.stateTimer >= 95:
            self.change = True

    def get_events(self, event):
        if event.type == pg.USEREVENT+1 :
            self.timer += 1
            self.stateTimer += 1


    def display_objects(self, window):
        window.fill((0, 0, 0))
        window.blit(self.renderText, (120, 260))
        window.blit(self.renderText2, (-850, 360))

    def change_check(self):
        if self.change == True:
            return characterCreator.CharaterCreatorState()

        else:
            return False