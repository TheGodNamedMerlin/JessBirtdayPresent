import pygame as pg
import sys
from data import StateManager, IntroState


def run():

    pg.init()

    window = pg.display.set_mode((1280, 720))

    clock = pg.time.Clock()

    stateManager = StateManager.StateManager(IntroState.IntroState())

    running = True

    pg.time.set_timer(pg.USEREVENT+1, 100)

    while running:

        clock.tick(60)

        running = get_events(stateManager)

        get_update(stateManager, clock)

        display_objects(window, stateManager)


        pg.display.update()
        stateManager.change_check()

    pg.quit()
    sys.exit()


def get_events(stateManager):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            return False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_1:
                pg.time.set_timer(pg.USEREVENT+1, 50)

            elif event.key == pg.K_2:
                pg.time.set_timer(pg.USEREVENT+1, 100)


            elif event.key == pg.K_3:
                pg.time.set_timer(pg.USEREVENT+1, 10)


        stateManager.get_state_events(event)


    return True

def get_update(stateManager, clock):
    stateManager.get_state_update(clock)

def display_objects(window, statemanager):

    statemanager.display_state_objects(window)

run()