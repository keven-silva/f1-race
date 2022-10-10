from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from app.utils.colors import * 
from app.scenery import Scenery
from app.utils.components import board
from OBJFileLoader import OBJ
import app


def init():
    glClearColor((0.2 - app.init_color), (0.5 - app.init_color), (1.50 - app.init_color), 1.0) #indica qual cor será usada para limpar o frame buffer (normalmente usa uma cor de background)

def axis()->None:
    glBegin(GL_LINES)
    #eixo x em vermelho
    glColor3f(1,0,0)
    glVertex3f(0,0,0)
    glVertex3f(100,0,0)
    #eixo y em verde
    glColor3f(0,1,0)
    glVertex3f(0,0,0)
    glVertex3f(0,100,0)
    #eixo z em azul
    glColor3f(0,0,1)
    glVertex3f(0,0,0)
    glVertex3f(0,0,100)
    glEnd()

def draw():
    init()
    scenery = Scenery()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)                                # Sempre antes de desenhar qualquer coisa, deve-se limpar o frame-buffer
    
    glMatrixMode(GL_PROJECTION)                                 # Comandos que determinam o tipo de visualização
    glLoadIdentity()
    glFrustum(-1, 1, -1, 1, 1, 500)                              # Definindo local da pespectiva
    
    glMatrixMode(GL_MODELVIEW)  
    glLoadIdentity()                          
    gluLookAt(app.cam_x, app.cam_y, app.axis_z, app.cam_at_x, app.cam_at_y, 0, 0, -1, 1)                     # Configurando posição da câmera

    car = OBJ('/home/keven/Cursos/CG/f1-race/objects/main_car/blue_car.obj')

    # Carros opositores
    oposite_car01 = OBJ('/home/keven/Cursos/CG/f1-race/objects/oposite_cars/red_car.obj')
    oposite_car02 = OBJ('/home/keven/Cursos/CG/f1-race/objects/oposite_cars/roxo_car.obj')
    oposite_car03 = OBJ('/home/keven/Cursos/CG/f1-race/objects/oposite_cars/gray_car.obj')

    axis()           
    scenery.fisrt_design(color=[GRAM])                          # Inicializando cenário

    glPushMatrix()
    glTranslatef(-17.0, app.board_index, 0)                     # Movimento de faixas centrais
    board()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0, app.road_index, 0)                         # Movimento de faixas centrais
    scenery.factory_road_lanes()
    glPopMatrix()
    
    # carro 01
    glPushMatrix()
    glTranslatef(-5, app.car1, 1.1)                            # Movimento de faixas centrais
    glScale(1.5, 1.5, 1.5)
    oposite_car01.render()
    glPopMatrix()

    #carro 02
    glPushMatrix()
    glTranslatef(5, app.car2, 1.1)                             # Movimento de faixas centrais
    glScale(1.5, 1.5, 1.5)
    oposite_car02.render()
    glPopMatrix()

    #carro 03
    glPushMatrix()
    glTranslatef(-5, app.car3, 1.1)                            # Movimento de faixas centrais
    glScale(1.5, 1.5, 1.5)
    oposite_car03.render()
    glPopMatrix()
    
    glPushMatrix()
    glTranslatef(app.index_car, 5, 1.1) 
    glScale(1.5, 1.5, 1.5)
    car.render()                                              # Rederizando o carro
    glPopMatrix()

    glutSwapBuffers()   #Todas as instruções anteriores apenas indicaram o que deve ser feito. Essa é a ordem pra GPU redesenhar com as informações enviadas