import pygame as pg
from data import Tools, CaveScene
import random


class openingSceneState(object):

    def __init__(self):

        self.change = False
        self.timer = 0
        self.stateTimer = 0
        self.gameStart = False

        self.photos = [
            pg.image.load("data/images/Enemy01.png").convert_alpha(),
            pg.image.load("data/images/Enemy02.png").convert_alpha(),
            pg.image.load("data/images/Enemy03.png").convert_alpha()
        ]

        self.lindorWrapper = pg.image.load("data/images/lindorChocolate.png").convert_alpha()
        self.backgroundImage = pg.image.load("data/images/DropDownSceneBackground.png").convert_alpha()
        self.backBanner = pg.image.load("data/images/backBanner.png").convert_alpha()
        self.backBanner = pg.transform.flip(self.backBanner, True, False)

        self.deathScreen = pg.image.load("data/images/DeathScreen.png").convert_alpha()

        self.moveBackgroundImage01 = pg.image.load("data/images/DropDownSceneBackgroundMove.png").convert_alpha()
        self.moveBackgroundImage02 = pg.transform.flip(self.moveBackgroundImage01, False, True)
        self.backPos01 = [300, 0]
        self.backPos02 = [300, -720]

        self.textManager = Tools.textBox_manager()
        self.displayText = "Theres a trail of lindor wrappers, Lewis must be this way. "

        self.openingText = True

        self.objectPositions = [301, 527, 754]
        self.enemyGroup = pg.sprite.Group()

        self.player = Player()
        self.playerTracker = 1

        self.points = 0
        self.dead = False
        self.retry = False
        self.win = False

        self.font = font = pg.font.Font("data/images/01.TTF", 24)



    def get_update(self, clock):
        clock.tick(60)
        if self.stateTimer > 100:
            self.openingText = False
            self.gameStart = True

        self.backPos01[1] += 1
        if self.backPos01[1] >= 720:
            self.backPos01[1] = -720
        self.backPos02[1] += 1
        if self.backPos02[1] >= 720:
            self.backPos02[1] = -720

        if self.dead == False and self.win == False:
            self.player.update(self.objectPositions[self.playerTracker])
            self.enemyGroup.update()

            collList = pg.sprite.spritecollide(self.player, self.enemyGroup, True)
            for block in collList:
                if block.enemyCheck():
                    self.dead = True

                else:
                    self.points += 1

        if self.points == 10:
            self.win = True
            self.timer = 0
            self.points += 1


    def get_events(self, event):
        if event.type == pg.USEREVENT+1:
            if self.stateTimer >= 10:
                self.timer += 1
            self.stateTimer += 1

        if self.gameStart and self.win == False:
            if self.timer >= 17:
                N = random.randint(1, 5)
                if N == 4:
                    self.enemyGroup.add(Block(random.choice(self.objectPositions), self.lindorWrapper, False))

                else:
                    self.enemyGroup.add(Block(random.choice(self.objectPositions), random.choice(self.photos), True))

                self.timer = 0



            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    if self.objectPositions[self.playerTracker] == 301:
                        pass
                    else:
                        self.playerTracker += -1

                if event.key == pg.K_RIGHT:
                    if self.objectPositions[self.playerTracker] == 754:
                        pass
                    else:
                        self.playerTracker += 1

                if self.dead:
                    if event.key == pg.K_SPACE:
                        self.retry = True

                if event.key == pg.K_5:
                    self.change = True

        elif self.win:
            if self.timer >= 60:
                self.change = True




    def display_objects(self, window):
        window.blit(self.backgroundImage, (0,0))
        window.blit(self.moveBackgroundImage01, self.backPos01)
        window.blit(self.moveBackgroundImage02, self.backPos02)

        if self.dead == False and self.win == False:
            self.player.draw(window)
            self.enemyGroup.draw(window)

        elif self.dead:
            window.blit(self.backBanner, (0,0))
            self.textManager.text_box("AAAAAAAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHHHHHHHH! ", window, 0, 0)
            window.blit(self.deathScreen, (0,0))


        if self.stateTimer >= 10 and self.openingText:
            window.blit(self.backBanner, (0,0))
            self.textManager.text_box(self.displayText, window, 0, 0)

        if self.win:
            window.blit(self.backBanner, (0,0))
            self.textManager.text_box("Oh hey theirs a cave here, maybe Lewis is in there. ", window, 0, 0)

        display_text = self.font.render("Score:  "+ str(self.points), True, (0, 0, 0))
        window.blit(display_text, (1030, 20))

    def change_check(self):
        if self.retry:
            return openingSceneState()

        if self.change:
            return CaveScene.caveSceneState()

        else:
            return False


class Block(pg.sprite.Sprite):

    def __init__(self, x,  photo, Enemy, speed=10):
        super(Block, self).__init__()

        self.image = photo
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = -370

        self.speed = speed

        self.enemy = Enemy


    def update_position(self):
        self.rect.y += self.speed

    def enemyCheck(self):
        return self.enemy

    def update(self):
        self.update_position()

    def draw(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(pg.sprite.Sprite):

    def __init__(self):
        super(Player, self).__init__()

        self.image = pg.image.load("data/images/DropDownSceneJess.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 527
        self.rect.y = 630

    def update(self, pos):
        self.rect.x = pos

    def returnPos(self):
        return self.rect.x

    def draw(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))