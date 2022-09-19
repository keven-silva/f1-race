from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from app.scenery import Scenery

from OBJFileLoader import OBJ

import app


def ocioso():
    # Controle de velocidade
    app.road_index -= app.road_speed
    app.car1 -= (app.road_speed + 0.0025)
    app.car2 -= app.road_speed
    app.car3 -= (app.road_speed + 0.001)

    if app.road_index <= -5:
        app.road_index = -1                        # Caso o valor da faixa central estiver na posição -10 do eixo y retorna para o valor "altura - 20"
        app.car1 = 4
        app.car2 = 0 
        app.car3 = 2

    if app.road_speed > 0.0005:
        app.road_speed -= 0.0003                                  # Decremento para uso na movimentação da faixa central
    else:
        app.road_speed = 0

    glutPostRedisplay()

def draw():
    scenery = Scenery()
    glClear(GL_COLOR_BUFFER_BIT)                                # Sempre antes de desenhar qualquer coisa, deve-se limpar o frame-buffer
    # Carro principal
    car = OBJ('/home/keven/Cursos/CG/f1-race/objects/F1_car.obj')
    box = car.box()
    size = [box[1][i] - box[0][i] for i in range(3)]
    max_size = max(size)
    distance = 12
    scale = distance / max_size

    # Carros opositores
    oposite_car01 = OBJ('/home/keven/Cursos/CG/f1-race/objects/F1-oposite_car01.obj')
    oposite_car02 = OBJ('/home/keven/Cursos/CG/f1-race/objects/F1-oposite_car02.obj')
    oposite_car03 = OBJ('/home/keven/Cursos/CG/f1-race/objects/F1-oposite_car03.obj')


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
    glTranslatef(0, app.road_index, 0)                         # Movimento de faixas centrais
    scenery.road_lane_center()
    glPopMatrix()
    
    #carro 01
    glPushMatrix()
    glTranslatef(0, app.car1, 0)                         # Movimento de faixas centrais
    glScale(scale - 1.5, scale - 1.5, scale - 1.5)
    oposite_car01 .render()
    glPopMatrix()

     #carro 02
    glPushMatrix()
    glTranslatef(-0.2, app.car2, 0)                         # Movimento de faixas centrais
    glScale(scale - 1.5, scale - 1.5, scale - 1.5)
    oposite_car02 .render()
    glPopMatrix()

     #carro 03
    glPushMatrix()
    glTranslatef(-0.5, app.car3, 0)                         # Movimento de faixas centrais
    glScale(scale - 1.5, scale - 1.5, scale - 1.5)
    oposite_car03 .render()
    glPopMatrix()

    glPopMatrix()
    
    glPushMatrix()
    # # glRotate(app.angle, 0, 1, 0)                                # Rotação para mostrar o carro
    glScale(scale - 1.65, scale - 1.65, scale - 1.65)
    car.render()                                              # Rederizando o carro
    glPopMatrix()

    glFlush() #Todas as instruções anteriores apenas indicaram o que deve ser feito. Essa é a ordem pra GPU redesenhar com as informações enviadas
    glutSwapBuffers()