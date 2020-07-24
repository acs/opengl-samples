#!/usr/bin/env python3

from OpenGL.GL import *
from OpenGL.GLUT import *

from opengl_app import OpenGLApp


class Lesson7(OpenGLApp):

    red = (1.0, 0.0, 0.0)
    dark_green = (0.0, 0.4, 0.0)
    light_green = (0.0, 0.4, 0.0)
    green = dark_green
    blue = (0.0, 0.0, 1.0)
    yellow = (1.0, 1.0, 0.0)
    cyan = (0.0, 1.0, 1.0)
    white = (1.0, 1.0, 1.0)

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
        glNormal3f(0.0, 0.0, 1.0)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(*top_front_left)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(*top_front_right)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(*bottom_front_right)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(*bottom_front_left)

        # Right square
        glNormal3f(1.0, 0.0, 0.0)
        glVertex3f(*top_front_right)
        glVertex3f(*top_back_right)
        glVertex3f(*bottom_back_right)
        glVertex3f(*bottom_front_right)

        # Back square
        glNormal3f(0.0, 0.0, -1.0)
        glVertex3f(*top_back_right)
        glVertex3f(*top_back_left)
        glVertex3f(*bottom_back_left)
        glVertex3f(*bottom_back_right)

        # Left square
        glNormal3f(-1.0, 0.0, 0.0)
        glVertex3f(*top_back_left)
        glVertex3f(*top_front_left)
        glVertex3f(*bottom_front_left)
        glVertex3f(*bottom_back_left)

        # Up square
        glNormal3f(0.0, 1.0, 1.0)
        glVertex3f(*top_front_right)
        glVertex3f(*top_back_right)
        glVertex3f(*top_back_left)
        glVertex3f(*top_front_left)

        # Down square
        glNormal3f(0.0, -1.0, 0.0)
        glVertex3f(*bottom_front_right)
        glVertex3f(*bottom_back_right)
        glVertex3f(*bottom_back_left)
        glVertex3f(*bottom_front_left)

    # The main drawing function.
    def draw_gl_scene(self):
        # Clear The Screen And The Depth Buffer
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()  # Reset The View to the center

        glTranslatef(0.0, 0.0, self.z_deep)

        # To show the pyramid and cube let's rotate it a bit based on y-axis
        glRotatef(self.x_rot, 1.0, 0.0, 0.0)
        glRotatef(self.y_rot, 0.0, 1.0, 0.0)
        self.x_rot += self.x_rot_speed
        self.y_rot += self.y_rot_speed

        # Select texture to use
        glBindTexture(GL_TEXTURE_2D, self.texture_ids[self.texture_id])

        # Draw
        glBegin(GL_QUADS)  # Doing it as a triangle probably it is faster
        self.cube_square()
        glEnd()

        glutSwapBuffers()


def main():
    Lesson7().main()


if __name__ == '__main__':
    main()
