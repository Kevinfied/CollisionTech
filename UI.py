"""
UI for the project
"""

import webbrowser
import pygame.camera
import pygame.image
import sys
import pygame

# Camera initialization
pygame.camera.init()

cameraList = pygame.camera.list_cameras()
webcam = pygame.camera.Camera(cameraList[1])

webcam.start()

# grab first frame
img = webcam.get_image()

WIDTH = (img.get_width())*2
HEIGHT = (img.get_height())*2


screen = pygame.display.set_mode( ( WIDTH, HEIGHT) )

mainMenu = pygame.Surface((WIDTH, HEIGHT))
mainMenu.fill((255, 255, 255))
# Camera Icon
cameraRect = pygame.Rect(10, HEIGHT - 110, 100, 100)
cameraIcon = pygame.image.load("assets/cameraIcon.png")
cameraIcon = pygame.transform.scale(cameraIcon, (100, 100))
mainMenu.blit(cameraIcon, (cameraRect))

# Github Icon
githubIcon = pygame.image.load("assets/github.png")
githubIcon = pygame.transform.scale(githubIcon, (30, 30))
githubRect = pygame.Rect(WIDTH - 40, HEIGHT - 40, 30, 30)
mainMenu.blit(githubIcon, (githubRect))


# Camera on/off flag
camOn = False


# Main loop
running = True
while running:
    for evt in pygame.event.get() :
        if evt.type == pygame.QUIT:
            sys.exit()
        if evt.type == pygame.MOUSEBUTTONDOWN:
            if cameraRect.collidepoint(evt.pos):
                camOn = True
            if githubRect.collidepoint(evt.pos):
                if camOn == False:
                    webbrowser.open('https://github.com/Kevinfied/EpicMHProject/tree/main')

        if evt.type == pygame.KEYDOWN:
            if evt.key == pygame.K_ESCAPE:
                camOn = False
            if evt.key == pygame.K_g:
                webbrowser.open('https://github.com/Kevinfied/EpicMHProject/tree/main')
            if evt.key == pygame.K_c:
                camOn = not camOn
    
    screen.blit(mainMenu, (0,0))


    if camOn:
        screen.blit(img, (0,0))
        img = webcam.get_image()
        img = pygame.transform.flip(img, True, False)
        img = pygame.transform.scale(img, (WIDTH, HEIGHT))

    pygame.display.flip()  
