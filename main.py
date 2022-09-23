from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from app.draw import draw 
from app.keyboard import special_keyboard, keyboard_ASCII
import app
import pygame


def timer(value:int):
    glutTimerFunc(1000//app.FPS, timer, 0)
    app.road_index -= app.road_speed
    glEnable(GL_DEPTH_TEST)

    app.road_index -= app.road_speed
    

    if app.road_index <= -10:
        app.road_index = -3                                       # Caso o valor da faixa central estiver na posição -10 do eixo y retorna para o valor "altura - 20"
    if app.road_speed > 0: 
        if app.car3 <= 20 and app.car3 >= -1:    
            app.car1 = 50
        if app.car1 <= 20 and app.car1 >= -1:    
            app.car2 = 50
        if app.car2 <= 20 and app.car2 >= -1:      
            app.car3 = 50

    if app.road_speed > 0.05:
        app.road_speed -= 0.03                                  # Decremento para uso na movimentação da faixa central
        app.car1 -= 0.4
        app.car2 -= 0.6
        app.car3 -= 0.8
    else:
        app.road_speed = 0

    glutPostRedisplay()


def main():
    pygame.init()
    glutInit()
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
    glutInitWindowPosition(200, 50)
    glutInitWindowSize(app.HEIGHT, app.WIDTH)
    glutCreateWindow("F1 Race")

    app.init()
    
    glutDisplayFunc(draw)
    glutKeyboardFunc(keyboard_ASCII)
    glutSpecialFunc(special_keyboard)
    glutTimerFunc(1000//app.FPS, timer, 0)
    glutMainLoop()

if __name__ == "__main__":
    main()