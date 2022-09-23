from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from app.scenery import Scenery

from OBJFileLoader import OBJ

import app


def draw():
    scenery = Scenery()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)                                # Sempre antes de desenhar qualquer coisa, deve-se limpar o frame-buffer
    # Carro principal
    car = OBJ('/home/keven/Cursos/CG/f1-race/objects/main_car/blue_car.obj')

    # Carros opositores
    oposite_car01 = OBJ('/home/keven/Cursos/CG/f1-race/objects/oposite_cars/red_car.obj')
    oposite_car02 = OBJ('/home/keven/Cursos/CG/f1-race/objects/oposite_cars/roxo_car.obj')
    oposite_car03 = OBJ('/home/keven/Cursos/CG/f1-race/objects/oposite_cars/yellow_car.obj')


    glMatrixMode(GL_PROJECTION)                                 # Comandos que determinam o tipo de visualização
    glLoadIdentity()
    glFrustum(-1, 1, -1, 1, 1, 500)                              # Definindo local da pespectiva
    
    glMatrixMode(GL_MODELVIEW)  
    glLoadIdentity()                          
    gluLookAt(0, -10, 4, 0, 0, 0, 0, -1, 1)                     # Configurando posição da câmera

    glPushMatrix()                                              #Salvando matriz
    glTranslatef(app.index_car, 0.0, 0.0)    
    scenery.fisrt_design(20, 20)                                # Inicializando cenário

    glPushMatrix()
    glTranslatef(0, app.road_index, 0)                         # Movimento de faixas centrais
    scenery.road_lane_center()
    glPopMatrix()
    
    # carro 01
    glPushMatrix()
    glTranslatef(0, app.car1, 0)                         # Movimento de faixas centrais
    glScale(0.5, 0.5, 0.5)
    oposite_car01 .render()
    glPopMatrix()

    #carro 02
    glPushMatrix()
    glTranslatef(3, app.car2, 0)                         # Movimento de faixas centrais
    glScale(0.5, 0.5, 0.5)
    oposite_car02 .render()
    glPopMatrix()

    #carro 03
    glPushMatrix()
    glTranslatef(-3, app.car3, 0)                         # Movimento de faixas centrais
    glScale(0.5, 0.5, 0.5)
    oposite_car03 .render()
    glPopMatrix()

    glPopMatrix()
    
    glPushMatrix()
    # # glRotate(app.angle, 0, 1, 0)                                # Rotação para mostrar o carro
    glTranslatef(0, -7, 0) 
    glScale(0.5, 0.5, 0.5)
    car.render()                                              # Rederizando o carro
    glPopMatrix()

    glFlush() #Todas as instruções anteriores apenas indicaram o que deve ser feito. Essa é a ordem pra GPU redesenhar com as informações enviadas
    glutSwapBuffers()