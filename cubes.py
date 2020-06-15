import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, 1, 1),
    (-1, -1, 1)
)

edges = (
    (0, 1),
    (0, 4),
    (0, 3),
    (2, 1),
    (2, 3),
    (2, 6),
    (5, 4),
    (5, 6),
    (5, 1),
    (7, 4),
    (7, 6),
    (7, 3)
)

surfaces = (
    (0,1,2,3),
    (0,4,5,1),
    (0,4,7,3),
    (6,7,4,5),
    (6,7,3,2),
    (6,5,1,2)
)

colors = (
    (0,255,0),
    (50,205,50),
    (0,0,255),
    (255,0,0),
    (30,144,255),
    (255,69,0),
    (255,215,0),
    (255,255,0),
    (173,255,47),
    (154,205,50),
    (0,128,0),
    (32,178,170),
    (0,206,209)
)

def cube():
    glBegin(GL_QUADS)
    
    for surface in surfaces:
        x = 0
        for vertex in surface:
            glColor3fv(colors[x])
            glVertex3fv(vertices[vertex])
            x+=1
    glEnd()
    glBegin(GL_LINES)
    for edge in edges:
        x = 0
        for vertex in edge:
            glColor3fv(colors[x])
            glVertex3fv(vertices[vertex])
            x+=1
    glEnd()

def cross(a,b):
    return (a[1]*b[2] - a[2]*b[1], a[2]*b[0]-b[2]*a[0], a[0]*b[1]-a[1]*b[0])


def draw():
    pygame.init()
    display = (800, 600)
    screen = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("CUBE") 
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)
    glRotatef(0, 0, 0, 0)
    mx = my = mz = 0
    rotate = False
    a = (1,1,0)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    glTranslate(0.1,0,0)
                if event.key == pygame.K_LEFT:
                    glTranslate(-0.1,0,0)
                if event.key == pygame.K_UP:
                    glTranslate(0,0.1,0)
                if event.key == pygame.K_DOWN:
                    glTranslate(0,-0.1,0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    rotate = True
                if event.button == 4:
                    glTranslate(0,0,0.1)
                if event.button == 5:
                    glTranslate(0,0,-0.1)
            if event.type == pygame.MOUSEMOTION and rotate:
                mx, my = pygame.mouse.get_pos()
                mx -= 400
                my -= 300
                mx, my, mz = cross(a,(mx, my, mz))
                glRotatef(1, mx, my, mz)
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    rotate = False
        # glRotatef(1, mx, my, 0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        cube()
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    draw()
