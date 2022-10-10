from OpenGL.GL import *
from OpenGL.GLUT import *
from app.utils.colors import *
from OBJFileLoader import OBJ
import random, time, app


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