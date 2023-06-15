# -*- coding: utf-8 -*- 

## local UI import
sys.path.append("../Menu/GameShell/10_Settings/Sound")
import pages
import myvars
sys.path.remove("../Menu/GameShell/10_Settings/Sound")

def Init(main_screen):
    pages.InitSoundPage(main_screen)

def API(main_screen):
    
    if main_screen !=None:
        main_screen.PushCurPage()
        main_screen.SetCurPage(myvars.SoundPage)
        main_screen.Draw()
        main_screen.SwapAndShow()
        
