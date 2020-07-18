#!/usr/bin/env python3

# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

# https://pyglet.readthedocs.io/en/latest/programming_guide/gl.html

from pyglet.gl import *

# Direct OpenGL commands to this window.
window = pyglet.window.Window()


@window.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glBegin(GL_TRIANGLES)
    glVertex2f(0, 0)
    glVertex2f(window.width, 0)
    glVertex2f(window.width, window.height)
    glEnd()


@window.event
def on_draw_new():
    glBegin(GL_TRIANGLES)
    glVertex2f(0, 0)
    glVertex2f(1, 0)
    glVertex2f(1, 1)
    glEnd()


if __name__ == '__main__':
    gluPerspective(45, (window.width / window.height), 0.1, 50.0)
    pyglet.app.run()