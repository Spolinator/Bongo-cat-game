import arcade
import os
import time
import pyglet

#constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
volume_on = True

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
    def check_mouse_press_playbtn(x,y):
        if x > (playbtncenter_x - playbtnwidth / 2) and x < (playbtncenter_x + playbtnwidth / 2):
            if y < (playbtncenter_y + playbtnheight / 2) and y > (playbtncenter_y - playbtnheight/2):
                print("I wanna play")



    def menusound():
        if volume_on == True:
            menusound = arcade.load_sound("Assets/Fig_Leaf_Times_Two.mp3")
            arcade.play_sound(menusound)
        else:
            menusound = None

    def draw_settingsbutton():
        scale = 0.7
        width = 87
        height = 87

        settingsbutton = arcade.load_texture("Assets/Main-Menu/Buttons/SETTINGSbtn.png")
        arcade.draw_texture_rectangle(1150.5, 675, width*scale, height*scale, settingsbutton)                        

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
        else:
            volumeoff = arcade.load_texture("Assets/Main-Menu/Buttons/VOLUME-OFFbtn.png")
            arcade.draw_texture_rectangle(volumebtncenter_x, volumebtncenter_y, volumebtnwidth*scale, volumebtnheight*scale, volumeoff)  

    def check_mouse_press_volumebtn(x,y):
        if x > (volumebtncenter_x - volumebtnwidth / 2) and x < (volumebtncenter_x + volumebtnwidth / 2):
            if y < (volumebtncenter_y + volumebtnheight / 2) and y > (volumebtncenter_y - volumebtnheight / 2):
                print("Sound off")
                volume_on == False
        main_menu.draw_volumebutton()      

    def draw_selectcat():
        scale = 0.45
        width = 397
        height = 87
        selectcat = arcade.load_texture("Assets/Main-Menu/Buttons/SELECTCATbtn.png")
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2 - 94.325, SCREEN_HEIGHT / 2 - 60.025, width*scale, height*scale, selectcat)

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
        
    def bongo_cat1():
        scale1 = 0.5      
        width = 423
        height = 423

        bongocat = arcade.load_texture("Assets/Main-Menu/Bongocat1.png")
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2 + 180, SCREEN_HEIGHT // 2 + 200, width*scale1, height*scale1, bongocat, -5)

    def bongo_cat2():
        scale2 = 0.5
        width = 680
        height = 689
                
        bongocat = arcade.load_texture("Assets/Main-Menu/Bongocat2.png")
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2 + 150, SCREEN_HEIGHT // 2 + 500, width*scale2, height*scale2, bongocat, -5)
        
    """def bongo_cat():
        while True:
            main_menu.bongo_cat1()
            time.sleep(0.8)
            main_menu.bongo_cat2()
            time.sleep(0.8)     """                           
                                       

def draw_Main_Menu():
    main_menu.draw_background()
    main_menu.draw_playbutton()
    main_menu.draw_selectcat()
    main_menu.draw_selectlevel()
    main_menu.draw_volumebutton()
    main_menu.draw_settingsbutton()
    main_menu.draw_title() 

def check_mouse_press(x,y):
    main_menu.check_mouse_press_playbtn(x,y)
    main_menu.check_mouse_press_volumebtn(x,y)


class Bongogame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
    def on_draw(self):
        draw_Main_Menu()
    def on_mouse_press(self, x,y, buttons, keymodifiers):
        check_mouse_press(x,y)

  


def main():
    window = Bongogame(SCREEN_WIDTH, SCREEN_HEIGHT, "Bongo Cat: The Game")
    #main_menu.menusound()
    arcade.run()

main()