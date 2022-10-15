from OpenGL.GL import *
from OpenGL.GLUT import *
from app.draw import draw_glut
from app.keyboard import keyboard_axis, special_keyboard
from app.utils.components import factory_day, timer_glut
import app
import pygame, threading


def main():
    pygame.init()
    glutInit()

    task = threading.Thread(target=factory_day, name='task1', daemon=True)
    task.start()

    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
    glutInitWindowPosition(200, 50)
    glutInitWindowSize(app.HEIGHT, app.WIDTH)
    glutCreateWindow("F1 Race")
     
    glutDisplayFunc(draw_glut)
    glutKeyboardFunc(keyboard_axis)
    glutSpecialFunc(special_keyboard)
    glutTimerFunc(1000//app.FPS, timer_glut, 0)
    
    glutMainLoop()

if __name__ == "__main__":
    main()