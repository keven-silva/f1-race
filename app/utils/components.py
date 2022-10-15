from OpenGL.GL import *
from OpenGL.GLUT import *
from app.utils.colors import *
from OBJFileLoader.objloader import OBJ
import random, time, app, pygame as pg


def board()->None:
    '''
        Função que cria uma arvore geometrica
    '''
    try:
        board =  OBJ('/home/keven/Cursos/CG/f1-race/objects/Scenary/board.obj')
        glPushMatrix()
        glTranslatef(0.0, 0.0, 6.0)
        glRotatef(90, 1.0, 0.0, 0.0)
        board.render()
        glPopMatrix()
    except:
        raise ValueError('Error ao gerar a placa')

def side_lane(vertex:list, color:list) -> None:
    '''
        Função que cria as faixas laterais da pista
    '''
    try:
        [glColor3f(v1, v2,v3) for v1, v2, v3 in  color]
        glBegin(GL_QUADS)
        [glVertex3f(v1, v2,v3) for v1, v2, v3 in  vertex]
        glEnd()
    except:
        raise ValueError('Error ao tentar gerar faixas centrais')
        
def road_lane_center(vertex:list, color:list) -> None:
    '''
        Função que cria as faixas centrais da pista
    '''
    try:
        [glColor3f(c1, c2,c3) for c1, c2, c3 in  color]
        glBegin(GL_QUADS)
        [glVertex3f(v1, v2,v3) for v1, v2, v3 in  vertex]
        glEnd()
    except:
        raise ValueError('Error ao tentar gerar faixas centrais')

def hill(vertex:list, color:list):
    [glColor3f(c1, c2,c3) for c1, c2, c3 in  color]
    glBegin(GL_TRIANGLES)
    [glVertex3f(v1, v2,v3) for v1, v2, v3 in  vertex]
    glEnd()

def road_sky(vertex:list, color:list)->None:
    '''
        Função responsavel pelos elementos do céu
    '''
    try:  
        nuvens(vertex, color, -60, -40)
        nuvens(vertex, color, -20, 0)
        nuvens(vertex, color, 20, 40)        
    except:
        raise ValueError('Error ao gerar as nuvens')

def nuvens(vertex:list, color:list, x_near:int, x_far)->None:
    '''
        Função responsavel por gerar nuvens
    '''
    try:
        for axi_x in range(x_near, x_far, 2):
            for axi_z in range(10, 20, 5): 
                glPushMatrix()
                glTranslatef(axi_x, 60.0, axi_z)
                glRotatef(45, 1.0, 0.0, 0.0)
                [glColor3f(c1, c2,c3) for c1, c2, c3 in  color]
                glBegin(GL_POLYGON)
                [glVertex3f(v1, v2,v3) for v1, v2, v3 in  vertex]
                glEnd()
                glPopMatrix()
    except:
        raise ValueError('Error ao tentar gerar as nuvens')

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


def timer_glut(value:int):
    glutTimerFunc(1000//app.FPS, timer_glut, 0)
    glEnable(GL_DEPTH_TEST)

    app.road_index -= app.road_speed   
    app.board_index -= app.road_speed                             # Movimentação da placa

    if app.road_index <= -10:
        app.road_index = -3                                       # Caso o valor da faixa central estiver na posição -10 do eixo y retorna para o valor "altura - 20"
    
    if app.board_index <= 2:
        app.board_index = 100 
    
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

def timer_pygame():
    glEnable(GL_DEPTH_TEST)

    app.road_index -= app.road_speed   
    app.board_index -= app.road_speed                             # Movimentação da placa

    if app.road_index <= -10:
        app.road_index = -3                                       # Caso o valor da faixa central estiver na posição -10 do eixo y retorna para o valor "altura - 20"
    
    if app.board_index <= 2:
        app.board_index = 100 
    
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

    if app.road_speed > 0.1:
        app.road_speed -= 0.07                                  # Decremento para uso na movimentação da faixa central
    else:
        app.road_speed = 0

def sound_pygame():
    while True:
        sound = pg.mixer.Sound('sounds/rock01.aiff')
        sound.play()
        sound.set_volume(0.1)
        time.sleep(29)