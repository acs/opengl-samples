#!/usr/bin/env python3

# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo
import sys
from time import sleep

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Based on https://pythonprogramming.net/opengl-rotating-cube-example-pyopengl-tutorial/

# 4 vertex up, 4 down, the order is important because how edges are drawn

vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

# 2 edges per face, 12
edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
)


def cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def print_error(str):
    sys.stderr.write(str + "\n")


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    # 45 degrees, aspect ratio and z visible range (clipping)
    # argNames=('fovy', 'aspect', 'zNear', 'zFar'),
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    # Moving back 5 units
    glTranslatef(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # angle, rx, ry, rz
        glRotatef(1, 3, 1, 1)
        # clear the OpenGL canvas
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        cube()
        # update the display
        pygame.display.flip()
        # this wait is needed?
        pygame.time.wait(10)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        s = "\n\nReceived Ctrl-C or other break signal. Exiting.\n"
        print_error(s)
        sys.exit(0)
