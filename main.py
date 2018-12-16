import arcade
import os
import time
import pyglet
import vlc
import random

#constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
volume_on = True
menusound_running = False
bongocat1_load = True
bongocat2_load = False

class main_menu:
    def draw_background():
        background = arcade.load_texture("Assets/background0.png")
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, background)

    def draw_playbutton():
        global playbtncenter_x
        global playbtncenter_y
        global playbtnscale
        global playbtnwidth
        global playbtnheight
        scale = 0.7
        width = 397
        height = 87
        playbtncenter_x = SCREEN_WIDTH / 2
        playbtncenter_y = SCREEN_HEIGHT / 2
        playbtnwidth = width * scale
        playbtnheight = height * scale            
        play = arcade.load_texture("Assets/Main-Menu/Buttons/PLAYbtn.png")
        arcade.draw_texture_rectangle(playbtncenter_x, playbtncenter_y, playbtnwidth, playbtnheight, play)

    def draw_settingsbutton():
        global settingsbtnscale
        global settingsbtnwidth
        global settingsbtnheight
        global settingsbtncenter_x
        global settingsbtncenter_y
        settingsbtnscale = 0.7
        settingsbtnwidth = 87
        settingsbtnheight = 87
        settingsbtncenter_x = 1150.5
        settingsbtncenter_y = 675
        settingsbutton = arcade.load_texture("Assets/Main-Menu/Buttons/SETTINGSbtn.png")
        arcade.draw_texture_rectangle(settingsbtncenter_x, settingsbtncenter_y, settingsbtnwidth*settingsbtnscale, settingsbtnheight*settingsbtnscale, settingsbutton)                        

    def draw_volumebutton():
        global volumebtnwidth
        global volumebtnheight
        global volumebtncenter_x
        global volumebtncenter_y
        scale = 0.7
        volumebtnwidth = 87
        volumebtnheight = 87
        volumebtncenter_x = 1232.5
        volumebtncenter_y = 675
        
        if volume_on == True:
            volumeon = arcade.load_texture("Assets/Main-Menu/Buttons/VOLUME-ONbtn.png")
            arcade.draw_texture_rectangle(volumebtncenter_x, volumebtncenter_y, volumebtnwidth*scale, volumebtnheight*scale, volumeon)                                                         
        elif volume_on == False:
            volumeoff = arcade.load_texture("Assets/Main-Menu/Buttons/VOLUME-OFFbtn.png")
            arcade.draw_texture_rectangle(volumebtncenter_x, volumebtncenter_y, volumebtnwidth*scale, volumebtnheight*scale, volumeoff)
        else:
            pass

    def draw_selectcat():
        global selectcatbtnscale
        global selectcatbtnwidth
        global selectcatbtnheight
        global selectcatbtncenter_x
        global selectcatbtncenter_y
        selectcatbtnscale = 0.45
        selectcatbtnwidth = 397
        selectcatbtnheight = 87
        selectcatbtncenter_x = SCREEN_WIDTH / 2 - 94.325
        selectcatbtncenter_y = SCREEN_HEIGHT / 2 - 60.025
        selectcat = arcade.load_texture("Assets/Main-Menu/Buttons/SELECTCATbtn.png")
        arcade.draw_texture_rectangle(selectcatbtncenter_x, selectcatbtncenter_y, selectcatbtnwidth*selectcatbtnscale, selectcatbtnheight*selectcatbtnscale, selectcat)

    def draw_selectlevel():
        scale = 0.45
        width = 397
        height = 87
        selectlevel = arcade.load_texture("Assets/Main-Menu/Buttons/LEVELSELECTbtn.png")
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2 + 94.325, SCREEN_HEIGHT / 2 - 60.025, width*scale, height*scale, selectlevel)                                

    def draw_title():
        scale = 0.85
        width = 877
        height = 161
        
        title = arcade.load_texture("Assets/Main-Menu/Bongocat-the-game.png")
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, 575, width*scale, height*scale, title)
        
    """def bongo_cat1():
        scale1 = 0.5      
        width = 423
        height = 423

        bongocat1 = arcade.load_texture("Assets/Main-Menu/Bongocat1.png")
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2 + 275, SCREEN_HEIGHT // 2 + 258, width*scale1, height*scale1, bongocat1)

    def bongo_cat2():
        scale2 = 0.4
        width = 680
        height = 689
                
        bongocat2 = arcade.load_texture("Assets/Main-Menu/Bongocat2.png")
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2 + 280, SCREEN_HEIGHT // 2 + 268, width*scale2, height*scale2, bongocat2)"""
        
    def bongo_cat():
        global bongocat1_load
        global bongocat2_load
        global bongocat
        scale1 = 0.5      
        width1 = 423
        height1 = 423 
        if bongocat1_load == True and bongocat2_load == False:         
            bongocat = arcade.load_texture("Assets/Main-Menu/Bongocat1.png")
            arcade.draw_texture_rectangle(SCREEN_WIDTH // 2 + 275, SCREEN_HEIGHT // 2 + 258, width1*scale1, height1*scale1, bongocat)
            bongocat1_load = False
            bongocat2_load = True
            time.sleep(0.5)
            print("bongocat1")
        else:
            """scale2 = 0.4
            width2 = 680
            height2 = 689  """     
            bongocat = arcade.load_texture("Assets/Main-Menu/Bongocat3.png")
            arcade.draw_texture_rectangle(SCREEN_WIDTH // 2 + 275, SCREEN_HEIGHT // 2 + 258, width1*scale1, height1*scale1, bongocat)
            """(SCREEN_WIDTH // 2 + 280, SCREEN_HEIGHT // 2 + 268, width2*scale2, height2*scale2, bongocat)"""
            bongocat1_load = True
            bongocat2_load = False
            time.sleep(0.5)
            print("bongocat2")

    def menusound():
        global menusound_running
        global menusound
        if volume_on == True and menusound_running == False:
            menusound = vlc.MediaPlayer("Assets/Fig_Leaf_Times_Two.mp3")
            menusound.play()
            menusound_running = True
        elif volume_on == True and menusound_running == True:
            pass
        elif volume_on == False:
            menusound.stop()
            menusound_running = False

    def check_mouse_press_playbtn(x,y):
        if x > (playbtncenter_x - playbtnwidth / 2) and x < (playbtncenter_x + playbtnwidth / 2):
            if y < (playbtncenter_y + playbtnheight / 2) and y > (playbtncenter_y - playbtnheight/2):
                print("Never gonna give you up")
    
    def check_mouse_press_settingsbtn(x,y):
        if x > (settingsbtncenter_x - settingsbtnwidth / 2) and x < (settingsbtncenter_x + settingsbtnwidth / 2):
            if y < (settingsbtncenter_y + settingsbtnheight / 2) and y > (settingsbtncenter_y - settingsbtnheight/2):
                print("Settings")
                
    def check_mouse_press_volumebtn(x,y):
        global volume_on
        if x > (volumebtncenter_x - volumebtnwidth / 2) and x < (volumebtncenter_x + volumebtnwidth / 2):
            if y < (volumebtncenter_y + volumebtnheight / 2) and y > (volumebtncenter_y - volumebtnheight / 2):
                if volume_on == True: 
                    volume_on = False
                    main_menu.menusound()
                else:
                    volume_on = True  
                    main_menu.menusound()

    def check_mouse_press_selectcatbtn(x,y):
        if x > (selectcatbtncenter_x - selectcatbtnbtnwidth / 2) and x < (selectcatbtncenter_x + selectcatbtnwidth / 2):
            if y < (selectcatbtncenter_y + selectcatbtnheight / 2) and y > (selectcatbtncenter_y - selectcatbtnheight / 2):
                print("No cat Implented ☹")
                                                         
def draw_Main_Menu():
    main_menu.draw_background()
    main_menu.draw_playbutton()
    main_menu.draw_selectcat()
    main_menu.draw_selectlevel()
    main_menu.draw_settingsbutton()
    main_menu.draw_volumebutton()
    main_menu.draw_title()
    main_menu.bongo_cat()

def check_mouse_press(x,y):
    main_menu.check_mouse_press_playbtn(x,y)
    main_menu.check_mouse_press_volumebtn(x,y)
    main_menu.check_mouse_press_settingsbtn(x,y)
    main_menu.check_mouse_press_selectcatbtn(x,y)

def check_update():
        main_menu.draw_volumebutton()
        main_menu.menusound()
        main_menu.bongo_cat()

class Bongogame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
    def on_draw(self):
        draw_Main_Menu()
    def on_mouse_press(self, x,y, buttons, keymodifiers):
        check_mouse_press(x,y)
    def on_update(self, delta_time):
        check_update()

def main():
    window = Bongogame(SCREEN_WIDTH, SCREEN_HEIGHT, "Bongo Cat: The Game")
    Bongogame.on_update()
    arcade.run()

main()