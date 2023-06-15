# -*- coding: utf-8 -*- 
import os
import sys 

## local UI import
#sys.path.remove('/home/cpi/launcher/Menu/GameShell/10_Settings')
#sys.path.append(os.path.dirname(__file__))
print(sys.path)
from Sound import pages
from Sound import myvars
#sys.path.remove(os.path.dirname(__file__))

def Init(main_screen):
    pages.InitSoundPage(main_screen)

def API(main_screen):
    
    if main_screen !=None:
        main_screen.PushCurPage()
        main_screen.SetCurPage(myvars.SoundPage)
        main_screen.Draw()
        main_screen.SwapAndShow()
        
