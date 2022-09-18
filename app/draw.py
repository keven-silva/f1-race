from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from app.scenery import Scenery

from OBJFileLoader import OBJ

import app


def ocioso():
    app.road_index -= app.road_speed

    if app.road_index <= -2:
        app.road_index = -1                        # Caso o valor da faixa central estiver na posição -10 do eixo y retorna para o valor "altura - 20"
        
    if app.road_speed > 0.0005:
        app.road_speed -= 0.0003                                  # Decremento para uso na movimentação da faixa central
    else:
        app.road_speed = 0
    app.angle += 0.1
    glutPostRedisplay()

def draw():
    scenery = Scenery()
    glClear(GL_COLOR_BUFFER_BIT)                                # Sempre antes de desenhar qualquer coisa, deve-se limpar o frame-buffer

    model = OBJ('/home/keven/Cursos/CG/f1-race/objects/F1_car.obj')
    box = model.box()
    size = [box[1][i] - box[0][i] for i in range(3)]
    max_size = max(size)
    distance = 11
    scale = distance / max_size

    glMatrixMode(GL_PROJECTION)                                 # Comandos que determinam o tipo de visualização
    glLoadIdentity()
    gluPerspective(35, (app.height/app.width), 0.1, distance*2) # Configurando posição da câmera
    
    glMatrixMode(GL_MODELVIEW)  
    glLoadIdentity()
    glTranslatef(0, -3, -distance)                              # Definindo local da pespectiva
    # gluLookAt(0, -8, 0, 0, 0.086, 0, 0, 0, 1)

    glPushMatrix()                                              #Salvando matriz
    glTranslatef(app.index_car, 0.0, 0.0)    
    scenery.fisrt_design(20, 10)                                # Inicializando cenário
    scenery.road_design(20, 10)

    glPushMatrix()
    glTranslatef(0, app.road_index, -8)                         # Movimento de faixas centrais
    scenery.road_lane_center(2, 10)
    scenery.road_lane_center(2, 8)
    scenery.road_lane_center(2, 5)
    scenery.road_lane_center(2, 1)
    glPopMatrix()

    glPopMatrix()
    
    glPushMatrix()
    # # glRotate(app.angle, 0, 1, 0)                                # Rotação para mostrar o carro
    # gluLookAt(5,5,1,app.angle,0,0,0,0,1)                          # Definindo local da pespectiva
    # # glLoadIdentity()
    glScale(scale - 0.5, scale - 0.5, scale - 0.5)
    model.render()                                              # Rederizando o carro
    glPopMatrix()

    glFlush() #Todas as instruções anteriores apenas indicaram o que deve ser feito. Essa é a ordem pra GPU redesenhar com as informações enviadas
    glutSwapBuffers()