import pygame as pg



class textBox_manager(object):

    def __init__(self):

        self.font = font = pg.font.Font("data/images/01.TTF", 24)
        self.textbox = pg.image.load("data/images/textbox.png").convert_alpha()
        self.characters = [
            pg.image.load("data/images/character.png").convert_alpha(),
            pg.image.load("data/images/jodiePhone.png").convert_alpha(),
            pg.image.load("data/images/BooBoo.png").convert_alpha(),
            pg.transform.flip(pg.image.load("data/images/BooBoo.png").convert_alpha(), True, False),
            pg.image.load("data/images/Juile.png").convert_alpha()

        ]


    def text_box(self, text, window, charater, side):

        #side is 0 or 1. 0 = left and 1 = right

        renderText = self.font.render(text, True, (0,0,0))
        window.blit(self.characters[charater], (side*1030+-10, 76))
        window.blit(self.textbox, (0, 585))
        window.blit(renderText, (25, 621))
