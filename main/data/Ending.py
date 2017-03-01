import pygame as pg

class EndingState(object):

    def __init__(self):


        self.finalText = "                           To be Continued..... "

        self.text = ""
        self.font = pg.font.Font("data/images/01.TTF", 24)
        self.renderText = self.font.render(self.text, True, (255,255,255))

        self.timer = 0
        self.stateTimer = 0

        self.currentCharacter = 10
        self.currentCharacter2 = 0

        self.change = False

    def get_update(self, clock):
        if self.timer > self.currentCharacter and self.currentCharacter < len(self.finalText):
            self.text += self.finalText[self.currentCharacter]
            self.currentCharacter += 1


        self.renderText = self.font.render(self.text, True, (255,255,255))


    def get_events(self, event):
        if event.type == pg.USEREVENT+1 :
            self.timer += 1
            self.stateTimer += 1


    def display_objects(self, window):
        window.fill((0, 0, 0))
        window.blit(self.renderText, (120, 260))

    def change_check(self):
        if self.change == True:
            return

        else:
            return False