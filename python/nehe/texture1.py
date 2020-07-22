#!/usr/bin/env python3

from OpenGL.GL import *
from OpenGL.GLUT import *

from opengl_app import OpenGLApp


class Texture1(OpenGLApp):

    # The main drawing function.
    def draw_gl_scene(self):
        # Clear The Screen And The Depth Buffer
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()  # Reset The View to the center

        glTranslatef(0.0, 0.0, -3.0)

        # Draw a square (quadrilateral)
        glBegin(GL_QUADS)  # Start drawing a 4 sided polygon
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-1.0, 1.0, 0.0)  # Top Left
        glTexCoord2f(1.0, 0.0)
        glVertex3f(1.0, 1.0, 0.0)  # Top Right
        glTexCoord2f(1.0, 1.0)
        glVertex3f(1.0, -1.0, 0.0)  # Bottom Right
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-1.0, -1.0, 0.0)  # Bottom Left
        glEnd()  # We are done with the polygon

        # since this is double buffered, swap the buffers to display what just got drawn.
        glutSwapBuffers()


def main():
    Texture1().main()


if __name__ == '__main__':
    main()
