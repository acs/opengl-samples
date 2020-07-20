#!/usr/bin/env python3

from OpenGL.GL import *
from OpenGL.GLUT import *

from opengl_app import OpenGLApp


class Lesson4(OpenGLApp):

    # The main drawing function.
    def draw_gl_scene(self):
        # Clear The Screen And The Depth Buffer
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()  # Reset The View to the center

        # Move Left 1.5 units and into the screen 6.0 units.
        glTranslatef(-1.5, 0.0, -6.0)

        glRotatef(self.rotation_triangle, 0.0, 1.0, 0.0)

        # Draw a triangle
        # glBegin(GL_POLYGON)  # Start drawing a polygon
        # https://community.khronos.org/t/drawing-speed-gl-triangles-vs-gl-polygon/59284
        glBegin(GL_TRIANGLES)  # Doing it as a triangle probably it is faster
        glColor3f(1.0, 0.0, 0.0)
        glVertex3f(0.0, 1.0, 0.0)  # Top
        glVertex3f(1.0, -1.0, 0.0)  # Bottom Right
        glColor3f(0.0, 1.0, 0.0)
        glVertex3f(-1.0, -1.0, 0.0)  # Bottom Left
        glEnd()  # We are done with the polygon

        glLoadIdentity()  # clean rotation

        # Move Right 1.5 units and to z -6.0
        glTranslatef(1.5, 0.0, -6.0)

        glRotatef(self.rotation_square, 1.0, 0.0, 0.0)
        # Draw a square (quadrilateral)
        glColor3f(0.5, 0.5, 1.0)
        glBegin(GL_QUADS)  # Start drawing a 4 sided polygon
        glVertex3f(-1.0, 1.0, 0.0)  # Top Left
        glVertex3f(1.0, 1.0, 0.0)  # Top Right
        glVertex3f(1.0, -1.0, 0.0)  # Bottom Right
        glVertex3f(-1.0, -1.0, 0.0)  # Bottom Left
        glEnd()  # We are done with the polygon

        glLoadIdentity()  # clean rotation

        #  since this is double buffered, swap the buffers to display what just got drawn.
        glutSwapBuffers()

        # update rotation
        self.rotation_triangle += 10
        self.rotation_square += 10


def main():
    Lesson4().main()


if __name__ == '__main__':
    main()
