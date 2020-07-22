#!/usr/bin/env python3

from OpenGL.GL import *
from OpenGL.GLUT import *

from opengl_app import OpenGLApp


class Pyramids(OpenGLApp):

    red = (1.0, 0.0, 0.0)
    dark_green = (0.0, 0.4, 0.0)
    light_green = (0.0, 0.4, 0.0)
    green = light_green
    blue = (0.0, 0.0, 1.0)
    yellow = (1.0, 1.0, 0.0)
    cyan = (0.0, 1.0, 1.0)
    white = (1.0, 1.0, 1.0)

    width = round(OpenGLApp.width * 1.5)

    def pyramid_square(self):
        # We have 5 vertex: top, and the 4 for the square base
        top = (0.0, 1.0, 0.0)
        front_left = (-1.0, -1.0, 1.0)
        front_right = (1.0, -1.0, 1.0)
        right_left = (1.0, -1.0, -1.0)
        right_right = front_right
        back_left = (-1.0, -1.0, -1.0)
        back_right = right_left
        left_left = front_left
        left_right = back_left

        # Front triangle
        glColor3f(*self.white)
        glVertex3f(*top)  # Top
        glColor3f(*self.green)
        glVertex3f(*front_left)  # Front Bottom Left
        glColor3f(*self.green)
        glVertex3f(*front_right)  # Front Bottom Right

        # Right Triangle
        glColor3f(*self.white)
        glVertex3f(*top)  # Top
        glColor3f(*self.green)
        glVertex3f(*right_right)  # Right Bottom Right
        glColor3f(*self.green)
        glVertex3f(*right_left)  # Right Bottom Left

        # Back Triangle
        glColor3f(*self.white)
        glVertex3f(*top)  # Top
        glColor3f(*self.green)
        glVertex3f(*back_right)  # Back Bottom Right
        glColor3f(*self.green)
        glVertex3f(*back_left)  # Back Bottom Left

        # Left Triangle
        glColor3f(*self.white)
        glVertex3f(*top)  # Top
        glColor3f(*self.green)
        glVertex3f(*left_right)  # Back Bottom Right
        glColor3f(*self.green)
        glVertex3f(*left_left)  # Back Bottom Left

    # The main drawing function.
    def draw_gl_scene(self):
        self.rotation_triangle += 1

        # Clear The Screen And The Depth Buffer
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        scale = 4
        z_distance = 25*scale
        x_distance = 5

        for y in range(-2*scale, 3*scale):
            for x in range(-3*scale, 4*scale):
                glLoadIdentity()
                glTranslatef(x*x_distance, 3.0 * y, -z_distance)
                glRotatef(self.rotation_triangle, 1.0 * x, 1.0, 1.0)
                glBegin(GL_TRIANGLES)
                self.pyramid_square()
                glEnd()

        glutSwapBuffers()


def main():
    Pyramids().main()


if __name__ == '__main__':
    main()
