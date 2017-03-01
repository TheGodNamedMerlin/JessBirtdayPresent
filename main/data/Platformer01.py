import pygame as pg
from data import MeetingJuile

class platformer(object):

    def __init__(self):

        self.timer = 0
        self.stateTimer = 0
        self.change = False
        self.retry = False

        self.player = Player()

        self.dead = False
        self.background = pg.image.load("data/images/JumpBooBackground.png").convert_alpha()
        self.deathScreen = pg.image.load("data/images/DeathScreen.png").convert_alpha()

        self.jump = True

        self.Enemy = pg.sprite.Group()
        self.Teleport = pg.sprite.Group()
        self.Walls01 = pg.sprite.Group()
        self.Walls02 = pg.sprite.Group()

        self.spikes = [
            [448, 557, 66, 19, 0, 0],
            [991, 557, 67, 19, 0, 0],
            [942, 366, 67, 19, 0, 0],
            [448, 365, 67, 20, 0, 0],
            [137, 140, 68, 19, 0, 0],
            [590, 141, 67, 19, 0, 0],
            [1052, 141, 66, 19, 0, 0]

        ]

        for enemy in self.spikes:
            self.Enemy.add(Block(enemy[0], enemy[1], enemy[2], enemy[3], enemy[4], enemy[5]))

        self.Walls01.add(Block(0, 576, 1363, 40, 0, 0))
        self.Walls01.add(Block(0, 384, 1280, 40, 0, 0))
        self.Walls01.add(Block(0, 160, 1280, 40, 0, 0))


        #x, y, width, height hitx hity
        self.Teleport.add(Block(1363, 385, 57, 192, 1363, 310))
        self.Teleport.add(Block(-140, 192, 57, 192, -140, 93))

        self.Endgate = Block(1400, 0, 57, 160, 0, 0)

    def get_update(self, clock):

        if self.dead == False:
            collList = pg.sprite.spritecollide(self.player, self.Enemy, True)
            for block in collList:
                self.dead = True

            collList = pg.sprite.spritecollide(self.player, self.Teleport, False)
            for block in collList:
                self.player.teleport(block.Hit())

            self.player.update(self.Walls01)

            if pg.sprite.collide_rect(self.player, self.Endgate):
                self.change = True



    def get_events(self, event):
        if event.type == pg.USEREVENT+1:
            if self.stateTimer >= 10:
                self.timer += 1
            self.stateTimer += 1

            self.player.update_image()

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                self.player.jumping()


            if event.key == pg.K_SPACE and self.dead:
                self.retry = True


    def display_objects(self, window):

        window.blit(self.background, (0,0))



        if self.dead:
            window.blit(self.deathScreen, (0,0))
        else:
            self.player.draw(window)

    def change_check(self):
        if self.retry:
            return platformer()

        if self.change:
            return MeetingJuile.MeetingJuileSceneState()
        else:
            return False

class Block(pg.sprite.Sprite):

    def __init__(self, x, y, width, height, hitx, hity):
        super(Block, self).__init__()

        self.image = pg.Surface((width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.hitx = hitx
        self.hity = hity

    def Hit(self):
        return (self.hitx, self.hity)


    def draw(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(pg.sprite.Sprite):

    def __init__(self):
        super(Player, self).__init__()

        self.frames = pg.image.load("data/images/RunningBoo.png").convert_alpha()
        self.image = pg.image.load("data/images/RunningBooBase.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = -125
        self.rect.y = 500
        self.currentImage = 0
        self.speed = 4
        self.direction = "right"

        self.jump = False

        # Set speed vector of player
        self.change_x = 0
        self.change_y = -3
        self.vel = 1

    def teleport(self, pos):
        self.rect.x, self.rect.y = pos
        self.frames = pg.transform.flip(self.frames, True, False)

        if self.speed == 4:
            self.speed = -4
        else:
            self.speed = 4

    def update(self, platform_list):

        self.rect.x += self.speed

        if self.jump:
            self.rect.y += self.change_y + self.vel
            self.vel += 0.08


            # Check and see if we hit anything
        block_hit_list = pg.sprite.spritecollide(self, platform_list, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y + self.vel > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y + self.vel < 0:
                self.rect.top = block.rect.bottom

            # Stop our vertical movement
            self.vel = 0.0
            self.jump = False

    def jumping(self):
        self.jump = True

    def update_image(self):
        if self.currentImage == 0:
            self.currentImage = 1
        else:
            self.currentImage = 0

    def draw(self, window):
        window.blit(self.frames, self.rect, (125*self.currentImage, 0, 125, 75))