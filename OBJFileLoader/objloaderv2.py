from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import pywavefront


class OBJ:
    def __init__(self, filename):
        self.filename = filename

    def render(self):
        scene = pywavefront.Wavefront(self.filename, collect_faces=True, create_materials=True)
        scene_box = (scene.vertices[0], scene.vertices[0])
        for vertex in scene.vertices:
            min_v = [min(scene_box[0][i], vertex[i]) for i in range(3)]
            max_v = [max(scene_box[1][i], vertex[i]) for i in range(3)]
            scene_box = (min_v, max_v)

        scene_size     = [scene_box[1][i]-scene_box[0][i] for i in range(3)]
        max_scene_size = max(scene_size)
        scaled_size    = 5
        scene_scale    = [scaled_size/max_scene_size for i in range(3)]
        scene_trans    = [-(scene_box[1][i]+scene_box[0][i])/2 for i in range(3)]

        glPushMatrix()
        glScalef(*scene_scale)
        glTranslatef(*scene_trans)

        for mesh in scene.mesh_list:
            glBegin(GL_TRIANGLES)
            for face in mesh.faces:
                for vertex_i in face:
                    glVertex3f(*scene.vertices[vertex_i])
            glEnd()

        glPopMatrix()
