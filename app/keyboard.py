from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import app


def keyboard_ASCII( key, x, y):
    '''
        Função indicada pra GLUT, que será executada sempre que um evento de teclado,
        que gere um caractere ASCII é criado
    '''
    if(key == b'a' or key == b'A'):
        if app.index_car > -3.3:
            app.index_car -= 0.05
            app.cam_x -= 0.05 
    elif(key == b'd' or key == b'D'):
        if app.index_car < 3.3:
            app.index_car += 0.05  
            app.cam_x += 0.05 
    elif(key == b'w' or key == b'W'):
        if app.road_speed >= 0 and app.road_speed <= 2:
            app.road_speed += 0.03 
    elif(key == b's' or key == b'S'):
        if app.road_speed > 0.05:
            app.road_speed -= 0.01
    
    glutPostRedisplay()


def special_keyboard( key, x, y):
    '''
        Função indicada pra GLUT, que será executada sempre que um evento de teclado,
        a partir de uma tecla especial é criado
    '''
    if(key == GLUT_KEY_LEFT):
        if app.index_car > -8:
            app.index_car -= 0.05
            app.cam_x -= 0.05
            app.cam_at_x -= 0.05

    elif(key == GLUT_KEY_RIGHT): 
        if app.index_car < 8:
            app.index_car += 0.05  
            app.cam_x += 0.05
            app.cam_at_x += 0.05

    if(key == GLUT_KEY_DOWN): 
        if app.road_speed > 0.05:
            app.road_speed -= 0.01
    elif(key == GLUT_KEY_UP): 
        if app.road_speed >= 0 and app.road_speed <= 2:
            app.road_speed += 0.03
        
    glutPostRedisplay() 

def keyboard_axis( key, x, y):
    '''
        Função para alterar valores do eixo da camera
    '''
    if(key == b'z'):  
        app.axis_z += 1
    elif(key == b'Z'):  
        app.axis_z -= 1
    elif(key == b'x'):  
        app.axis_x += 1
    elif(key == b'X'):  
        app.axis_x -= 1
    elif(key == b'y'): 
        app.axis_y += 1
    elif(key == b'Y'): 
        app.axis_y -= 1
    elif(key == b'b'): 
        app.at += 1
    elif(key == b'B'): 
        app.at -= 1
    
    glutPostRedisplay()
