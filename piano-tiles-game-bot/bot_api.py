from pyautogui import *
import pyautogui
import os
import time
import keyboard
import random
import mouse

im1 = pyautogui.screenshot(region=(690,381,442,619)) #region=(331,166,242,319)
im1.save(r"./savedimage.png")
x = im1.getpixel((0,0))
print (x)

#Tile 1 position: (X,Y): (682,994)
#Tile 2 position: (X,Y): (793,998
#Tile 3 position: (X,Y): (959,988)
#Tile 4 position: (X,Y): (1098,988)

def pyautogui.click():  # так как как у меня проблемы с ОС я вынужден дописать в  названии фунции ее ссылку на откуда буду брать действие,  из какой документации (не Win Api *туть*)
    pyautogui.moveTo()
    pyautogui.(button='left', click=1, interval=0.01)

while keyboard.is_pressed('q') == False: #дописать РГБ не совпадает с винапишными(RGB = Nan)
    if pyautogui.pixel(682, 994):        # для x и y если что подкоректировать положение браузера
        pyautogui.click (682, 994)
    if pyautogui.pixel(793, 998):
        pyautogui.click (793, 998)
    if pyautogui.pixel(959, 988):
        pyautogui.click (959, 988)
    if pyautogui.pixel(682, 988):
        pyautogui.click (682, 988)
