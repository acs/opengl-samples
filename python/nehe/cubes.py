#!/usr/bin/env python3

from OpenGL.GL import *
from OpenGL.GLUT import *

from opengl_app import OpenGLApp


class Cubes(OpenGLApp):

    red = (1.0, 0.0, 0.0)
    dark_green = (0.0, 0.4, 0.0)
    light_green = (0.0, 0.4, 0.0)
    green = light_green
    blue = (0.0, 0.0, 1.0)
    yellow = (1.0, 1.0, 0.0)
    cyan = (0.0, 1.0, 1.0)
    white = (1.0, 1.0, 1.0)

    width = round(OpenGLApp.width * 1.5)

    def cube_square(self):
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
        glColor3f(*self.blue)
        glVertex3f(*top_front_left)
        glColor3f(*self.blue)
        glVertex3f(*top_front_right)
        glColor3f(*self.green)
        glVertex3f(*bottom_front_right)
        glColor3f(*self.green)
        glVertex3f(*bottom_front_left)

        # Right square
        glColor3f(*self.blue)
        glVertex3f(*top_front_right)
        glColor3f(*self.blue)
        glVertex3f(*top_back_right)
        glColor3f(*self.green)
        glVertex3f(*bottom_back_right)
        glColor3f(*self.green)
        glVertex3f(*bottom_front_right)

        # Back square
        glColor3f(*self.blue)
        glVertex3f(*top_back_right)
        glColor3f(*self.blue)
        glVertex3f(*top_back_left)
        glColor3f(*self.green)
        glVertex3f(*bottom_back_left)
        glColor3f(*self.green)
        glVertex3f(*bottom_back_right)

        # Left square
        glColor3f(*self.blue)
        glVertex3f(*top_back_left)
        glColor3f(*self.blue)
        glVertex3f(*top_front_left)
        glColor3f(*self.green)
        glVertex3f(*bottom_front_left)
        glColor3f(*self.green)
        glVertex3f(*bottom_back_left)

    # The main drawing function.
    def draw_gl_scene(self):
        self.rotation_triangle += 1

        # Clear The Screen And The Depth Buffer
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        scale = 1
        z_distance = 25*scale
        x_distance = 5

        for y in range(-2*scale, 3*scale):
            for x in range(-3*scale, 4*scale):
                glLoadIdentity()
                glTranslatef(x*x_distance, 3.0 * y, -z_distance)
                glRotatef(self.rotation_triangle, 1.0 * x, 1.0, 1.0)
                glBegin(GL_QUADS)
                self.cube_square()
                glEnd()

        glutSwapBuffers()


def main():
    Cubes().main()


if __name__ == '__main__':
    main()
