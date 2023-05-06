"""
UI for the project
"""


# Is this working
import webbrowser
import pygame.camera
import pygame.image
import sys
import pygame

# initialization
pygame.camera.init()
pygame.font.init()


cameraList = pygame.camera.list_cameras()
webcam = pygame.camera.Camera(cameraList[1])
webcam.start()

# grab first frame
img = webcam.get_image()

WIDTH = 960
HEIGHT = 720


screen = pygame.display.set_mode( ( WIDTH, HEIGHT) )

mainMenu = pygame.Surface((WIDTH, HEIGHT))
mainMenu.fill((255, 255, 255))

# Font
sunnyFontS = pygame.font.Font("assets/SunnySunday.ttf", 12)
sunnyFontM = pygame.font.Font("assets/SunnySunday.ttf", 24)
sunnyFontL = pygame.font.Font("assets/SunnySunday.ttf", 36)


# Background

background = pygame.image.load("assets/background2.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
mainMenu.blit(background, (0,0))

# Camera Icon
# cameraRect = pygame.Rect(10, HEIGHT - 110, 100, 100)
# cameraIcon = pygame.image.load("assets/betterCamera.png")
# cameraIcon = pygame.transform.scale(cameraIcon, (100, 100))
# mainMenu.blit(cameraIcon, (cameraRect))


# Github Icon
# githubIcon = pygame.image.load("assets/github.png")
# githubIcon = pygame.transform.scale(githubIcon, (30, 30))
# githubRect = pygame.Rect(WIDTH - 40, HEIGHT - 40, 30, 30)
# mainMenu.blit(githubIcon, (githubRect))

# Button 1
button1Rect = pygame.Rect(0, 150, 450, 100)
button1Img = pygame.image.load("assets/button1b.png")
button1Img = pygame.transform.scale(button1Img, (450, 100))
mainMenu.blit(button1Img, (button1Rect))

# Button 2
button2Rect = pygame.Rect(510, 300, 450, 100)
button2Img = pygame.image.load("assets/button3.png")
button2Img = pygame.transform.scale(button2Img, (450, 100))
mainMenu.blit(button2Img, (button2Rect))

# Button 3
button3Rect = pygame.Rect(0, 450, 450, 100)
button3Img = pygame.image.load("assets/button2a.png")
button3Img = pygame.transform.scale(button3Img, (450, 100))
mainMenu.blit(button3Img, (button3Rect))





# Camera on/off flag
camOn = False
selected = "menu"



# Main loop
running = True
while running:
    for evt in pygame.event.get() :
        if evt.type == pygame.QUIT:
            sys.exit()
        if evt.type == pygame.MOUSEBUTTONDOWN:
            if button2Rect.collidepoint(evt.pos):
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







