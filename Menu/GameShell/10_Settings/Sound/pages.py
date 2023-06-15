# -*- coding: utf-8 -*- 

from Sound.sound_page import SoundPage

from Sound import myvars

def InitSoundPage(main_screen):

    myvars.SoundPage = SoundPage()
    
    myvars.SoundPage._Screen = main_screen
    myvars.SoundPage._Name = "Sound volume"
    myvars.SoundPage.Init()
