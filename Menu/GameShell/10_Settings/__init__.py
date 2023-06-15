# -*- coding: utf-8 -*- 

print("now we're in 10_Settings __init__.py")


import pygame
from pygame.locals import *
from sys import exit
import os
import sys

from datetime import datetime

import base64
from beeprint import pp

## local UI import
print("importing pages.py with sys.path that looks like: " + sys.path)
import pages
import myvars

def Init(main_screen):
    pages.InitListPage(main_screen)

def API(main_screen):
    
    if main_screen !=None:
        main_screen.PushCurPage()
        main_screen.SetCurPage(myvars.ListPage)
        main_screen.Draw()
        main_screen.SwapAndShow()
        
