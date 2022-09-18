from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from app.components import tree


class Scenery():
    
    def __init__(self) -> None:
        pass    

    def fisrt_design(self, zone_x, zone_y):
        #Road background
        glColor3f(0.2, 0.36, 0.1)
        glBegin(GL_QUADS) #a cada quatro pontos, conecte-os em quadriláteros
        glVertex3f(-zone_x, -1, 0)
        glVertex3f(zone_x, -1, 0)
        glVertex3f(zone_x, zone_y + 15, -50)
        glVertex3f(-zone_x, zone_y + 15, -50)
        glEnd()

        # tree(20, 20)   
        # tree(68, 20) 
        

    # #Road sky
    def road_sky(self, sky_x, sky_y):
        glColor3f(0.21, 0.62, 0.7)
        glBegin(GL_QUADS) #a cada quatro pontos, conecte-os em quadriláteros
        glVertex3f(0, sky_x + 4, 0)
        glVertex3f(sky_x + 40, sky_x + 4, 0)
        glVertex3f(sky_x + 40, sky_x + 40, -3)
        glVertex3f(0, sky_x + 40, -3)
        glEnd()

    # Road Desigh inm front page
    def road_design(self, road_x, road_y):
        glColor3f(0.2, 0.2, 0.2)
        glBegin(GL_QUADS) #a cada quatro pontos, conecte-os em quadriláteros
        glVertex3f(-road_x + 17, -1, 0)
        glVertex3f(road_x - 17, -1, 0)
        glVertex3f(road_x - 17, road_y + 15, -50)
        glVertex3f(-road_x + 17, road_y + 15, -50)
        glEnd()

        # Road lane left
        glColor3f(0.3, 0.0, 0.1)
        glBegin(GL_QUADS) #cada dois novos pontos são conectados aos dois últimos formando quadriláteros
        glVertex3f(-road_x + 16.8, -1, 0)
        glVertex3f(-road_x + 17.2, -1, 0)
        glVertex3f(-road_x + 17.3, road_y + 15, -50)
        glVertex3f(-road_x + 16.9, road_y + 15, -50)
        glEnd()

        # # Road lane right
        glColor3f(0.3, 0.0, 0.1)
        glBegin(GL_QUADS) #cada dois novos pontos são conectados aos dois últimos formando quadriláteros
        glVertex3f(road_x - 17.2, -1, 0)
        glVertex3f(road_x - 16.8, -1, 0)
        glVertex3f(road_x - 17.3, road_y + 15, -50)
        glVertex3f(road_x - 16.9, road_y + 15, -50)
        glEnd()
 
    def road_lane_center(self, index_x, lane_y):
        glColor3f(1.0, 1.0, 1.0)
        glBegin(GL_QUADS)
        glVertex3f(index_x - 2.1, lane_y - 5, 0)
        glVertex3f(index_x - 1.9, lane_y - 5, 0)
        glVertex3f(index_x - 1.9, lane_y - 2, -50)
        glVertex3f(index_x - 2.1, lane_y - 2, -50)
        glEnd()

    def hill(self):
        #Hill 1
        glColor3f(0.15, 0.17, 0.12)
        glBegin(GL_TRIANGLES)
        glVertex2f(20, 55)
        glVertex2f(27, 45)
        glVertex2f(0, 45)
        glEnd()

        #Hill 2
        glColor3f(0.198, 0.2, 0.16)
        glBegin(GL_TRIANGLES)
        glVertex2f(28, 75)
        glVertex2f(48, 55)
        glVertex2f(15, 55)
        glEnd()

        #Hill 3
        glColor3f(0.1, 0.402, 0.1)
        glBegin(GL_TRIANGLES)
        glVertex2f(77, 75)
        glVertex2f(90, 55)
        glVertex2f(62, 55)
        glEnd()

        #Hill 4
        glColor3f(0.135, 0.702, 0.243)
        glBegin(GL_TRIANGLES)
        glVertex2f(87, 65)
        glVertex2f(100, 55)
        glVertex2f(63, 55)
        glEnd()