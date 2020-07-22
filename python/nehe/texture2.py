#!/usr/bin/env python3

from OpenGL.GL import *
from OpenGL.GLUT import *

from opengl_app import OpenGLApp


class Texture1(OpenGLApp):

    def cube_square_texture(self):
        # We have 8 vertex: 4 top square, 4 for bottom square
        top_front_left = (-1.0, 1.0, 1.0)
        top_front_right = (1.0, 1.0, 1.0)
        top_back_left = (-1.0, 1.0, -1.0)
        top_back_right = (1.0, 1.0, -1.0)

        bottom_front_left = (-1.0, -1.0, 1.0)
        bottom_front_right = (1.0, -1.0, 1.0)
        bottom_back_left = (-1.0, -1.0, -1.0)
        bottom_back_right = (1.0, -1.0, -1.0)

        # Front square
        glTexCoord2f(0.0, 0.0)
        glVertex3f(*top_front_left)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(*top_front_right)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(*bottom_front_right)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(*bottom_front_left)

        # Right square
        glVertex3f(*top_front_right)
        glVertex3f(*top_back_right)
        glVertex3f(*bottom_back_right)
        glVertex3f(*bottom_front_right)

        # Back square
        glVertex3f(*top_back_right)
        glVertex3f(*top_back_left)
        glVertex3f(*bottom_back_left)
        glVertex3f(*bottom_back_right)

        # Left square
        glVertex3f(*top_back_left)
        glVertex3f(*top_front_left)
        glVertex3f(*bottom_front_left)
        glVertex3f(*bottom_back_left)

    def draw_gl_scene(self):
        # Clear The Screen And The Depth Buffer
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()  # Reset The View to the center

        glTranslatef(0.0, 0.0, -5.0)

        # To show the pyramid and cube let's rotate it a bit based on y-axis
        glRotatef(self.rotation_triangle, 1.0, 1.0, 1.0)
        self.rotation_triangle += 1

        # Draw a square (quadrilateral)
        glBegin(GL_QUADS)
        self.cube_square_texture()
        glEnd()  # We are done with the polygon

        # since this is double buffered, swap the buffers to display what just got drawn.
        glutSwapBuffers()


def main():
    Texture1().main()


if __name__ == '__main__':
    main()
