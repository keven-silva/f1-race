from OpenGL.GL import *
from OpenGL.GLUT import *


#Velocidade do jogo
FPS = 80          # frames por segundos

# janela
WIDTH =  960      # largura da janela
HEIGHT =  1280     # altura da janela

#Carros chegando
car1 = 30
car2 = -11
car3 = -11

#Pista
road_speed = 0
road_index = -2    # posição da pista central

index_car = 0

def init():
    glClearColor(0.2, 0.5, 1.50, 1.0) #indica qual cor será usada para limpar o frame buffer (normalmente usa uma cor de background)
