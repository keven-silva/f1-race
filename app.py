from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
from app.draw import draw_pygame
from app.keyboard import pygame_keyboard
from app.utils.components import factory_day, timer_pygame, car_accelerate_sound, background_sound
import app
import pygame as pg, threading


def main():
    pg.init()
    display = (1280,960)
    pg.display.set_mode(display, DOUBLEBUF | OPENGL)
    pg.display.set_caption('F1 Race')
    clock = pg.time.Clock()

    task = threading.Thread(target=factory_day, name='task1', daemon=True)
    sound = threading.Thread(target=background_sound, name='background_sound', daemon=True)

    task.start()
    sound.start()
    play = True

    while True:
        clock.tick(app.FPS)
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
                
        key = pg.key.get_pressed()
        if key:
            key_l = pg.key.get_pressed()[pg.K_LEFT]
            key_r = pg.key.get_pressed()[pg.K_RIGHT]
            key_up = pg.key.get_pressed()[pg.K_UP]
            key_down = pg.key.get_pressed()[pg.K_DOWN]

            pygame_keyboard(key_l, key_r, key_up, key_down)

        if app.road_speed > 0:
            car_accelerate_sound()

        draw_pygame()
        timer_pygame()
        pg.display.flip()
    

if __name__ == "__main__":
    main()