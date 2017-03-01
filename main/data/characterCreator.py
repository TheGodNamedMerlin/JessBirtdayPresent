import pygame as pg
from data import OpeningScene


class CharaterCreatorState(object):

    def __init__(self):

        #background handling
        self.background01 = pg.image.load("data/images/creatorCreationBackground.png").convert_alpha()
        self.background02 = pg.transform.flip(self.background01, True, False)
        self.background01Rect = self.background01.get_rect()
        self.background02Rect = self.background02.get_rect()
        self.background02Rect[0] += self.background01Rect[2]

        self.whenDone = pg.image.load("data/images/whenDone.png").convert_alpha()

        self.timer = 0
        self.scrollTime = 10


        #image handling
        self.baseBody = pg.image.load("data/images/baseBody.png").convert_alpha()

        self.headImages = get_headImages()
        self.headImagesId = 0

        self.bodyImages = get_bodyImages()
        self.bodyImagesId = 0

        self.legImages = get_legImages()
        self.legImagesId = 0

        self.save = False

        #button handling

        self.buttonGroup = pg.sprite.Group()

        #x, y, value, direction
        buttons = [
            [830, 122, 1, 0],
            [830, 312, 2, 0],
            [830, 502, 3, 0],
            [390, 122, 4, 2],
            [390, 312, 5, 2],
            [390, 502, 6, 2],
            [1000, 640, 7, 0]
        ]

        for button in buttons:
            self.buttonGroup.add(buttonSprite(button[0], button[1], button[2], button[3]))

        self.cooldown = 10

        self.change = False

    def get_update(self, clock):
        self.timer += clock.get_time()
        while self.timer >= self.scrollTime:
            self.timer -= self.scrollTime
            self.background01Rect[0] += -1
            self.background02Rect[0] += -1
        if self.background01Rect[0] <= -self.background01Rect[2]:
            self.background01Rect[0] = self.background01Rect[2]

        elif self.background02Rect[0] <= -self.background02Rect[2]:
            self.background02Rect[0] = self.background02Rect[2]

        if self.cooldown > 0:
            self.cooldown += -1

        if pg.mouse.get_pressed()[0]:
            mousePos = pg.mouse.get_pos()

            for button in self.buttonGroup:

                if button.get_value() == 1 and self.cooldown <= 0:
                    if buttonClick(button, mousePos) and self.headImagesId < len(self.headImages)-1:
                        self.headImagesId += 1
                        self.cooldown = 10

                elif button.get_value() == 4 and self.cooldown <= 0:
                    if buttonClick(button, mousePos) and self.headImagesId-1 >= 0:
                        self.headImagesId += -1
                        self.cooldown = 10

                elif button.get_value() == 2 and self.cooldown <= 0:
                    if buttonClick(button, mousePos) and self.bodyImagesId < len(self.bodyImages)-1:
                        self.bodyImagesId += 1
                        self.cooldown = 10

                elif button.get_value() == 5 and self.cooldown <= 0:
                    if buttonClick(button, mousePos) and self.bodyImagesId-1 >= 0:
                        self.bodyImagesId += -1
                        self.cooldown = 10

                elif button.get_value() == 3 and self.cooldown <= 0:
                    if buttonClick(button, mousePos) and self.legImagesId < len(self.legImages)-1:
                        self.legImagesId += 1
                        self.cooldown = 10

                elif button.get_value() == 6 and self.cooldown <= 0:
                    if buttonClick(button, mousePos) and self.legImagesId-1 >= 0:
                        self.legImagesId += -1
                        self.cooldown = 10

                elif button.get_value() == 7:
                    if buttonClick(button, mousePos):
                        self.save = True

    def display_objects(self, window):
        window.blit(self.background01, self.background01Rect)
        window.blit(self.background02, self.background02Rect)
        pg.draw.line(window, (255,255,255), (536, 0), (763, 720), 700)
        window.blit(self.whenDone, (1047, 558))
        window.blit(self.baseBody, (470, 65))
        window.blit(self.headImages[self.headImagesId], (470, 65))
        window.blit(self.bodyImages[self.bodyImagesId], (470, 255))
        window.blit(self.legImages[self.legImagesId], (470, 445))
        self.buttonGroup.draw(window)

        if self.save:
            character = window.subsurface((470, 65, 340, 590))
            pg.image.save(character, "data/images/character.png")
            self.change = True




    def get_events(self, event):
        pass

    def change_check(self):
        if self.change == True:
            return OpeningScene.openingSceneState()

        else:
            return False

def get_headImages():

    images = [
        pg.image.load("data/images/invisHead.png").convert_alpha(),
        pg.image.load("data/images/Head01.png").convert_alpha(),
        pg.image.load("data/images/Head02.png").convert_alpha(),
        pg.image.load("data/images/Head03.png").convert_alpha(),
        pg.image.load("data/images/Head04.png").convert_alpha(),
        pg.image.load("data/images/Head05.png").convert_alpha(),
        pg.image.load("data/images/Head06.png").convert_alpha(),
        pg.image.load("data/images/Head07.png").convert_alpha(),
        pg.image.load("data/images/Head08.png").convert_alpha(),
        pg.image.load("data/images/Head09.png").convert_alpha(),
        pg.image.load("data/images/Head10.png").convert_alpha()
    ]

    return images

def get_bodyImages():

    images = [
        pg.image.load("data/images/invisHead.png").convert_alpha(),
        pg.image.load("data/images/Body01.png").convert_alpha(),
        pg.image.load("data/images/Body02.png").convert_alpha(),
        pg.image.load("data/images/Body03.png").convert_alpha(),
        pg.image.load("data/images/Body04.png").convert_alpha(),
        pg.image.load("data/images/Body05.png").convert_alpha(),
        pg.image.load("data/images/Body06.png").convert_alpha(),
        pg.image.load("data/images/Body07.png").convert_alpha(),
        pg.image.load("data/images/Body08.png").convert_alpha()
    ]

    return images

def get_legImages():

    images = [
        pg.image.load("data/images/invisHead.png").convert_alpha(),
        pg.image.load("data/images/Leg01.png").convert_alpha(),
        pg.image.load("data/images/Leg02.png").convert_alpha(),
        pg.image.load("data/images/Leg03.png").convert_alpha(),
        pg.image.load("data/images/Leg04.png").convert_alpha(),
        pg.image.load("data/images/Leg05.png").convert_alpha(),
        pg.image.load("data/images/Leg06.png").convert_alpha(),
        pg.image.load("data/images/Leg07.png").convert_alpha(),
        pg.image.load("data/images/Leg08.png").convert_alpha(),
        pg.image.load("data/images/Leg09.png").convert_alpha(),
        pg.image.load("data/images/Leg10.png").convert_alpha()
    ]

    return images

def buttonClick(button, mouse):
    pos = button.get_position()
    if mouse[0] > pos[0]:
        if mouse[1] > pos[1]:
            if mouse[0] < pos[2]:
                if mouse[1] < pos[3]:
                    return True

class buttonSprite(pg.sprite.Sprite):

    def __init__(self, x, y, value, direction):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load("data/images/arrow.png").convert_alpha()
        self.image = pg.transform.rotate(self.image, 90*direction)
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.value = value

    def get_value(self):
        return self.value

    def get_position(self):
        pos = [
            self.rect.topleft[0],
            self.rect.topleft[1],
            self.rect.bottomright[0],
            self.rect.bottomright[1]
        ]

        return pos

    def draw(self, window):
        window.blit(self.image, self.rect)
