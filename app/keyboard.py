from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import app


#Função indicada pra GLUT que será executada sempre que um evento de teclado que gere um caractere ASCII é criado
def keyboard_ASCII( key, x, y):
    
    if(key == b'a' or key == b'A'):  #caso a seta esquerda seja pressionada, a coordenada x do ponto inferior esquerdo é reduzida, deslocando o quadrado pra esquerda
        if app.index_car < 3.3:
            app.index_car += 0.05 
    elif(key == b'd' or key == b'D'):  #caso a seta esquerda seja pressionada, a coordenada x do ponto inferior esquerdo é reduzida, deslocando o quadrado pra esquerda
        if app.index_car > -3.3:
            app.index_car -= 0.05  
    elif(key == b'w' or key == b'W'): #caso a tecla R seja pressionada, a componente vermelha é ligada ou desligada
        if app.road_speed >= 0 and app.road_speed <= 2:
            app.road_speed += 0.03 
    elif(key == b's' or key == b'S'): #caso a tecla G seja pressionada, a componente verde é ligada ou desligada
        if app.road_speed > 0.05:
            app.road_speed -= 0.01
    
    glutPostRedisplay() #Instrução que indica pra GLUT que o frame buffer deve ser atualizado


#Função indicada pra GLUT que será executada sempre que um evento de teclado a partir de uma tecla especial é criado
def special_keyboard( key, x, y):
    if(key == GLUT_KEY_LEFT):  #caso a seta esquerda seja pressionada, a coordenada x do ponto inferior esquerdo é reduzida, deslocando o quadrado pra esquerda
        if app.index_car < 3.3:
            app.index_car += 0.05  
    elif(key == GLUT_KEY_RIGHT): #caso a seta direita seja pressionada, a coordenada x do ponto inferior esquerdo é aumentada, deslocando o quadrado pra direita
        if app.index_car > -3.3:
            app.index_car -= 0.05  
    if(key == GLUT_KEY_DOWN):  #caso a seta pra baixo seja pressionada, a coordenada y do ponto inferior esquerdo é reduzida, deslocando o quadrado pra baixo
        if app.road_speed > 0.05:
            app.road_speed -= 0.01
    elif(key == GLUT_KEY_UP):   #caso a seta pra cima seja pressionada, a coordenada y do ponto inferior esquerdo é aumentada, deslocando o quadrado pra cima
        if app.road_speed >= 0 and app.road_speed <= 2:
            app.road_speed += 0.03
    glutPostRedisplay() #Instrução que indica pra GLUT que o frame buffer deve ser atualizado



