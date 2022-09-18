from OpenGL.GL import *
from OpenGL.GLUT import *
import app


def tree(x, y):
    newx = x
    newy = y

    glColor3f(0.65, 0.5, 0.5)
    glBegin(GL_TRIANGLES)
    glVertex3f(newx + 11, newy + 45, -1.5)
    glVertex3f(newx + 13, newy + 35, -1.5)
    glVertex3f(newx + 10, newy + 35, -1.5)
    glEnd()

    glColor3f(0.1, 0.27, 0.1)
    glBegin(GL_TRIANGLES)
    glVertex3f(newx + 11, newy + 48, -1.5)
    glVertex3f(newx + 15, newy + 42, -1.5)
    glVertex3f(newx + 7, newy + 42, -1.5)
    glEnd()

def front_tire():
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_POLYGON)
    glVertex2f(app.index + 24, 5)
    glVertex2f(app.index + 24, 7)
    glVertex2f(app.index + 32, 7)
    glVertex2f(app.index + 32, 5)
    glEnd()

def back_tire():
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_POLYGON)
    glVertex2f(app.index + 24, 1)
    glVertex2f(app.index + 24, 3)
    glVertex2f(app.index + 32, 3)
    glVertex2f(app.index + 32, 1)
    glEnd()

def car_body():
    glColor3f(0.678, 1.0, 0.184)
    glBegin(GL_QUADS)
    glVertex2f(26, 8)
    glVertex2f(46, 8)
    # glVertex3f(0.0, 0.545, 0.545)

    glVertex2f(46, 8)
    glVertex2f(26, 8)
    # glVertex2f(30, 1)
    glEnd()

def start_game():
    #Road
    glColor3f(0.412, 0.412, 0.412)
    glBegin(GL_POLYGON)
    glVertex2f(20, 0)
    glVertex2f(20, 100)
    glVertex2f(80, 100)
    glVertex2f(80, 0)
    glEnd()
    #Road left border
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_POLYGON)
    glVertex2f(20, 0)
    glVertex2f(20, 100)
    glVertex2f(23, 100)
    glVertex2f(23, 0)
    glEnd()
    #Road right border
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_POLYGON)
    glVertex2f(77, 0)
    glVertex2f(77, 100)
    glVertex2f(80, 100)
    glVertex2f(80, 0)
    glEnd()
    #Road middel border: top
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_POLYGON)
    glVertex2f(48, app.road_top + 80)
    glVertex2f(48, app.road_top + 100)
    glVertex2f(52, app.road_top + 100)
    glVertex2f(52, app.road_top + 80)
    glEnd()
    
    app.road_top -= 1

    if app.road_top <- 100:
        app.road_top = 20
        app.score += 1
    #Road left border
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_POLYGON)
    glVertex2f(48, app.road_md + 40)
    glVertex2f(48, app.road_md + 60)
    glVertex2f(52, app.road_md + 60)
    glVertex2f(52, app.road_md + 40)
    glEnd()

    app.road_md -= 1

    if app.road_md <- 60:
        app.road_md = 60
        app.score += 1
    #Road right border
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_POLYGON)
    glVertex2f(48, app.road_btm + 0)
    glVertex2f(48, app.road_btm + 20)
    glVertex2f(52, app.road_btm + 20)
    glVertex2f(52, app.road_btm + 0)
    glEnd()

    app.road_btm -= 1
    if app.road_btm <- 20:
        app.road_btm = 100
        app.score += 1

    #Score board
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_POLYGON)
    glVertex2f(80, 97)
    glVertex2f(100, 97)
    glVertex2f(100, 98)
    glVertex2f(80, 98)
    glEnd()

    glColor3f(0.0, 1.0, 0.0)
    # .render_bitmap_string(80.5, 92 - 2, font, buf)

    if (app.score / 50) == 0:
        last = app.score / 50
        if last != app.level:
            app.level = app.score / 50
            app.fps = app.fps + 2 
