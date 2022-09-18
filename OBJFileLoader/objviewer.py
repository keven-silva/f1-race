from OpenGL.GL import *
from OpenGL.GLU import *
from objloader import *

pygame.init()
display = (640, 480)

pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)
clock = pygame.time.Clock()

model = OBJ('/home/keven/Cursos/CG/T1-F1_Racer/objects/F1_car.obj')
box = model.box()
center = [(box[0][i] + box[1][i])/2 for i in range(3)]
size = [box[1][i] - box[0][i] for i in range(3)]
max_size = max(size)
distance = 10
scale = distance / max_size
angle = 0

glMatrixMode(GL_PROJECTION)
gluPerspective(90, (display[0]/display[1]), 0.1, distance*2)

glMatrixMode(GL_MODELVIEW)
glTranslatef(0.0, 0, -distance)

run = True
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    glPushMatrix()
    glRotate(angle, 0, 1, 0)
    glScale(scale, scale, scale)
    glTranslate(-center[0], -center[1], -center[2])
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    model.render()
    glPopMatrix()
    angle += 1
    
    pygame.display.flip()

pygame.quit()
quit()

