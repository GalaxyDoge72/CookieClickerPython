import pygame
import os
import sys
import random
import time
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()
true = True
false = False
pygame.init()
CookiesTotal = 0
CursorBaseCost = 10
BaseCursorAmount = 0
last_time = time.time()
cookies_per_second = 0
rectanglecolour = (0,0,0)
CursorButtonColour = (153,153,153)
## Set up the window ##

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("PyCookie")

## Set up the font ##

font = pygame.font.SysFont("Arial", 48)
CursorFont = pygame.font.SysFont("Arial", 18)

## Render Cookie Image ##
currentDir = filedialog.askdirectory()
CookieImage = pygame.image.load(currentDir + "\cookie.png")
original_width, original_height = CookieImage.get_rect().size
scaled_image = pygame.transform.scale(CookieImage, (original_width // 2, original_height // 2))
scaled_width, scaled_height = scaled_image.get_rect().size
x = (screen_width - scaled_width) // 2
y = (screen_height - scaled_height) // 2
screen.blit(scaled_image, (x, y))
pygame.display.update()

CursorButtonImage = pygame.image.load(currentDir + "\CursorButton.png")
originalcursorbuttonwidth, originalcursorbuttonheight = CursorButtonImage.get_rect().size
scaledcursorimage = pygame.transform.scale(CursorButtonImage, (originalcursorbuttonwidth // 8, originalcursorbuttonheight // 8))
scaledcursorwidth, scaledcursorheight = scaledcursorimage.get_rect().size
CursorButtonX = (screen_width - scaledcursorwidth) / 2 - 450
CursorButtonY = (screen_height - scaledcursorheight) / 2 - 250
screen.blit(scaledcursorimage, (CursorButtonX, CursorButtonY))
pygame.display.update()

GrandmaButtonImage = pygame.image.load(currentDir + "\GrandmaButton.png")
originalgrandmawidth, originalgrandmaheight = GrandmaButtonImage.get_rect().size
scaledgrandmaimage = pygame.transform.scale(GrandmaButtonImage, (originalgrandmawidth // 6 , originalgrandmaheight // 6))
scaledgrandmawidth, scaledgrandmaheight = scaledgrandmaimage.get_rect().size
GrandmaButtonX = (screen_width - scaledgrandmawidth) / 2 - 450
GrandmaButtonY = (screen_height - scaledgrandmaheight) / 2
screen.blit(scaledgrandmaimage, (GrandmaButtonX, GrandmaButtonY))
pygame.display.update()

CursorCost = CursorFont.render(str(CursorBaseCost) + " Cookies", True, (255, 255, 255))
Cursortext_rect = CursorCost.get_rect()
CursorTextX = CursorButtonX * 2 + 70
CursorTextY = CursorButtonY * 2
screen.blit(CursorCost, (CursorTextX, CursorTextY))
pygame.display.update()

CookiesText = font.render(str(CookiesTotal) + " Cookies", True, (255,255,255))
text_rect = CookiesText.get_rect()
TextX = (screen_width - text_rect.width) / 2
TextY = (screen_height - text_rect.height) / 8
screen.blit(CookiesText, (TextX, TextY))
pygame.display.update()

## Render Assets ##
def ClearText():
    rect_surface = pygame.Surface((text_rect.width, text_rect.height))
    rect_surface.fill(rectanglecolour)
    CookiesText.blit(rect_surface, (0, 0), special_flags=pygame.BLEND_RGB_MULT)
    pygame.display.update()
def ClearCursorText():
    Cursorrect_surface = pygame.Surface((Cursortext_rect.width, Cursortext_rect.height), pygame.SRCALPHA)
    Cursorrect_surface.fill((0, 0, 0, 0))  # fill with transparent color
    CursorCost.blit(Cursorrect_surface, (0, 0))
    pygame.display.update()
def RenderText():
    x = int(CookiesTotal)
    CookiesText = font.render(str(x) + " Cookies", True, (255,255,255))
    CookiesTextAlt = font.render(str(x) + " Cookies", True, True, (0,0,0))
    text_rect = CookiesText.get_rect()
    TextX = (screen_width - text_rect.width) / 2
    TextY = (screen_height - text_rect.height) / 8
    screen.blit(CookiesText, (TextX, TextY))
    pygame.display.update()
    screen.blit(CookiesTextAlt, (TextX, TextY))
def RenderCookieButtonText():
    y = int(CursorBaseCost)
    CursorCost = CursorFont.render(str(y) + " Cookies", True, (255, 255, 255))
    cursorrect = CursorCost.get_rect()
    CursorTextX = CursorButtonX * 2 + 75
    CursorTextY = CursorButtonY * 2
    screen.blit(CursorCost, (CursorTextX, CursorTextY))
    pygame.display.update()

def RenderCursor():
    CursorButtonImage = pygame.image.load(currentDir + "\CursorButton.png")
    originalcursorbuttonwidth, originalcursorbuttonheight = CursorButtonImage.get_rect().size
    scaledcursorimage = pygame.transform.scale(CursorButtonImage, (originalcursorbuttonwidth // 8, originalcursorbuttonheight // 8))
    scaledcursorwidth, scaledcursorheight = scaledcursorimage.get_rect().size
    CursorButtonX = (screen_width - scaledcursorwidth) / 2 - 450
    CursorButtonY = (screen_height - scaledcursorheight) / 2 - 250
    screen.blit(scaledcursorimage, (CursorButtonX, CursorButtonY))
    pygame.display.update()

def RenderGrandma():
    GrandmaButtonImage = pygame.image.load(currentDir + "\GrandmaButton.png")
    originalgrandmawidth, originalgrandmaheight = GrandmaButtonImage.get_rect().size
    scaledgrandmaimage = pygame.transform.scale(GrandmaButtonImage, (originalgrandmawidth // 6, originalgrandmaheight // 6))
    scaledgrandmawidth, scaledgrandmaheight = scaledgrandmaimage.get_rect().size
    GrandmaButtonX = (screen_width - scaledgrandmawidth) / 2 - 450
    GrandmaButtonY = (screen_height - scaledgrandmaheight) / 2
    screen.blit(scaledgrandmaimage, (GrandmaButtonX, GrandmaButtonY))
    pygame.display.update()

## Run Game ##
RenderText()
RenderCursor()
RenderGrandma()
## Run Game ##
while True:
    prev_cookies_total = CookiesTotal
    CookiesTotal = CookiesTotal + cookies_per_second
    RenderText()
    if CookiesTotal < 0:
        CookiesTotal = 0
    for event in pygame.event.get():
        RenderGrandma()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            image_rect = CookieImage.get_rect(topleft=(x, y))
            CursorRect = scaledcursorimage.get_rect(topleft=(CursorButtonX, CursorButtonY))
            if image_rect.collidepoint(mouse_pos):
                screen.fill((0, 0, 0))
                screen.blit(scaled_image, (x, y))
                screen.blit(scaledcursorimage, (CursorButtonX, CursorButtonY))
                screen.blit(CursorCost, (CursorTextX, CursorTextY))
                pygame.display.update()
                CookiesTotal = CookiesTotal + 1
                RenderCursor()
                RenderCookieButtonText()
                RenderGrandma()
                pygame.display.update()
            elif CursorRect.collidepoint(mouse_pos):
                if CookiesTotal >= CursorBaseCost:
                    screen.fill((0, 0, 0))
                    screen.blit(scaled_image, (x, y))
                    screen.blit(scaledcursorimage, (CursorButtonX, CursorButtonY))
                    screen.blit(CursorCost, (CursorTextX, CursorTextY))
                    if cookies_per_second < 1 / 1000:
                        cookies_per_second = (cookies_per_second + 1) / 1000
                    else:
                        cookies_per_second = cookies_per_second + 1 / 1000
                    CursorBaseCost += CursorBaseCost * (random.random())
                    CookiesTotal = CookiesTotal - CursorBaseCost
                    RenderCursor()
                    RenderCookieButtonText()
                    RenderGrandma()
                    pygame.display.update()
                    print("Cookies per second is now: " + str(cookies_per_second * 1000))
                else:
                    print("You don't have enough cookies!")
                    break
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
