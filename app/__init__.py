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

# Arvore
tree_index = 0

#Pista
road_speed = 0
road_index = -2    # posição da pista central

index_car = 0
# cor de fundo 
init_color = 0.0
