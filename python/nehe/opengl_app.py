#!/usr/bin/env python

# Base class App used for the OpenGL tutorials http://nehe.gamedev.net
import numpy
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from PIL import Image

import sys


class OpenGLApp:

    # Keyboard
    ESCAPE_KEY = b'\x1b'
    CTRLC_KEY = b'\x03'

    # GL Window
    window = 0
    width = 640
    height = 480
    window_active = True
    full_screen = False
    z_deep = -5.0

    # Rotation
    rotation_triangle = 0
    rotation_square = 0
    x_rot = y_rot = 0
    x_rot_speed = y_rot_speed = 1

    # Blending
    blend = False

    # Lighting
    lights = False  # lights on/off
    # Ambient light is light that doesn't come from any particular direction.
    # All the objects in your scene will be lit up by the ambient light
    light_ambient = (0.5, 0.5, 0.5, 1.0)
    # Diffuse light is created by your light source and is reflected off the surface of an object in your scene.
    # Any surface of an object that the light hits directly will be very bright,
    # and areas the light barely gets to will be darker. This creates a nice shading effect on the sides
    light_diffuse = (1.0, 1.0, 1.0, 1.0)
    # Light in front of the screen because of 2.0 z
    light_position = (0.0, 0.0, 2.0, 1.0)

    # Textures
    texture_id = 0
    texture_ids = []
    # Nice place to get textures: https://www.texturex.com/
    textures = [("data/voxelers.bmp", GL_NEAREST),
                ("data/NeHe.bmp", GL_LINEAR_MIPMAP_NEAREST),
                ("data/glass.bmp", GL_LINEAR)]

    def load_gl_texture(self, image_path, filtering=GL_NEAREST):
        """
        Load a texture

        :param image_path: path with the image path
        :param filtering: GL_NEAREST (no filtering), GL_LINEAR (texture look smooth CPU/GPU intensive),
        GL_LINEAR_MIPMAP_NEAREST (tries different texture resolutions)
        :return:
        """

        image = Image.open(image_path)
        image_data = numpy.array(list(image.getdata()), numpy.uint8)

        # Create three Textures
        texture_id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, texture_id)

        glPixelStorei(GL_UNPACK_ALIGNMENT, 4)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_BASE_LEVEL, 0)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAX_LEVEL, 0)
        # filtering to use when the image is larger (GL_TEXTURE_MAG_FILTER)
        # or stretched on the screen than the original texture,
        # or when it's smaller (GL_TEXTURE_MIN_FILTER) on the screen than the actual texture
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        # Generate the texture
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, image.size[0], image.size[1],
                     0, GL_RGB, GL_UNSIGNED_BYTE, image_data)

        image.close()
        return texture_id

    def load_textures(self, textures):
        for texture in textures:
            self.texture_ids.append(self.load_gl_texture(texture[0], texture[1]))

    # A general OpenGL initialization function.  Sets all of the initial parameters.
    # We call this right after our OpenGL window is created.
    def init_gl(self):

        self.load_textures(self.textures)

        glEnable(GL_TEXTURE_2D)

        glClearColor(0.0, 0.0, 0.0, 0.0)  # This Will Clear The Background Color To Black
        glClearDepth(1.0)  # Enables Clearing Of The Depth Buffer
        glDepthFunc(GL_LEQUAL)  # The Type Of Depth Test To Do
        glEnable(GL_DEPTH_TEST)  # Enables Depth Testing
        glShadeModel(GL_SMOOTH)  # Enables Smooth Color Shading
        glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)  # Really Nice Perspective

        # Setup lighting
        glLightfv(GL_LIGHT1, GL_AMBIENT, self.light_ambient)
        glLightfv(GL_LIGHT1, GL_DIFFUSE, self.light_diffuse)
        glLightfv(GL_LIGHT1, GL_POSITION, self.light_position)
        glEnable(GL_LIGHT1)  # Lights won't show until GL_LIGHTING is enabled

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()  # Reset The Projection Matrix
        # Calculate The Aspect Ratio Of The Window
        gluPerspective(45.0, float(self.width) / float(self.height), 0.1, 100.0)

        glMatrixMode(GL_MODELVIEW)

        # Blending
        glColor4f(1.0,1.0,1.0,0.5)
        glBlendFunc(GL_SRC_ALPHA,GL_ONE)
    
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

    # The function called whenever a key is pressed
    def key_pressed(self, *args):
        # If escape is pressed, kill everything.
        if args[0] in [self.ESCAPE_KEY, self.CTRLC_KEY]:
            glutDestroyWindow(self.window)
            sys.exit()

        if args[0] == b'f':
            glutFullScreenToggle()
        if args[0] == b'l':
            self.lights = not self.lights
            if self.lights:
                glEnable(GL_LIGHTING)
            else:
                glDisable(GL_LIGHTING)
        if args[0] == b'w':
            self.z_deep += 0.1
        if args[0] == b's':
            self.z_deep -= 0.1
        if args[0] == b't':
            self.texture_id +=1
            self.texture_id = self.texture_id % len(self.texture_ids)
        if args[0] == b'b':
            self.blend = not self.blend
            if self.blend:
                glEnable(GL_BLEND)
                glDisable(GL_DEPTH_TEST)
            else:
                glDisable(GL_BLEND)
                glEnable(GL_DEPTH_TEST)




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
