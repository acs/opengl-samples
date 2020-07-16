#!/usr/bin/env python3

# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

# Based on: https://medium.com/@yvanscher/opengl-and-pyglet-basics-1bd9f1721cc6

import pyglet
from pyglet.gl import *

# create a pyglet window
win = pyglet.window.Window()

@win.event
def on_draw():
    glBegin(GL_LINES)
    # create a line, x,y,z
    glVertex3f(100.0,100.0,0.25)
    glVertex3f(200.0,300.0,-0.75)
    glEnd()

# run our pyglet app, and show the window
pyglet.app.run()