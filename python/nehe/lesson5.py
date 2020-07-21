#!/usr/bin/env python3

from OpenGL.GL import *
from OpenGL.GLUT import *

from opengl_app import OpenGLApp


class Lesson5(OpenGLApp):

    red = (1.0, 0.0, 0.0)
    dark_green = (0.0, 0.4, 0.0)
    light_green = (0.0, 0.4, 0.0)
    green = dark_green
    blue = (0.0, 0.0, 1.0)
    yellow = (1.0, 1.0, 0.0)
    cyan = (0.0, 1.0, 1.0)
    white = (1.0, 1.0, 1.0)

    def pyramid_triangle(self):
        # We have 4 vertex: top, and the 3 for the triangle base
        top = (0.0, 1.0, 0.0)
        front_left = (-1.0, -1.0, 1.0)
        front_right = (1.0, -1.0, 1.0)
        right_left = (0.0, -1.0, -1.0)
        right_right = front_right
        back_left = front_left
        back_right = right_left

        # Front triangle
        glColor3f(*self.red)
        glVertex3f(*top)  # Top
        glColor3f(*self.green)
        glVertex3f(*front_left)  # Front Bottom Left
        glColor3f(*self.blue)
        glVertex3f(*front_right)  # Front Bottom Right

        # Right Triangle
        glColor3f(*self.red)
        glVertex3f(*top)  # Top
        glColor3f(*self.blue)
        glVertex3f(*right_right)  # Right Bottom Right
        glColor3f(*self.yellow)
        glVertex3f(*right_left)  # Right Bottom Left

        # Back Triangle
        glColor3f(*self.red)
        glVertex3f(*top)  # Top
        glColor3f(*self.yellow)
        glVertex3f(*back_right)  # Back Bottom Right
        glColor3f(*self.green)
        glVertex3f(*back_left)  # Back Bottom Left

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
        # Clear The Screen And The Depth Buffer
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()  # Reset The View to the center

        glTranslatef(0.0, 0.0, -5.0)

        # To show the pyramid and cube let's rotate it a bit based on y-axis
        glRotatef(self.rotation_triangle, 1.0, 1.0, 1.0)
        self.rotation_triangle += 1

        # Draw
        glBegin(GL_QUADS)  # Doing it as a triangle probably it is faster
        self.cube_square()
        glEnd()

        # glTranslatef(0.0, 0.0, -6.0)

        glBegin(GL_TRIANGLES)  # Doing it as a triangle probably it is faster
        self.pyramid_square()
        glEnd()

        glutSwapBuffers()


def main():
    Lesson5().main()


if __name__ == '__main__':
    main()
