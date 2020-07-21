#!/usr/bin/env python

# Base class App used for the OpenGL tutorials http://nehe.gamedev.net

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys


class OpenGLApp:
    
    ESCAPE_KEY = b'\x1b'
    CTRLC_KEY = b'\x03'
    FULL_SCREEN_KEY = b'f'
    
    # Number of the glut window.
    window = 0
    width = 640
    height = 480

    # Rotation
    rotation_triangle = 0
    rotation_square = 0
        
    # A general OpenGL initialization function.  Sets all of the initial parameters.
    def init_gl(self):  # We call this right after our OpenGL window is created.
        glClearColor(0.0, 0.0, 0.0, 0.0)  # This Will Clear The Background Color To Black
        glClearDepth(1.0)  # Enables Clearing Of The Depth Buffer
        glDepthFunc(GL_LESS)  # The Type Of Depth Test To Do
        glEnable(GL_DEPTH_TEST)  # Enables Depth Testing
        glShadeModel(GL_SMOOTH)  # Enables Smooth Color Shading
    
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()  # Reset The Projection Matrix
        # Calculate The Aspect Ratio Of The Window
        gluPerspective(45.0, float(self.width) / float(self.height), 0.1, 100.0)
    
        glMatrixMode(GL_MODELVIEW)
    
    # The function called when our window is resized (which shouldn't happen if you enable fullscreen, below)
    def resize_gl_scene(self, width, height):
        self.width = width
        self.height = height
        if height == 0:  # Prevent A Divide By Zero If The Window Is Too Small
            height = 1
    
        glViewport(0, 0, width, height)  # Reset The Current Viewport And Perspective Transformation
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, float(self.width) / float(self.height), 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)
      
    # The main drawing function.
    def draw_gl_scene(self):
        # Clear The Screen And The Depth Buffer
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()  # Reset The View to the center

        # since this is double buffered, swap the buffers to display what just got drawn.
        glutSwapBuffers()

    # The function called whenever a key is pressed. Note the use of Python tuples to pass in: (key, x, y)
    def key_pressed(self, *args):
        # If escape is pressed, kill everything.
        if args[0] in [self.ESCAPE_KEY, self.CTRLC_KEY]:
            glutDestroyWindow(self.window)
            sys.exit()
        if args[0] in [self.FULL_SCREEN_KEY]:
            glutFullScreen()

    def main(self):
        # For now we just pass glutInit one empty argument. I wasn't sure what should or could be passed in (tuple, list, ...)
        # Once I find out the right stuff based on reading the PyOpenGL source, I'll address this.
        glutInit(())
    
        # Select type of Display mode:
        #  Double buffer
        #  RGBA color
        # Alpha components supported
        # Depth buffer
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    
        # get a 640 x 480 window
        glutInitWindowSize(self.width, self.height)
    
        # the window starts at the upper left corner of the screen
        glutInitWindowPosition(0, 0)
    
        # Okay, like the C version we retain the window id to use when closing, but for those of you new
        # to Python (like myself), remember this assignment would make the variable local and not global
        # if it weren't for the global declaration at the start of main.
        window = glutCreateWindow("GL Code Tutorial based on NeHe '99")
    
        # Register the drawing function with glut, BUT in Python land, at least using PyOpenGL, we need to
        # set the function pointer and invoke a function to actually register the callback, otherwise it
        # would be very much like the C version of the code.
        glutDisplayFunc(self.draw_gl_scene)
    
        # Uncomment this line to get full screen.
        # glutFullScreen()
    
        # When we are doing nothing, redraw the scene.
        glutIdleFunc(self.draw_gl_scene)
    
        # Register the function called when our window is resized.
        glutReshapeFunc(self.resize_gl_scene)
    
        # Register the function called when the keyboard is pressed.
        glutKeyboardFunc(self.key_pressed)
    
        # Initialize our window.
        self.init_gl()
    
        # Start Event Processing Engine
        glutMainLoop()
