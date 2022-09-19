from OpenGL.GL import *
from OpenGL.GLUT import *


#Velocidade do jogo
fps = 800          # frames por segundos

# janela
width =  960      # largura da janela
height =  1280     # altura da janela

#Carros chegando
car1 = 4
car2 = 0 
car3 = 2

#Pista
road_speed = 0
road_index = 0     # posição da pista central


index_car = 0
angle = 0 
# index_lane = 0

# posx = 40
# posy = 53

#direção
# way_x = posx
# way_y = posy


def init():
    glClearColor(0.2, 0.5, 1.50, 1.0) #indica qual cor será usada para limpar o frame buffer (normalmente usa uma cor de background)
