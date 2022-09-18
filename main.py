from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from app.draw import draw, ocioso
from app.keyboard import special_keyboard, keyboard_ASCII
import app
import pygame


def idle(value:int):
    glutPostRedisplay()

def main():
    pygame.init()
    glutInit()
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
    glutInitWindowPosition(200, 50)
    glutInitWindowSize(app.height, app.width)
    glutCreateWindow("F1 Race")

    app.init()
    
    glutDisplayFunc(draw)
    glutIdleFunc(ocioso)
    # glutKeyboardFunc(keyboard_ASCII)
    glutSpecialFunc(special_keyboard)
    glutTimerFunc((1000//app.fps), idle, 0)

    glutMainLoop()

if __name__ == "__main__":
    main()