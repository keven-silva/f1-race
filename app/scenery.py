from OpenGL.GL import *
from app.utils.components import road_sky, side_lane, road_lane_center
from app.utils.colors import *


class Scenery():
    def __init__(self) -> None:
        pass    

    def fisrt_design(self, color:list):
        '''
            Cenario inicial
        '''
        vertex = [
            # Left
            (-100.0, 0.0, 0.0),
            (-100.0, 0.0, 1.0),
            (-100.0, 100.0, 1.0),
            (-100.0, 100.0, 0.0),
            # Right
            (100.0, 0.0, 0.0),
            (100.0, 0.0, 1.0),
            (100.0, 100.0, 1.0),
            (100.0, 100.0, 0.0),
            # Back
            (-100.0, 0.0, 0.0),
            (-100.0, 0.0, 1.0),
            (100.0, 0.0, 1.0),
            (100.0, 0.0, 0.0),
            # Front
            (-100.0, 100.0, 0.0),
            (-100.0, 100.0, 1.0),
            (100.0, 100.0, 1.0),
            (100.0, 100.0, 0.0),
            #Bottom
            (100.0, 0.0, 0.0),
            (100.0, 100.0, 0.0),
            (-100.0, 100.0, 0.0),
            (-100.0, 0.0, 0.0),
             # Top
            (100.0, 0.0, 1.0),
            (100.0, 100.0, 1.0),
            (-100.0, 100.0, 1.0),
            (-100.0, 0.0, 1.0),
        ]

        [glColor3f(c1, c2,c3) for c1, c2, c3 in  color]
        glBegin(GL_QUADS)
        [glVertex3f(v1, v2,v3) for v1, v2, v3 in  vertex]
        glEnd()

        self.road_design(
            vertex = [
                # Left
                (-10.0, 0.0, 1.0),
                (-10.0, 0.0, 1.1),
                (-10.0, 100.0, 1.1),
                (-10.0, 100.0, 1.0),
                # Right
                (10.0, 0.0, 1.0),
                (10.0, 0.0, 1.1),
                (10.0, 100.0, 1.1),
                (10.0, 100.0, 1.0),
                # # Front
                (10.0, 100.0, 1.0),
                (10.0, 100.0, 1.1),
                (-10.0, 100.0, 1.1),
                (-10.0, 100.0, 1.0),
                # Back
                (-10.0, 0.0, 1.0),
                (-10.0, 0.0, 1.1),
                (10.0, 0.0, 1.1),
                (10.0, 0.0, 1.0),
                # Botom
                (10.0, 0.0, 1.0),
                (10.0, 100.0, 1.0),
                (-10.0, 100.0, 1.0),
                (-10.0, 0.0, 1.0),
                # Top
                (10.0, 0.0, 1.1),
                (10.0, 100.0, 1.1),
                (-10.0, 100.0, 1.1),
                (-10.0, 0.0, 1.1)
                ], 
            color=[ROAD]) 
        self.factory_sky()

    # Road sky
    def factory_sky(self):
        '''
            Função responsavel por passar vertices e cores da nuvem
        '''
        vertex = [
             ( 5.0,10.0, 20.0),
            ( 6.0, 9.0, 20.0),
            ( 7.0, 9.0, 20.0),
            ( 8.0,10.0, 20.0),
            ( 8.0,11.0, 20.0),
            ( 7.0,12.0, 20.0),
            ( 6.0,12.0, 20.0),
            ( 5.0,11.0, 20.0),
        ]

        road_sky(vertex=vertex, color=[WHITE])

    # Road Desigh inm front page
    def road_design(self, vertex:list, color:list):
        '''
            Função responsavel por criar a pista
        '''
        glBegin(GL_QUADS) #a cada quatro pontos, conecte-os em quadrilátero
        [glColor3f(c1, c2,c3) for c1, c2, c3 in  color]
        [glVertex3f(v1, v2,v3) for v1, v2, v3 in  vertex]
        glEnd()
        
        #Faixa direita
        side_lane(
            vertex=[(10.0, 0.0, 1.1), 
                    (12, 0.0, 1.1), 
                    (12, 100.0, 1.1), 
                    (10.0, 100.0, 1.1)], 
            color=[SIDE_STRIPS])

        #Faixa esquerda
        side_lane(
            vertex=[(-10.0, 0.0, 1.1), 
                    (-12, 0.0, 1.1), 
                    (-12.0, 100.0, 1.1), 
                    (-10.0, 100.0, 1.1)], 
            color=[SIDE_STRIPS])
 
    def factory_road_lanes(self):  
        '''
            Gerando uma quantidade n de faixas centrais
        '''
        for l in range(0, 100, 10):
            road_lane_center(
                vertex=[(0.2, 1.0 + l, 1.1), 
                        (0.2, 6.0 + l, 1.1), 
                        (-0.2, 6.0 + l, 1.1), 
                        (-0.2, 1.0 + l, 1.1)], 
                color=[ROAD_LANE])
