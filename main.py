from OpenGL.GL import *
from OpenGL.GLUT import *
from app.draw import draw 
from app.keyboard import keyboard_axis, special_keyboard
import app
import pygame, time, threading


def change_to_day():
        app.init_color -= 0.03

        if app.init_color <= 0:
            app.day = True

def change_to_night():
        app.init_color += 0.03

        if app.init_color >= 1.5:
            app.day = False

def factory_day():
    while True:
        while app.day:
            time.sleep(0.5)
            change_to_night()

        while app.day == False:
            time.sleep(0.5)
            change_to_day()

        time.sleep(2)

def timer(value:int):
    glutTimerFunc(1000//app.FPS, timer, 0)
    glEnable(GL_DEPTH_TEST)

    app.road_index -= app.road_speed   
    app.board_index -= app.road_speed                             # Movimentação da placa

    if app.road_index <= -10:
        app.road_index = -3                                       # Caso o valor da faixa central estiver na posição -10 do eixo y retorna para o valor "altura - 20"
    
    if app.board_index <= 2:
        app.board_index = 60 
    
    # Movimentação dos carros
    if app.car1 <= 100:
        app.car1 += 1
        if app.road_speed > 0 and app.car1 >= 0:
            app.car1 -= app.road_speed
        if app.car1 >= 100: 
            app.car1 = 0

    if app.car2 <= 100:    
        app.car2 += 1.4
        if app.road_speed > 0 and app.car2 >= 0:
            app.car2 -= app.road_speed
        if app.car2 >= 100: 
            app.car2 = 0

    if app.car3 <= 100:    
        app.car3 += 1.6
        if app.road_speed > 0 and app.car3 >= 0:
            app.car3 -= app.road_speed
        if app.car3 >= 100: 
            app.car3 = 0

    if app.road_speed > 0.05:
        app.road_speed -= 0.03                                  # Decremento para uso na movimentação da faixa central
    else:
        app.road_speed = 0

    glutPostRedisplay()

def main():
    pygame.init()
    glutInit()

    task = threading.Thread(target=factory_day, name='task1', daemon=True)
    task.start()

    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
    glutInitWindowPosition(200, 50)
    glutInitWindowSize(app.HEIGHT, app.WIDTH)
    glutCreateWindow("F1 Race")
     
    glutDisplayFunc(draw)
    glutKeyboardFunc(keyboard_axis)
    glutSpecialFunc(special_keyboard)
    glutTimerFunc(1000//app.FPS, timer, 0)
    
    glutMainLoop()

if __name__ == "__main__":
    main()