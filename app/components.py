from OpenGL.GL import *
from OpenGL.GLUT import *
import app


def tree():
    newx = 0
    newy = 0

    glColor3f(0.65, 0.5, 0.5)
    glBegin(GL_TRIANGLES)
    glVertex3f(newx + 11, newy + 25, 4)
    glVertex3f(newx + 11, newy + 15, 0)
    glVertex3f(newx + 7, newy + 15, 0)
    glEnd()

    glColor3f(0.1, 0.27, 0.1)
    glBegin(GL_TRIANGLES)
    glVertex3f(newx + 11, newy + 28, 8)
    glVertex3f(newx + 15, newy + 22, 2)
    glVertex3f(newx + 7, newy + 22, 2)
    glEnd()