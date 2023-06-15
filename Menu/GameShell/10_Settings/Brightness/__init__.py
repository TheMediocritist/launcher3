# -*- coding: utf-8 -*- 

## local UI import
sys.path.append("../Menu/GameShell/10_Settings/Brightness")
import pages
import myvars
sys.path.remove("../Menu/GameShell/10_Settings/Brightness")

def Init(main_screen):
    pages.InitBrightnessPage(main_screen)

def API(main_screen):
    
    if main_screen !=None:
        main_screen.PushCurPage()
        main_screen.SetCurPage(myvars.BrightnessPage)
        main_screen.Draw()
        main_screen.SwapAndShow()
        
