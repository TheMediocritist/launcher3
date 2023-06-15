# -*- coding: utf-8 -*- 
import sys

## local UI import
sys.path.append("../Menu/GameShell/10_Settings/Wifi")
import pages
import myvars

"""
try:
    from icons import preload
except:
    print("No icons package")
"""

def Init(main_screen):
    #pages.InitPasswordPage(main_screen)
    #pages.InitScanPage(main_screen)
    print("issues here!")

def API(main_screen):
    
    if main_screen != None:
        main_screen.PushCurPage()
        main_screen.SetCurPage(myvars.ScanPage)
        main_screen.Draw()
        main_screen.SwapAndShow()
sys.path.remove("../Menu/GameShell/10_Settings/Wifi")

