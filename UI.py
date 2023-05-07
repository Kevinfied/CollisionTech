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
webcam = pygame.camera.Camera(cameraList[0])
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
sunnyFontL = pygame.font.Font("assets/SunnySunday.ttf", 56)
sunnyFontXL = pygame.font.Font("assets/SunnySunday.ttf", 72)

# Background
# global background
background = pygame.image.load("assets/background2.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))




# def setup():
    # Background
button1Area = mainMenu.subsurface((0, 195, 960, 100))
button2Area = mainMenu.subsurface((0, 385, 960, 100))
button3Area = mainMenu.subsurface((0, 575, 960, 100))
# global background
mainMenu.blit(background, (0,0))

titleText = sunnyFontXL.render("Testing Technologies", True, (77, 84, 114))
titleTextRect = titleText.get_rect()
titleTextRect.center = (WIDTH/2, 100)
mainMenu.blit(titleText, titleTextRect)


button1Cap = button1Area.copy()
button2Cap = button2Area.copy()
button3Cap = button3Area.copy()

# global button2X, button2Y, button2W, button2H, button2Rect, button1X, button1Y, button1W, button1H, button1Rect, button3Rect, button3X, button3Y, button3W, button3H
# Button 1
button1X, button1Y = 0, 195
button1W, button1H = 550, 100
# global button1Rect
button1Rect = pygame.Rect(button1X, button1Y, button1W, button1H)
# button1Img = pygame.image.load("assets/button1b.png")
# button1Img = pygame.transform.scale(button1Img, (button1W, button1H))
# mainMenu.blit(button1Img, (button1Rect))
pygame.draw.rect(mainMenu, (238, 225, 255), button1Rect, 50, 20)
instructionsX = 325
instructionsText = sunnyFontL.render("INTRODUCTION", True, (77, 84, 114))
instructionsTextRect = instructionsText.get_rect()
instructionsTextRect.center = (instructionsX, 245)
mainMenu.blit(instructionsText, instructionsTextRect)



# Button 2
button2X, button2Y = 410, 385
button2W, button2H = 550, 100
global button2Rect
button2Rect = pygame.Rect(button2X, button2Y, button2W, button2H)
# button2Img = pygame.image.load("assets/button3.png")
# button2Img = pygame.transform.scale(button2Img, (button2W, button2H))
# mainMenu.blit(button2Img, (button2Rect))
pygame.draw.rect(mainMenu, (216, 246, 255), button2Rect, 50, 20)

global cameraText, cameraTextRect, cameraTextX, cameraTextY
cameraTextX, cameraTextY = 550, 435
cameraText = sunnyFontL.render("START", True, (77, 84, 114))
cameraTextRect = cameraText.get_rect()
cameraTextRect.center = (cameraTextX, cameraTextY)
mainMenu.blit(cameraText, cameraTextRect)

# Button 3


button3X, button3Y = 0, 575
button3W, button3H = 550, 100

button3Rect = pygame.Rect(button3X, button3Y, button3W, button3H)
# button3Img = pygame.image.load("assets/button2a.png")
# button3Img = pygame.transform.scale(button3Img, (button3W, button3H))
# mainMenu.blit(button3Img, (button3Rect))
pygame.draw.rect(mainMenu, (227, 255, 230), button3Rect, 50, 20)

aboutX = 325
aboutText = sunnyFontL.render("ABOUT US", True, (77, 84, 114))
aboutTextRect = aboutText.get_rect()
aboutTextRect.center = (aboutX, 625)
mainMenu.blit(aboutText, aboutTextRect)




screen.blit(mainMenu, (0,0))

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


# Button area captures


# Instructions Page
instructionsPage = pygame.Surface((WIDTH, HEIGHT))
instructionsPage.blit(background, (0,0))








# FLAGS
selected = "menu"
button1Hover = False
button2Hover = False
button3Hover = False


# Crosshair for the camera mode
def cursor(x, y):
    pygame.draw.line(screen, (255, 0, 0), (x-5, y), (x+5, y), 1)
    pygame.draw.line(screen, (255, 0, 0), (x, y - 5), (x, y + 5), 1)

# Project Info Page
infoPage = pygame.Surface((WIDTH, HEIGHT))
infoPage.blit(background, (0,0))
line1 = sunnyFontM.render("The point of this project is to demonstrate the advantages and disadvantages of", True, (77, 84, 114))
line2 = sunnyFontM.render("2D recognition and how it can be used to warn drivers about obstacles or other", True, (77, 84, 114))
line3 = sunnyFontM.render("dangers. We created a prototype model to test this idea in the real world and", True, (77, 84, 114))
line4 = sunnyFontM.render("identify areas for improvement. Since this is simply a proof of concept, we", True, (77, 84, 114))
line5 = sunnyFontM.render("manually adjust the OpenCV thresholds to account for specific lighting", True, (77, 84, 114))
line6 = sunnyFontM.render("conditions. We hope that this project will serve as a stepping stone to help", True, (77, 84, 114))
line7 = sunnyFontM.render("us improve when testing other ideas. Projects like these also help educate", True, (77, 84, 114))
line8 = sunnyFontM.render("the public about new safety concepts and encourage them to think about ", True, (77, 84, 114))
line9 = sunnyFontM.render("their thoughts about these concepts", True, (77, 84, 114))
infoPage.blit(line1, (50, 100))
infoPage.blit(line2, (50, 150))
infoPage.blit(line3, (50, 200))
infoPage.blit(line4, (50, 250))
infoPage.blit(line5, (50, 300))
infoPage.blit(line6, (50, 350))
infoPage.blit(line7, (50, 400))
infoPage.blit(line8, (50, 450))
infoPage.blit(line9, (50, 500))





# Main loop
running = True
while running:
    for evt in pygame.event.get() :
        if evt.type == pygame.QUIT:
            sys.exit()
        if evt.type == pygame.MOUSEBUTTONDOWN:

            if selected == "menu":
                if button2Rect.collidepoint(evt.pos):
                    selected = "camera"
                # if githubRect.collidepoint(evt.pos):
                #     if camOn == False:
                #         webbrowser.open('https://github.com/Kevinfied/EpicMHProject/tree/main')
                # if button3Rect.collidepoint(evt.pos):
                #     sys.exit()
            
                if button1Rect.collidepoint(evt.pos):
                    selected = "info"

                if button3Rect.collidepoint(evt.pos):
                    webbrowser.open('https://github.com/Kevinfied/EpicMHProject/blob/main/README.md')
            elif selected == "camera":
                print(mx, my)
                sys.exit()
            #               


            if selected == "camera":
                print(mx, my)

        if evt.type == pygame.KEYDOWN:
            if evt.key == pygame.K_ESCAPE:
                selected = "menu"
            if evt.key == pygame.K_g:
                webbrowser.open('https://github.com/Kevinfied/EpicMHProject/tree/main')
            if evt.key == pygame.K_c:
                if selected != "camera":
                    selected = "camera"
                else:
                    selected = "menu"

    mx, my = pygame.mouse.get_pos()
    mb = pygame.mouse.get_pressed()
    # Button 2






### MENU ###
    if selected == "menu":
        pygame.mouse.set_visible(True)
        # Background

        


        button1Hover = False
        button2Hover = False
        button3Hover = False

        if button2Rect.collidepoint(mx, my):
            if mb[0] == 0:
                button2Hover = True
                while button2W < 600:
                    button2X -= 1
                    button2W += 1
                    cameraTextX -= 1
                    cameraTextRect.center = (cameraTextX, cameraTextY)
                    # button2Img = pygame.transform.scale(button2Img, (button2W, button2H))
                    # mainMenu.blit(button2Img, (button2X, button2Y))
                    pygame.draw.rect(mainMenu, (216, 246, 255), (button2X, button2Y, button2W, button2H), 50, 20)
                    mainMenu.blit(cameraText, cameraTextRect)
                    screen.blit(mainMenu, (0,0))
                    pygame.display.flip()
                    pygame.time.wait(2)


        if button1Rect.collidepoint(mx, my):
            if mb[0] == 0:
                button1Hover = True
                while button1W < 600:
                    button1W += 1
                    instructionsX += 1
                    # button1Img = pygame.transform.scale(button1Img, (button1W, button1H))
                    # mainMenu.blit(button1Img, (button1X, button1Y))
                    pygame.draw.rect(mainMenu, (238, 225, 255), (button1X, button1Y, button1W, button1H), 50, 20)
                    screen.blit(mainMenu, (0,0))
                    
                    instructionsTextRect.center = (instructionsX, 245)
                    mainMenu.blit(instructionsText, instructionsTextRect)

                    screen.blit(mainMenu, (0,0))
                    pygame.display.flip()
                    pygame.time.wait(2)
        
        if button3Rect.collidepoint(mx, my):
            if mb[0] == 0:
                button3Hover = True
                while button3W < 600:
                    button3W += 1
                    aboutX += 1
                    # button3Img = pygame.transform.scale(button3Img, (button3W, button3H))
                    # mainMenu.blit(button3Img, (button3X, button3Y))
                    pygame.draw.rect(mainMenu, (227, 255, 230), (button3X, button3Y, button3W, button3H), 50, 20)
                    screen.blit(mainMenu, (0,0))

                    aboutTextRect.center = (aboutX, 625)
                    mainMenu.blit(aboutText, aboutTextRect)
                    screen.blit(mainMenu, (0,0))

                    pygame.display.flip()
                    pygame.time.wait(2)

        
        if button1Hover == False:
            button1W = 550
            mainMenu.blit(button1Cap, (0,195))
            pygame.draw.rect(mainMenu, (238, 225, 255), (0, 195, 550, 100), 50, 20)
            instructionsX = 325
            instructionsTextRect.center = (instructionsX, 245)
            mainMenu.blit(instructionsText, instructionsTextRect)

        if button2Hover == False:
            button2W = 550
            button2X = 410
            mainMenu.blit(button2Cap, (0, 385))
            pygame.draw.rect(mainMenu, (216, 246, 255), (410, 385, 550, 100), 50, 20)
            cameraTextX = 550
            cameraTextRect.center = (cameraTextX, cameraTextY)
            mainMenu.blit(cameraText, cameraTextRect)


        
        if button3Hover == False:
            button3W = 550
            aboutX = 325
            aboutTextRect.center = (aboutX, 625)
            mainMenu.blit(button3Cap, (0, 575))
            pygame.draw.rect(mainMenu, (227, 255, 230), (0, 575, 550, 100), 50, 20)
            mainMenu.blit(aboutText, aboutTextRect)

        screen.blit(mainMenu, (0,0))


        # Reset button sizes
        button1Hover = False
        button2Hover = False
        button3Hover = False


            


      

    # if selected == "info":



    if selected == "camera":
        # screen.blit(img, (0,0))
        # img = webcam.get_image()
        # img = pygame.transform.flip(img, True, False)
        # img = pygame.transform.scale(img, (WIDTH, HEIGHT))
        # pygame.mouse.set_visible(False)
        # cursor(mx, my)
        sys.exit()
    
    if selected == "info":
        screen.blit(infoPage, (0,0))


    pygame.display.flip()