# -*- coding: utf-8 -*- 
import sys 

## local UI import
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
print(sys.path)
import pages
import myvars
sys.path.remove(os.path.join(os.path.dirname(__file__), '..'))

def Init(main_screen):
    pages.InitSoundPage(main_screen)

def API(main_screen):
    
    if main_screen !=None:
        main_screen.PushCurPage()
        main_screen.SetCurPage(myvars.SoundPage)
        main_screen.Draw()
        main_screen.SwapAndShow()
        
