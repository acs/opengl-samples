#!/usr/bin/env python3

# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

# Based on: https://medium.com/@yvanscher/opengl-and-pyglet-basics-1bd9f1721cc6

import pyglet
from pyglet.gl import *

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


# Just rotate the current scene
def update_frame(x, y):
    # angle, x, y, z
    glRotatef(1, 3*100, 1*100, 0)


def cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3f(vertices[vertex][0], vertices[vertex][1], vertices[vertex][2])
    glEnd()


def line():
    glBegin(GL_LINES)
    # create a line, x,y,z
    glVertex3f(100.0,100.0,0.25)
    glVertex3f(200.0,300.0,-0.75)
    # glVertex3f(1,1,0.25)
    # glVertex3f(2,3,-0.75)

    glEnd()


# create a pyglet window
win = pyglet.window.Window()


@win.event
def on_draw():
    # glClear(GL_COLOR_BUFFER_BIT)
    line()


if __name__ == '__main__':
    # display = (800, 600)
    # 45 degrees, aspect ratio and z visible range (clipping)
    # gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    # Moving back 5 units
    # glTranslatef(0.0, 0.0, -2)

    # every 1/10 th get the next frame
    # pyglet.clock.schedule(update_frame, 1/10.0)
    # run our pyglet app, and show the window
    pyglet.app.run()